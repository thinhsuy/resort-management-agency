# documents/

Hồ sơ bối cảnh nghiệp vụ về **Anh Nguyễn Ocean Front Villas, Nha Trang** — đối tượng
mà hệ thống RMA sẽ quản lý.

Đây là nơi lưu **thông tin nền về doanh nghiệp**. Tài liệu kỹ thuật, ADR và định nghĩa KPI
sẽ nằm trong các thư mục con của chính `documents/` khi bắt đầu code.

> ⚠️ **Đừng nhầm với `docs/` ở gốc repo.** Thư mục đó là **trang web công khai** do
> GitHub Pages phục vụ ra internet, được sinh tự động bởi `scripts/build-site.py`.
> Bất cứ file nào đặt vào `docs/` đều thành công khai.

**Ngày tra cứu: 11/08/2026.** Toàn bộ dựa trên nguồn công khai. Chưa có thông tin nội bộ.

---

## Mục lục

| # | Tài liệu | Nội dung |
|---|---|---|
| 00 | [Tóm tắt điều hành](00-tom-tat-dieu-hanh.md) | **Đọc file này trước.** Ba phát hiện quan trọng nhất |
| 01 | [Định danh & vị trí](01-dinh-danh-vi-tri.md) | Tên, địa chỉ, quy mô đất, bản đồ các website dễ nhầm lẫn |
| 02 | [Chủ đầu tư](02-chu-dau-tu.md) | Công ty TNHH Anh Nguyễn: sở hữu, tài chính 2016–2020 |
| 03 | [Lịch sử dự án](03-lich-su-du-an.md) | Dòng thời gian 2005 → 2027, các lần điều chỉnh quy hoạch |
| 04 | [Quy mô & sản phẩm](04-quy-mo-san-pham.md) | 3 phân khu, 79 biệt thự, cấu hình, tiện ích |
| 05 | [Pháp lý & rủi ro](05-phap-ly-rui-ro.md) | Sạt lở, đất rừng phòng hộ, vi phạm khoáng sản, mâu thuẫn về sổ |
| 06 | [Mô hình vận hành](06-mo-hinh-van-hanh.md) | **Quan trọng.** Cho thuê phân mảnh, không có PMS trung tâm |
| 07 | [Kinh tế vận hành](07-kinh-te-van-hanh.md) | Giá thuê, giá bán, ước tính doanh thu |
| 08 | [OTA & đánh giá khách](08-ota-danh-gia-khach.md) | Điểm 9,8/10 nhưng chỉ 6 review |
| 09 | [Thị trường Khánh Hoà](09-thi-truong-khanh-hoa.md) | Số liệu du lịch 2025, cạnh tranh, tính mùa vụ |
| 10 | [Khoảng trống thông tin](10-khoang-trong-thong-tin.md) | **14 câu hỏi cần chủ dự án trả lời** |
| 11 | [Hàm ý cho hệ thống RMA](11-ham-y-cho-he-thong.md) | Điều chỉnh đề xuất so với README gốc |
| 12 | [Nguồn tham khảo](12-nguon-tham-khao.md) | Toàn bộ link nguồn |

---

## Quy ước

### Nhãn độ tin cậy

Mọi khẳng định trong các tài liệu này đều gắn một nhãn:

| Nhãn | Ý nghĩa |
|---|---|
| `[XÁC MINH]` | Nhiều nguồn độc lập khớp nhau |
| `[MỘT NGUỒN]` | Chỉ tìm thấy ở một nguồn — chưa đối chứng |
| `[MARKETING]` | Lấy từ tài liệu bán hàng, có thể thổi phồng |
| `[SUY LUẬN]` | Do phân tích rút ra, chưa xác thực |

Đây là áp dụng trực tiếp nguyên tắc **provenance** của dự án (xem `CLAUDE.md`):
không bao giờ trộn thông tin đã xác minh với thông tin marketing hay suy đoán.

### Quy ước khác

- Mỗi tài liệu ghi rõ **ngày tra cứu** ở đầu file. Thông tin thị trường và pháp lý
  hết hạn nhanh — quá 6 tháng thì coi là cần tra lại.
- Một chủ đề = một file. Không gom nhiều chủ đề vào một tài liệu.
- Khi có thông tin nội bộ từ phía vận hành, **tạo file mới** (đánh số từ 20 trở đi)
  thay vì sửa đè lên các file nghiên cứu công khai này.

---

## Trạng thái

| Nhóm | Trạng thái |
|---|---|
| Thông tin công khai | ✅ Đã thu thập (file 01–09) |
| Thông tin nội bộ vận hành | ❌ Chưa có — xem [file 10](10-khoang-trong-thong-tin.md) |
| Phạm vi quản lý thực tế | ❌ **Chưa xác nhận** — đây là câu hỏi chặn |
