# documents/

Hồ sơ bối cảnh nghiệp vụ về **hai cơ sở** trong danh mục quản lý.

Đây là nơi lưu **thông tin nền về doanh nghiệp**. Tài liệu kỹ thuật, ADR và định nghĩa KPI
sẽ nằm trong các thư mục con của chính `documents/` khi bắt đầu code.

> ⚠️ **Đừng nhầm với `docs/` ở gốc repo.** Thư mục đó là **trang web công khai** do
> GitHub Pages phục vụ ra internet, được sinh tự động bởi `scripts/build-site.py`.
> Bất cứ file nào đặt vào `docs/` đều thành công khai.

---

## Hai cơ sở

| Cơ sở | Vị trí | Bản chất | Hồ sơ |
|---|---|---|---|
| **Anh Nguyễn Ocean Front Villas** | Nha Trang, Khánh Hoà | Dự án BĐS 79 biệt thự, vận hành phân mảnh | [→ hồ sơ](anh-nguyen-oceanfront/00-tom-tat-dieu-hanh.md) |
| **Jiva Hoa Lu Retreat** | Hoa Lư, Ninh Bình | Resort 63 phòng, vận hành tập trung, SLH | [→ hồ sơ](jiva-hoa-lu/README.md) |

### ⭐ [So sánh hai resort](so-sanh-hai-resort.md)

Bảng đối chiếu, mùa vụ lệch nhau, và ba thay đổi kiến trúc bắt buộc cho hệ thống RMA.
**Đọc file này nếu chỉ có thời gian đọc một file.**

---

## Báo cáo trình bày

| File | Nội dung |
|---|---|
| [bao-cao-boi-canh.html](bao-cao-boi-canh.html) | Báo cáo HTML có tab chuyển đổi giữa hai resort + tab so sánh. Nguồn để sinh trang GitHub Pages |

Sửa file HTML xong, chạy `python3 scripts/build-site.py` để cập nhật `docs/index.html`.

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
- Một chủ đề = một file. Một cơ sở = một thư mục.
- Khi có thông tin nội bộ, **tạo file mới** `20-thong-tin-noi-bo.md` trong thư mục
  của cơ sở đó, thay vì sửa đè lên các file nghiên cứu công khai (00–12).

---

## Trạng thái

| Nhóm | Anh Nguyễn | Jiva |
|---|---|---|
| Thông tin công khai | ✅ Đã thu thập | ✅ Đã thu thập |
| Chủ sở hữu & tài chính | ✅ Có (báo chí) | ❌ Không công khai |
| Thông tin nội bộ vận hành | ❌ Chưa có | ❌ Chưa có |
| Câu hỏi chặn | **Phạm vi quản lý** | **Vai trò của bạn + có PMS không** |
