# CLAUDE.md

Bối cảnh dự án cho AI coding agent. Đọc `README.md` để có mô tả đầy đủ.

## Dự án là gì

Hệ thống quản trị vận hành resort có tích hợp Agentic AI. Quản lý ba trục:
**quy trình (SOP)**, **nhân sự**, và **các nhận định chiến lược để cải thiện resort**.

Không phải PMS/POS đặt phòng. Đây là lớp quản trị nằm phía trên các hệ thống đó.

## Đối tượng cụ thể

**Anh Nguyễn Ocean Front Villas, Nha Trang** — hồ sơ bối cảnh ở `documents/`
(13 tài liệu, mục lục tại `documents/README.md`). Đọc `documents/00-tom-tat-dieu-hanh.md`
trước khi thiết kế gì.

Ba điều cần biết ngay:
- Đây là **dự án BĐS 79 biệt thự sở hữu riêng lẻ**, không phải resort có một ban điều hành.
  Việc cho thuê đang **phân mảnh qua nhiều đầu mối**, không có PMS trung tâm.
- **Phạm vi quản lý thực tế của người dùng chưa được xác nhận** (1 căn? 14 căn? cả khu?
  hay phía chủ đầu tư?). Đây là câu hỏi chặn — hỏi trước khi giả định.
- Khu đất nằm trong **vùng nguy cơ sạt lở** — là rủi ro vận hành thật, cần vào SOP kỹ thuật.

## Người dùng chính

Người điều hành resort (Owner / Managing Director). Cách họ làm việc:
leader từng bộ phận báo cáo mỗi chu kỳ → người điều hành đọc báo cáo + tự quan sát thực tế
→ đưa ra nhận định cần cải thiện → biến thành sáng kiến và theo dõi kết quả.

Hệ thống hỗ trợ đúng vòng lặp đó.

## Bốn nguyên tắc bất di bất dịch

1. **Provenance** — mọi dữ kiện mang nhãn `REPORTED` (leader khai) /
   `MEASURED` (số liệu hệ thống) / `OBSERVED` (quan sát thực địa).
   Không bao giờ gộp ba nguồn này. Giá trị lõi của hệ thống là **so chúng và chỉ ra chỗ vênh**.
2. **Evidence-linked** — mọi kết luận AI sinh ra phải trích dẫn `report_id` / `kpi_record_id` /
   `observation_id`. Không có bằng chứng thì ghi "chưa đủ dữ liệu", tuyệt đối không suy diễn.
3. **AI đề xuất, người quyết định** — mọi output có sức nặng đi qua hai bước:
   AI soạn nháp → người duyệt. Lưu người duyệt và thời điểm.
4. **Đóng vòng** — sáng kiến không có tiêu chí đo kết quả thì không được tạo.

## Guardrails cứng (kiểm tra bằng code, không chỉ bằng prompt)

- Không tự động ra quyết định nhân sự (đánh giá, kỷ luật, sa thải, lương thưởng).
  People Agent chỉ hỗ trợ **phát triển** năng lực.
- Không bịa số. Thiếu dữ liệu → báo thiếu.
- Audit trail cho mọi đề xuất AI và mọi quyết định của người dùng.
- Dữ liệu cá nhân nhân viên: phân quyền theo vai trò, log truy cập.
- Đề xuất liên quan giờ làm / ca kíp / hợp đồng phải tuân thủ luật lao động Việt Nam.

## Bảy agent

`Intake` (chuẩn hoá báo cáo) → `Reconciliation` (đối chiếu 3 nguồn) →
`Signal` (bất thường KPI) · `Process` (SOP drift) · `People` (năng lực, kế nhiệm) →
`Strategy` (soạn phương án) → **[người duyệt]** → `Initiative` (theo dõi kết quả)

Mỗi agent một module riêng. Agent chỉ trả về dữ liệu có cấu trúc; việc định dạng
và hiển thị do code làm, không để model tự quyết định format.

## Quy ước

- **Ngôn ngữ tài liệu:** tiếng Việt. **Code, tên biến, tên bảng, commit message:** tiếng Anh.
- Thuật ngữ nghiệp vụ khách sạn giữ nguyên tiếng Anh: `OCC`, `ADR`, `RevPAR`, `GOPPAR`,
  `ALOS`, `CPOR`, `NPS`, `SOP`, `Housekeeping`, `Front Office`.
- Mã bộ phận viết hoa: `FO`, `HK`, `FB`, `KIT`, `ENG`, `SM`, `HR`, `FIN`, `SEC`, `SPA`, `LND`, `GX`.
- Quyết định kiến trúc ghi vào `docs/decisions/` dưới dạng ADR.

## Trạng thái

**Giai đoạn 0 — chưa có code.** Repo mới chỉ có tài liệu đóng khung.

Tech stack ở mục 9 của README (Python + FastAPI + PostgreSQL + Claude API + Next.js)
là **đề xuất chưa được chốt**. Đừng scaffold code theo stack đó khi chưa có xác nhận.

Bảy câu hỏi ở mục 12 của README (quy mô, chu kỳ, sơ đồ tổ chức thật, nguồn dữ liệu,
người dùng, ngôn ngữ giao diện, stack) đều chưa có câu trả lời. Nếu một tác vụ phụ thuộc
vào câu trả lời nào trong đó, hãy hỏi thay vì tự giả định.

## Khi làm việc trong repo này

- Ưu tiên làm rõ nghiệp vụ trước khi viết code. Dự án đang ở giai đoạn đóng khung.
- Danh sách bộ phận, KPI, ngưỡng cảnh báo trong README là **khung mặc định**,
  chưa phải số liệu thật của resort. Đừng hardcode chúng như thể đã được chốt.
- Khi thêm tính năng, kiểm tra nó không vi phạm bốn nguyên tắc và các guardrail ở trên.
