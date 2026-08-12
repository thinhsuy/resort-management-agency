# 10 — Khoảng trống thông tin · Jiva Hoa Lu Retreat

> Tra cứu **12/08/2026** · [Mục lục](README.md) · [Quy ước nhãn](../README.md#nhãn-độ-tin-cậy)

---

Với Anh Nguyễn, câu hỏi chặn là **phạm vi quản lý**. Với Jiva, phạm vi rõ ràng —
một resort vận hành tập trung. Khoảng trống ở đây là **dữ liệu vận hành nội bộ**,
thứ không bao giờ công khai với bất kỳ resort nào.

---

## 🔴 Nhóm A — Sở hữu & quản trị

| # | Câu hỏi | Vì sao quan trọng |
|---|---|---|
| **JA1** | Pháp nhân chủ sở hữu là ai? | Không có nguồn công khai nào nêu tên |
| **JA2** | Có công ty quản lý khách sạn riêng không, hay chủ tự vận hành? | Quyết định ai ra quyết định vận hành |
| **JA3** | **Vai trò của bạn là gì?** Tổng quản lý · giám sát chủ sở hữu · quản lý danh mục hai resort? | Quyết định luồng báo cáo trong hệ thống RMA |
| **JA4** | Ai là GM hiện tại? Bạn ở trên hay ngang hàng? | Xác định ai nộp báo cáo cho ai |

## 🔴 Nhóm B — Hợp đồng SLH

| # | Câu hỏi | Vì sao quan trọng |
|---|---|---|
| **JB5** | Phí thành viên SLH bao nhiêu? Tính theo doanh thu hay cố định? | Khoản chi phí đáng kể chưa nắm được |
| **JB6** | Tiêu chuẩn nào bắt buộc phải duy trì? | Phải đưa vào SOP như ràng buộc cứng |
| **JB7** | Chu kỳ đánh giá lại tư cách thành viên? | Cần lịch chuẩn bị trước |
| **JB8** | Tỷ trọng doanh thu từ SLH/Hilton so với OTA phổ thông? | Đo mức phụ thuộc vào kênh này |

## 🟠 Nhóm C — Vận hành

| # | Câu hỏi |
|---|---|
| **JC9** | Tổng số nhân sự? Cơ cấu bộ phận thực tế? |
| **JC10** | **Đang dùng PMS/POS nào? Có API không?** ← quyết định cách lấy dữ liệu `MEASURED` |
| **JC11** | Có channel manager không? Đồng bộ SLH/Hilton thế nào? |
| **JC12** | Tiện ích nào **đang hoạt động** vs **chưa mở**? (The Cellar Door mở 12/2025 — còn gì nữa?) |
| **JC13** | Có SOP sẵn chưa? Ở dạng nào — văn bản, phần mềm, hay truyền miệng? |

## 🟡 Nhóm D — Kinh tế

| # | Câu hỏi |
|---|---|
| **JD14** | **OCC và ADR thực tế 12 tháng gần nhất, theo tháng và theo hạng phòng** |
| **JD15** | Cơ cấu doanh thu: phòng / F&B / spa / tour / khác |
| **JD16** | Tỷ trọng kênh bán và hoa hồng từng kênh |
| **JD17** | Cơ cấu chi phí → tính được GOPPAR |
| **JD18** | Đang lỗ hay lãi? Mục tiêu tài chính? |

## 🟢 Nhóm E — Rủi ro & tuân thủ

| # | Câu hỏi |
|---|---|
| **JE19** | **Quy chế bảo tồn di sản** áp dụng cho khu đất — được phép làm gì, cấm gì? |
| **JE20** | Đã có sự cố nào chưa: ngập, bão, hư hại công trình gỗ? |
| **JE21** | Bảo trì nhà cổ đang theo lịch nào, nhà thầu nào? |
| **JE22** | Bảo hiểm tài sản và trách nhiệm ở mức nào? |

---

## Thứ tự nên hỏi

1. **JA3 + JA4** — vai trò của bạn. Không có cái này thì không thiết kế được luồng báo cáo.
2. **JC10** — PMS. Quyết định toàn bộ kiến trúc lấy dữ liệu, và nên làm trước Anh Nguyễn nếu Jiva có API.
3. **JD14** — OCC/ADR. Không có thì mọi phân tích kinh tế đều là phỏng đoán.
4. **JB6 + JE19** — hai bộ ràng buộc cứng (SLH và di sản) phải vào SOP trước khi viết SOP.
5. Phần còn lại thu thập dần.

---

## Cách dùng tài liệu này

Khi có câu trả lời, **tạo file mới** `20-thong-tin-noi-bo.md` trong thư mục này
thay vì sửa đè lên các file nghiên cứu công khai (00–12) — để luôn phân biệt được
nguồn công khai với nguồn nội bộ, đúng nguyên tắc provenance của dự án.

---

[← 09 — Thị trường Ninh Bình](09-thi-truong-ninh-binh.md) · [Mục lục](README.md) · [11 — Hàm ý cho hệ thống →](11-ham-y-cho-he-thong.md)
