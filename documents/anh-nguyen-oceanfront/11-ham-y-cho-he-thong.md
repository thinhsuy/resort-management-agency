# 11 — Hàm ý cho hệ thống RMA

> Hồ sơ bối cảnh **Anh Nguyễn Ocean Front Villas** · Tra cứu **11/08/2026**
> · [Mục lục](README.md) · Nhãn độ tin cậy: xem [quy ước](README.md#nhãn-độ-tin-cậy)

---

README gốc của dự án được viết trước khi có bối cảnh cụ thể, nên dùng **khung chuẩn
ngành khách sạn**. Sau nghiên cứu, nhiều giả định trong đó không khớp thực tế.

Tài liệu này liệt kê các điều chỉnh đề xuất. **Chưa áp dụng vào README** — chờ
trả lời [nhóm câu hỏi A](10-khoang-trong-thong-tin.md#-nhóm-a--phạm-vi-câu-hỏi-chặn) trước.

---

## Bảng đối chiếu: giả định vs thực tế

| # | Giả định trong README | Thực tế theo nghiên cứu | Điều chỉnh đề xuất |
|---|---|---|---|
| 1 | **12 bộ phận** có leader riêng | Nhiều khả năng là đội <40 người ([06](06-mo-hinh-van-hanh.md)) | Rút gọn còn **4–6 bộ phận** thực chất; chấp nhận leader kiêm nhiệm nhiều vai |
| 2 | `MEASURED` lấy từ PMS/POS **qua API** | Nhiều khả năng **không có PMS trung tâm** ([06](06-mo-hinh-van-hanh.md)) | Thiết kế nhánh **nhập tay / import Excel làm đường chính**, API là tuỳ chọn |
| 3 | Bộ KPI khách sạn đầy đủ (GOPPAR, F&B capture, CPOR…) | Mô hình villa cho thuê không có phần lớn các chỉ số này | Thu gọn còn: **OCC · ADR · RevPAR/căn · doanh thu ròng/căn · chi phí/đêm · số review · điểm review** |
| 4 | Chu kỳ báo cáo **tuần + tháng** | Quy mô nhỏ → tuần có thể quá dày | **Tháng làm chu kỳ chính**; tuần chỉ dùng cho vận hành, không cần brief AI đầy đủ |
| 5 | — | **Rủi ro sạt lở là có thật** ([05](05-phap-ly-rui-ro.md)) | Bổ sung **SOP kiểm tra rủi ro thiên tai**, tần suất tăng mùa mưa tháng 9–12 |
| 6 | — | **Chỉ 6 review trên OTA** ([08](08-ota-danh-gia-khach.md)) | KPI giai đoạn đầu là **tăng số lượng review**, chưa phải tối ưu điểm |
| 7 | — | **Phân phối online yếu** ([08](08-ota-danh-gia-khach.md)) | Đưa "mở rộng kênh phân phối" vào danh mục sáng kiến **ưu tiên sớm** |
| 8 | — | **Tiện ích chung do chủ đầu tư quản** ([06](06-mo-hinh-van-hanh.md)) | Thêm loại `Observation` cho hạ tầng **ngoài tầm kiểm soát** — ghi nhận để phản ánh lên ban quản lý khu |

---

## Điều chỉnh cụ thể theo từng trục

### Trục quy trình (SOP)

SOP đầu tiên nên viết, theo thứ tự ưu tiên:

1. **Kiểm tra an toàn sườn núi & thoát nước** — mùa mưa (rủi ro cao nhất, [05](05-phap-ly-rui-ro.md))
2. **Quy trình check-in / check-out villa** — điểm chạm quan trọng nhất với khách
3. **Quy trình dọn dẹp & bàn giao giữa hai lượt khách** — ảnh hưởng trực tiếp điểm "Sạch sẽ"
4. **Quy trình xin review sau lưu trú** — đòn bẩy rẻ nhất cho vấn đề ở [08](08-ota-danh-gia-khach.md)
5. **Bảo trì định kỳ hồ bơi & thiết bị** — chi phí lớn, dễ bị bỏ sót

### Trục nhân sự

Với đội nhỏ, khung năng lực 12 bộ phận là quá nặng. Đề xuất:

- Xây khung năng lực cho **3–5 vị trí cốt lõi** trước (quản lý, lễ tân/CSKH, buồng phòng, kỹ thuật)
- Ưu tiên **kế nhiệm cho vị trí quản lý** — đội nhỏ thì rủi ro phụ thuộc cá nhân rất cao
- Bỏ qua các chỉ số HR quy mô lớn (labor cost % toàn khu, giờ đào tạo/người) ở giai đoạn đầu

### Trục chiến lược

Ba sáng kiến có vẻ đáng ưu tiên nhất dựa trên nghiên cứu:

| Sáng kiến | Luận điểm | Cách đo |
|---|---|---|
| **Mở rộng & chuẩn hoá kênh phân phối** | Điểm review 9,8 nhưng chỉ 6 review → sản phẩm tốt, phân phối yếu | Số listing · số review/tháng · % doanh thu từ OTA |
| **Chiến lược lấp mùa thấp** | Cao điểm Tết ~82% nhưng không biết mùa thấp; đây là chỗ quyết định lợi nhuận năm | OCC tháng thấp nhất · RevPAR cả năm |
| **Chương trình an toàn sườn núi** | Rủi ro sạt lở có thật, hậu quả nghiêm trọng | Số lần kiểm tra đúng lịch · số sự cố · thời gian xử lý |

> Đây là **đề xuất từ dữ liệu công khai**, chưa qua đối chiếu với quan sát thực địa
> của bạn. Đúng tinh thần nguyên tắc của dự án: AI đề xuất, người quyết định.

---

## Điều KHÔNG nên thay đổi

Bốn nguyên tắc trong `CLAUDE.md` vẫn giữ nguyên, và nghiên cứu này càng củng cố chúng:

| Nguyên tắc | Vì sao nghiên cứu củng cố nó |
|---|---|
| **Provenance** (`REPORTED`/`MEASURED`/`OBSERVED`) | Chính tài liệu này đã phải dùng 4 nhãn độ tin cậy để không trộn thông tin marketing với sự thật. Nếu nghiên cứu công khai đã cần thế, dữ liệu vận hành càng cần |
| **Evidence-linked** | Ba nguồn mâu thuẫn nhau về pháp lý sổ đỏ ([05](05-phap-ly-rui-ro.md)) và về giá bán ([07](07-kinh-te-van-hanh.md)) — không trích nguồn thì không thể phát hiện |
| **AI đề xuất, người quyết định** | Ba sáng kiến ở trên đều là suy luận từ dữ liệu công khai, thiếu bối cảnh thực địa. Không thể tự động hoá |
| **Đóng vòng** | Dự án 20 năm với 4 lần điều chỉnh quy hoạch mà không rõ kết quả ([03](03-lich-su-du-an.md)) là ví dụ sống về cái giá của việc không đo kết quả |

---

## Bước tiếp theo

1. Trả lời [nhóm A](10-khoang-trong-thong-tin.md#-nhóm-a--phạm-vi-câu-hỏi-chặn) — xác định phạm vi
2. Cập nhật README theo bảng đối chiếu ở trên
3. Đi thực địa lập danh sách tiện ích *đang hoạt động* vs *chưa có* ([04](04-quy-mo-san-pham.md))
4. Thu thập dữ liệu OCC/ADR/chi phí 12 tháng ([07](07-kinh-te-van-hanh.md))
5. Bắt đầu giai đoạn 1

---

[← 10 — Khoảng trống thông tin](10-khoang-trong-thong-tin.md) · [Mục lục](README.md) · [12 — Nguồn tham khảo →](12-nguon-tham-khao.md)
