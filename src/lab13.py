"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# A1 · Các hàm kỳ vọng chạy, xác suất thành công và hệ số chi phí.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not 0 < p <= 1:
        raise ValueError('p phải nằm trong (0, 1]')
    if k is None:
        return 1.0 / p
    if k < 1:
        raise ValueError('k phải là số nguyên dương')
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not 0 <= p <= 1:
        raise ValueError('p phải nằm trong [0, 1]')
    if k is None:
        return 1.0 if p > 0 else 0.0
    if k < 1:
        raise ValueError('k phải là số nguyên dương')
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    success = ti_le_thanh_cong(p, k)
    if success == 0:
        return math.inf
    return so_lan_chay_ky_vong(p, k) / success


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# A2 · Mô hình chi phí dùng lại cho phân tích độ nhạy ở B.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    req_ids = set(reqs['request_id'])
    runs = runs[runs['request_id'].isin(req_ids)].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay].copy()
        handed_off = reqs['so_lan_chay'].astype(int) > max_lan_chay
        reqs.loc[handed_off, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[handed_off, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    token_cost = (runs['tokens_in'] / 1000 * gia_vao
                  + runs['tokens_out'] / 1000 * gia_ra).sum()
    tool_cost = (runs['tool_calls'] * gia_tool).sum()
    review_cost = (reqs['phut_xem_lai_simulated'].astype(float).sum()
                   * luong_phut * he_so_xem_lai)
    rework_cost = (reqs['phut_lam_lai_simulated'].astype(float).sum()
                   * luong_phut * he_so_lam_lai)
    total = token_cost + tool_cost + review_cost + rework_cost
    successes = int((reqs['ket_qua'] == 'thanh_cong').sum())
    requests_count = len(reqs)
    cps = total / successes if successes else math.inf
    token_tool = token_cost + tool_cost
    return {
        'token': token_cost,
        'tool': tool_cost,
        'chay_lai': ((runs.loc[runs['attempt'] > 1, 'tokens_in'] / 1000 * gia_vao
                      + runs.loc[runs['attempt'] > 1, 'tokens_out'] / 1000 * gia_ra)
                     + runs.loc[runs['attempt'] > 1, 'tool_calls'] * gia_tool).sum(),
        'xem_lai': review_cost,
        'lam_lai': rework_cost,
        'tong': total,
        'thanh_cong': successes,
        'cps': cps,
        'hoa_don_moi_yc': token_tool / requests_count if requests_count else math.inf,
        'so_yeu_cau': requests_count,
        'khong_thanh_cong': requests_count - successes,
    }


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    print('\nA2 · Mô hình chi phí (đ)')
    for ten in ('token', 'tool', 'chay_lai', 'xem_lai', 'lam_lai', 'tong', 'thanh_cong', 'cps', 'hoa_don_moi_yc'):
        print(f'{ten:20s} {ket_qua[ten]:14,.2f}')

    # A3 · Phân tích theo loại yêu cầu.
    print('\nA3 · Theo loại yêu cầu')
    for loai in sorted(reqs['loai'].unique()):
        subset = reqs[reqs['loai'] == loai]
        result = mo_hinh(runs, subset)
        print(f"{loai:12s} n={len(subset):4d} success={result['thanh_cong']/len(subset):.4%} "
              f"runs/request={len(runs[runs['request_id'].isin(set(subset['request_id']))])/len(subset):.4f} "
              f"cps={result['cps']:,.2f} ({result['cps']/BASELINE:.4f}x baseline)")
    print('A3 · Tỉ lệ status=ok theo attempt')
    category_runs = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    for loai in sorted(reqs['loai'].unique()):
        subset = category_runs[category_runs['loai'] == loai]
        rates = subset.groupby('attempt')['status'].apply(lambda values: (values == 'ok').mean())
        print(f"{loai:12s} " + ' '.join(f"lần {attempt}: {rate:.2%}" for attempt, rate in rates.items()))

    # A4 · Chi phí cố định nel per-success volume assumption.
    scope = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    scope_result = mo_hinh(runs, scope)
    monthly_success = 45000 * scope_result['thanh_cong'] / len(reqs)
    fixed_per_success = 40_000_000 / monthly_success
    print('\nA4 · Chi phí cố định, phạm vi nội địa + hàng nặng (đ)')
    for volume_factor, label in ((1.0, '45,000 yêu cầu/tháng'), (0.5, 'một nửa khối lượng')):
        variable_per_success = scope_result['cps']
        fixed = fixed_per_success / volume_factor
        print(f'{label:28s} successes/month={monthly_success*volume_factor:,.0f} '
              f'fixed/success={fixed:,.2f} total/success={variable_per_success+fixed:,.2f} '
              f'({(variable_per_success+fixed)/BASELINE:.4f}x baseline)')

    # B1/B2 · Độ nhạy theo từng giả định và một cặp yếu tố.
    scenarios = {
        'Giá token gấp đôi': {'gia_vao': 52, 'gia_ra': 260},
        'Giá token giảm một nửa': {'gia_vao': 13, 'gia_ra': 65},
        'Tỉ lệ xem lại gấp đôi': {'he_so_xem_lai': 2},
        'Tỉ lệ xem lại giảm một nửa': {'he_so_xem_lai': 0.5},
        'Số ca làm lại gấp đôi': {'he_so_lam_lai': 2},
        'Số ca làm lại giảm một nửa': {'he_so_lam_lai': 0.5},
        'Lương nhân viên tăng 25%': {'luong_phut': 2500},
        'Chỉ cho chạy tối đa 2 lần': {'max_lan_chay': 2},
        'Chỉ cho chạy 1 lần': {'max_lan_chay': 1},
    }
    print('\nB1 · Độ nhạy')
    for name, kwargs in scenarios.items():
        result = mo_hinh(runs, reqs, **kwargs)
        print(f"{name:30s} cps={result['cps']:9,.2f} change={(result['cps']/ket_qua['cps']-1)*100:+7.2f}%")
    pair = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)
    print(f"{'Token x2 + xem lại x2':30s} cps={pair['cps']:9,.2f} change={(pair['cps']/ket_qua['cps']-1)*100:+7.2f}%")

    # B3 · Chi phí toàn hệ thống tính cả yêu cầu chuyển nhân viên.
    print('\nB3 · Chi phí cả hệ thống (đ)')
    for limit in (1, 2, 3):
        result = mo_hinh(runs, reqs, max_lan_chay=limit)
        system_cost = result['tong'] + result['khong_thanh_cong'] * BASELINE
        print(f"{limit} lần: assistant={result['tong']:,.2f} failed={result['khong_thanh_cong']} "
              f"system={system_cost:,.2f} cps={result['cps']:,.2f}")

    # B4 · 100% review trong phạm vi, dùng 5 phút/request và 9 phút/rework như đề bài.
    scope_ids = set(scope['request_id'])
    scope_runs = runs[runs['request_id'].isin(scope_ids)]
    requests_with_ok = set(scope_runs.loc[scope_runs['status'] == 'ok', 'request_id'])
    review_minutes = len(requests_with_ok) * 5
    rework_cases = int((scope['ket_qua'] == 'lam_lai').sum())
    token_tool = scope_result['token'] + scope_result['tool']
    b4_total = token_tool + review_minutes * LUONG_PHUT + rework_cases * 9 * LUONG_PHUT
    b4_success = scope_result['thanh_cong']
    print('\nB4 · Xem lại 100% trong phạm vi (giả định đề bài, đ)')
    print(f"requests={len(scope)} reviewed_after_ok={len(requests_with_ok)} review_minutes={review_minutes} "
          f"rework_cases={rework_cases} total={b4_total:,.2f} cps={b4_total/b4_success:,.2f} "
          f"({b4_total/b4_success/BASELINE:.4f}x baseline)")

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
