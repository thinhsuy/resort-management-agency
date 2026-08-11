# 10 — Khoảng trống thông tin

> Hồ sơ bối cảnh **Anh Nguyễn Ocean Front Villas** · Tra cứu **11/08/2026**
> · [Mục lục](README.md) · Nhãn độ tin cậy: xem [quy ước](README.md#nhãn-độ-tin-cậy)

---

Những thông tin dưới đây **không thể tìm thấy công khai** và ảnh hưởng trực tiếp
tới thiết kế hệ thống RMA. Cần chủ dự án trả lời.

---

## 🔴 Nhóm A — Phạm vi (câu hỏi chặn)

Đây là nhóm quan trọng nhất. Chưa có câu trả lời thì mọi thiết kế đều là phỏng đoán.

### A1. Bạn quản lý cái gì?

- [ ] (a) Một hoặc vài căn biệt thự cho thuê ngắn ngày
- [ ] (b) Một đơn vị quản lý ~14 căn (kiểu `anhnguyenvillas.com`)
- [ ] (c) Toàn bộ khu 79 căn
- [ ] (d) Phía chủ đầu tư — Công ty TNHH Anh Nguyễn
- [ ] (e) Khác: ______

### A2. Bao nhiêu căn, mã căn nào?

Hệ mã công khai đang là **B1, B2, B8, B29…**

### A3. Quan hệ pháp lý của bạn với các căn đó?

- [ ] Chủ sở hữu
- [ ] Thuê lại để khai thác (master lease)
- [ ] Nhận uỷ thác quản lý cho chủ (management contract)
- [ ] Khác: ______

> **Vì sao câu này quan trọng:** nó quyết định bạn kiểm soát được gì.
> Nếu là uỷ thác quản lý, bạn không tự quyết được đầu tư cải tạo.
> Nếu là thuê lại, bạn chịu toàn bộ rủi ro công suất.

---

## 🟠 Nhóm B — Vận hành

### B4. Tổng số nhân sự?

Bao nhiêu người toàn thời gian, bao nhiêu thời vụ?

### B5. Có bao nhiêu quản lý cấp trung sẽ nộp báo cáo mỗi chu kỳ?

Đây là con số quyết định quy mô luồng `REPORTED` trong hệ thống.

### B6. Cơ cấu bộ phận thực tế?

Danh sách 12 bộ phận trong README gốc là khung ngành khách sạn — chắc chắn không đúng
với thực tế một đơn vị quản lý villa.

### B7. Đang dùng phần mềm gì?

| Chức năng | Phần mềm hiện dùng |
|---|---|
| Quản lý đặt phòng | ______ |
| Channel manager (đồng bộ OTA) | ______ |
| Thu chi / kế toán | ______ |
| Chấm công / nhân sự | ______ |
| Giao việc / vận hành | ______ |

Hay hoàn toàn thủ công / Excel / Zalo?

> **Vì sao quan trọng:** quyết định nguồn `MEASURED` lấy được qua API hay phải nhập tay.

### B8. Tỷ trọng kênh bán?

| Kênh | % doanh thu |
|---|---:|
| OTA (Booking, Agoda, Airbnb…) | ___% |
| Trực tiếp (website, Zalo, Facebook, điện thoại) | ___% |
| Môi giới / đại lý | ___% |
| Khách quen / giới thiệu | ___% |

### B9. Dịch vụ đang cung cấp?

- [ ] Bếp / F&B tại villa
- [ ] Đưa đón sân bay
- [ ] Nhân sự trực tại villa 24/7
- [ ] Dọn phòng hằng ngày
- [ ] Tour / hoạt động
- [ ] Tổ chức sự kiện (tiệc, cưới, team building)

---

## 🟡 Nhóm C — Kinh tế

### C10. Công suất (OCC) thực tế 12 tháng gần nhất?

Theo tháng, để thấy hình dạng mùa vụ.

### C11. Giá bán thực tế bình quân (ADR)?

**Không phải giá niêm yết.** Giá niêm yết công khai là 5–15 triệu/đêm
([xem 07](07-kinh-te-van-hanh.md)) — cần biết mức thực.

### C12. Cơ cấu chi phí?

| Khoản mục | Chi phí/tháng |
|---|---:|
| Nhân sự | ______ |
| Điện nước | ______ |
| Bảo trì | ______ |
| Hoa hồng OTA | ______ |
| Phí quản lý khu | ______ |
| Marketing | ______ |
| Khác | ______ |

### C13. Đang lỗ hay lãi? Mục tiêu tài chính là gì?

---

## 🟢 Nhóm D — Rủi ro

### D14. Đã từng có sự cố sạt lở, ngập, hư hại do mưa bão chưa?

Nếu có: khi nào, mức độ, xử lý thế nào?

### D15. Ràng buộc với ban quản lý khu?

- Phí quản lý phải nộp là bao nhiêu?
- Quy chế nội khu có hạn chế gì với cho thuê ngắn ngày không?
- Tiện ích chung nào bạn được dùng, cái nào không?

### D16. Tình trạng bảo hiểm?

Bảo hiểm tài sản, bảo hiểm trách nhiệm với khách — mức nào?

---

## Cách dùng tài liệu này

1. **Trả lời nhóm A trước.** Ba câu này quyết định toàn bộ phần còn lại.
2. Nhóm B và C có thể trả lời dần — nhưng cần xong trước khi bắt đầu giai đoạn 1.
3. Nhóm D nên trả lời trước khi thiết kế SOP kỹ thuật.
4. Khi có câu trả lời, **tạo file mới `20-thong-tin-noi-bo.md`** thay vì sửa đè lên
   các tài liệu nghiên cứu công khai (01–09) — để luôn phân biệt được nguồn công khai
   với nguồn nội bộ.

---

[← 09 — Thị trường Khánh Hoà](09-thi-truong-khanh-hoa.md) · [Mục lục](README.md) · [11 — Hàm ý cho hệ thống RMA →](11-ham-y-cho-he-thong.md)
