# 06 — Mô hình vận hành · Jiva Hoa Lu Retreat

> Tra cứu **12/08/2026** · [Mục lục](README.md) · [Quy ước nhãn](../README.md#nhãn-độ-tin-cậy)

---

**Đây là mục có ảnh hưởng lớn nhất tới thiết kế hệ thống RMA** — và là nơi Jiva
khác Anh Nguyễn nhiều nhất.

---

## Vận hành tập trung, một đầu mối `[XÁC MINH]`

Mọi dấu hiệu công khai đều cho thấy Jiva là **một cơ sở lưu trú vận hành thống nhất**:

| Dấu hiệu | Quan sát được |
|---|---|
| Một website chính thức duy nhất | `jivahoaluretreat.com` |
| Một số hotline, hai email theo chức năng | `inquiry@` (hỏi chung) · `reservation@` (đặt phòng) |
| Một listing trên mỗi OTA | Booking, Expedia, Traveloka, Trip.com — mỗi nơi **một** property |
| Lễ tân 24/7, an ninh 24/7, bác sĩ trực gọi | Có bộ máy vận hành thường trực |
| Chính sách nhận/trả phòng thống nhất | 14:00 / 12:00 |
| Chương trình đặt trực tiếp | Mã `JIVALIFE` áp dụng toàn cơ sở |

**Không có dấu vết nào của mô hình phân mảnh** — không môi giới cá nhân rao lẻ từng villa,
không listing trùng lặp, không đầu mối bên thứ ba.

---

## Bộ máy nhân sự

| Chỉ số | Giá trị | Nguồn |
|---|---:|---|
| Nhân sự từ Ninh Bình | **70%** | `[MARKETING]` |
| Nhân sự từ miền Bắc | **96%** | `[MARKETING]` |
| Tổng số nhân sự | **không rõ** | — |

Resort công bố chính sách đào tạo và đề bạt người địa phương lên vị trí quản lý.

> **Ước tính quy mô đội ngũ:** một resort 5 sao 63 phòng có 2 nhà hàng, spa, gym và
> lễ tân 24/7 thường cần **80–130 nhân sự** (tỷ lệ 1,3–2 nhân sự/phòng là mức thông dụng
> cho phân khúc luxury). `[SUY LUẬN]` — cần xác nhận số thật.

Nếu con số này đúng, đây là **tổ chức đủ lớn để có cơ cấu bộ phận đầy đủ** —
tức là mô hình 12 bộ phận trong thiết kế RMA gốc **có thể phù hợp với Jiva**,
trong khi không phù hợp với Anh Nguyễn.

---

## Kênh phân phối — nhiều tầng, có chủ đích

```
  Khách quốc tế cao cấp          Khách OTA phổ thông        Khách trực tiếp
          │                              │                        │
   SLH · Hilton · Michelin      Booking · Expedia ·         Website + mã JIVALIFE
   Kiwi · Jacada · Via          Traveloka · Trip.com        (giảm 5% phòng, 10% spa)
          │                              │                        │
          └──────────────────────────────┴────────────────────────┘
                                    │
                          Một hệ thống đặt phòng
```

Ba tầng kênh phục vụ ba nhóm khách khác nhau, với mã đặt trực tiếp để kéo khách
khỏi kênh có hoa hồng cao. Đây là **cấu trúc phân phối trưởng thành**. `[SUY LUẬN]`

---

## Hệ quả cho thiết kế hệ thống RMA

| Đặc điểm | Hệ quả |
|---|---|
| Có ban điều hành thống nhất | Vòng lặp **leader báo cáo → người điều hành nhận định** hoạt động đúng như thiết kế gốc |
| Nhiều bộ phận thật (FO, HK, F&B, Bếp, Spa, Kỹ thuật, An ninh…) | Cơ cấu bộ phận trong README **áp dụng được**, chỉ cần tinh chỉnh |
| Nhiều điểm doanh thu (phòng, 2 nhà hàng, bar, spa, tour) | Cần chỉ số **ngoài phòng**: F&B capture rate, doanh thu spa/khách, tỷ lệ mua tour |
| Có ràng buộc tiêu chuẩn SLH | SOP phải neo vào tiêu chuẩn thương hiệu, không tự do định nghĩa |
| Nhiều kênh phân phối | Cần theo dõi **tỷ trọng kênh** và chi phí hoa hồng theo kênh |
| Nhiều khả năng đã có PMS | Nguồn dữ liệu `MEASURED` **có thể lấy qua hệ thống** — khác hẳn Anh Nguyễn |

> **Điểm quan trọng nhất:** nếu Jiva có PMS/POS thật, thì hệ thống RMA nên
> **xây nhánh tích hợp dữ liệu cho Jiva trước**, rồi mới xử lý nhánh nhập tay cho Anh Nguyễn.
> Làm ngược lại sẽ tốn công gấp đôi. `[SUY LUẬN]`

---

## Câu hỏi cần trả lời

1. Đang dùng PMS nào? (Opera, Smile, ezCloud, Cloudbeds…) Có API không?
2. Có channel manager không? Đồng bộ với SLH/Hilton thế nào?
3. Tổng nhân sự và cơ cấu bộ phận thực tế?
4. Ai là Tổng quản lý (GM)? Bạn ở vai trò nào so với GM?

→ [10 — Khoảng trống thông tin](10-khoang-trong-thong-tin.md)

---

[← 05 — Rủi ro](05-rui-ro.md) · [Mục lục](README.md) · [07 — Kinh tế vận hành →](07-kinh-te-van-hanh.md)
