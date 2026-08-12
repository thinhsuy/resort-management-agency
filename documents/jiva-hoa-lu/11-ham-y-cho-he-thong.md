# 11 — Hàm ý cho hệ thống RMA · Jiva Hoa Lu Retreat

> Tra cứu **12/08/2026** · [Mục lục](README.md) · [Quy ước nhãn](../README.md#nhãn-độ-tin-cậy)

---

## Điểm mấu chốt

**Jiva khớp với thiết kế RMA gốc; Anh Nguyễn thì không.**

README ban đầu giả định một resort có ban điều hành, nhiều bộ phận, leader báo cáo theo chu kỳ,
và dữ liệu lấy từ PMS/POS. Giả định đó **sai với Anh Nguyễn** nhưng **nhiều khả năng đúng với Jiva**.

Nghĩa là hệ thống không nên chọn một trong hai mô hình — nó phải **hỗ trợ cả hai**.

---

## Đối chiếu với thiết kế gốc

| # | Giả định trong README | Jiva | Anh Nguyễn |
|---|---|---|---|
| 1 | Có ban điều hành, leader báo cáo mỗi chu kỳ | ✅ Khớp | ❌ Không có |
| 2 | Nhiều bộ phận (FO, HK, F&B, Bếp, Spa, ENG…) | ✅ Khớp | ❌ Quá lớn |
| 3 | Dữ liệu `MEASURED` từ PMS/POS qua API | ⚠️ Nhiều khả năng có — cần xác nhận | ❌ Không có |
| 4 | Bộ chỉ số khách sạn đầy đủ (OCC, ADR, RevPAR, GOPPAR, F&B capture) | ✅ Áp dụng được | ❌ Phần lớn không dùng được |
| 5 | Chu kỳ tuần + tháng | ✅ Phù hợp | ⚠️ Tháng là đủ |
| 6 | — | Thêm: **ràng buộc tiêu chuẩn SLH** | Thêm: **rủi ro sạt lở** |
| 7 | — | Thêm: **quy chế di sản UNESCO** | Thêm: **pháp lý dự án** |

---

## Ba điều chỉnh kiến trúc cần thiết

### 1. Hệ thống phải đa cơ sở (multi-property) ngay từ schema

Đây là thay đổi lớn nhất so với thiết kế gốc. Mọi thực thể — báo cáo, KPI, quan sát,
SOP, nhân sự, sáng kiến — đều phải gắn `property_id`.

Sửa sau sẽ rất tốn. **Cần quyết định trước khi viết dòng code đầu tiên.**

### 2. Bộ chỉ số phải theo cấu hình từng cơ sở, không cứng trong code

Cùng tên chỉ số nhưng ý nghĩa và giai đoạn khác nhau:

| Chỉ số | Jiva | Anh Nguyễn |
|---|---|---|
| Điểm review | Giữ 4,9 và thứ hạng 1/68 | **Tăng số lượng** từ 6 lên đủ mẫu |
| F&B capture rate | Áp dụng — có 2 nhà hàng | Không áp dụng |
| GOPPAR | Áp dụng | Không tính được |
| Doanh thu/căn | Không phải đơn vị phù hợp | Đơn vị chính |

→ Ngưỡng cảnh báo và bộ chỉ số phải là **dữ liệu cấu hình**, không hardcode.

### 3. Nguồn `MEASURED` phải hỗ trợ hai đường song song

| Cơ sở | Đường lấy dữ liệu |
|---|---|
| Jiva | Tích hợp PMS/POS (nếu có API) |
| Anh Nguyễn | Nhập tay / import Excel |

**Thứ tự triển khai đề xuất:** làm nhánh Jiva trước nếu có API — vì nó cho vòng lặp
dữ liệu hoàn chỉnh sớm nhất, từ đó kiểm chứng được thiết kế agent. Nhánh nhập tay
cho Anh Nguyễn làm sau, dùng lại cùng lược đồ. `[SUY LUẬN]`

---

## SOP nên viết trước cho Jiva

Khác thứ tự với Anh Nguyễn, vì rủi ro và ràng buộc khác nhau:

| # | SOP | Lý do |
|---|---|---|
| 1 | **Tuân thủ tiêu chuẩn SLH** | Ràng buộc cứng, mất là mất kênh phân phối quốc tế |
| 2 | **Bảo trì công trình gỗ cổ** | Chuyên biệt, tốn kém, dễ bị bỏ sót |
| 3 | **Buồng phòng & bàn giao** | Đang đạt 5,0 sạch sẽ — cần giữ, không để tụt |
| 4 | **Tuân thủ quy chế di sản** | Mọi thay đổi vật lý đều phải qua bước kiểm tra |
| 5 | **Vận hành F&B hai nhà hàng** | Có phàn nàn lặp về buffet sáng |

So với Anh Nguyễn, nơi SOP số 1 là **kiểm tra an toàn sườn núi**.

---

## Sáng kiến đề xuất cho Jiva `[SUY LUẬN]`

| Sáng kiến | Luận điểm | Cách đo |
|---|---|---|
| **Cải thiện buffet sáng** | Phàn nàn lặp lại, chi phí thấp, tác động trực tiếp lên điểm "Đáng tiền" (4,8 — thấp nhất) | Điểm "Đáng tiền" · số phàn nàn về ăn sáng |
| **Đẩy tỷ trọng đặt trực tiếp** | Đã có mã `JIVALIFE`; mỗi điểm % chuyển từ OTA sang trực tiếp tiết kiệm 15–20% hoa hồng | % doanh thu đặt trực tiếp |
| **Lấp mùa thấp bằng danh mục hai resort** | Mùa vụ Ninh Bình và Nha Trang lệch nhau | OCC tháng thấp nhất của cả hai |

Sáng kiến thứ ba **chỉ khả thi khi quản lý cả hai** — đây là giá trị riêng của việc
vận hành danh mục, xem [So sánh hai resort](../so-sanh-hai-resort.md).

---

[← 10 — Khoảng trống thông tin](10-khoang-trong-thong-tin.md) · [Mục lục](README.md) · [12 — Nguồn tham khảo →](12-nguon-tham-khao.md)
