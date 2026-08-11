# Resort Management Agency (RMA)

Hệ thống hỗ trợ điều hành một doanh nghiệp resort, có tích hợp Agentic AI.

Đây **không phải** phần mềm PMS/POS đặt phòng. Đây là **lớp quản trị vận hành** nằm phía trên:
quy trình (SOP), nhân sự, và các nhận định chiến lược để cải thiện resort.

---

## 1. Bối cảnh

Người dùng chính của hệ thống là **người điều hành resort** (Owner / Managing Director).

Cách làm việc hiện tại:

1. Mỗi chu kỳ, **leader của từng bộ phận gửi báo cáo** lên.
2. Người điều hành **trực tiếp tham gia và quan sát** thực tế tại resort.
3. Từ (1) + (2), người điều hành **đưa ra nhận định** về những gì cần cải thiện
   (phát triển nhân sự, chiến dịch thay đổi kiến trúc/cảnh quan, chuẩn hoá quy trình, dịch vụ mới...).
4. Các nhận định đó trở thành **sáng kiến (initiative)** được triển khai và theo dõi kết quả.

### Vấn đề đang giải quyết

| Vấn đề | Hệ quả |
|---|---|
| Báo cáo rời rạc, mỗi bộ phận một định dạng | Mất thời gian tổng hợp, khó so sánh theo thời gian |
| Báo cáo mang tính tự đánh giá | Số đẹp nhưng không phản ánh thực tế; thiếu đối chiếu |
| Quan sát thực địa nằm trong đầu, không được ghi lại | Không có bằng chứng khi ra quyết định, không truy vết được |
| Nhận định → sáng kiến → kết quả không được đóng vòng | Không biết sáng kiến nào thực sự có tác dụng |
| Tri thức vận hành phụ thuộc vào cá nhân | Người nghỉ việc là mất know-how |

### Hệ thống này làm gì

- Chuẩn hoá và lưu trữ báo cáo chu kỳ theo một lược đồ chung.
- Ghi nhận quan sát thực địa như một **nguồn dữ liệu ngang hàng** với báo cáo.
- Đối chiếu ba nguồn (báo cáo / số liệu hệ thống / quan sát) và **nêu ra chỗ vênh**.
- Phát hiện tín hiệu bất thường và xu hướng trên KPI.
- Đề xuất phương án cải thiện có kèm chi phí – tác động – rủi ro.
- Theo dõi sáng kiến từ lúc ra quyết định đến lúc đo được kết quả.

### Hệ thống này KHÔNG làm gì

- Không thay người điều hành ra quyết định. AI **đề xuất**, người **quyết định**.
- Không tự động ra quyết định nhân sự (đánh giá, kỷ luật, sa thải, lương thưởng).
- Không thay thế PMS/POS/kế toán. Hệ thống **đọc** dữ liệu từ các nguồn đó.

---

## 2. Nguyên tắc thiết kế

Bốn nguyên tắc dưới đây ràng buộc mọi tính năng. Vi phạm nguyên tắc = từ chối tính năng.

### 2.1. Provenance — mọi dữ kiện phải biết đến từ đâu

Mỗi dữ kiện trong hệ thống bắt buộc mang một trong ba nhãn:

| Nhãn | Nguồn | Độ tin cậy |
|---|---|---|
| `REPORTED` | Leader tự khai trong báo cáo chu kỳ | Chủ quan, có thể thiên lệch |
| `MEASURED` | Trích từ hệ thống (PMS, POS, HR, chấm công, review OTA) | Khách quan trong phạm vi hệ thống đo |
| `OBSERVED` | Người điều hành ghi nhận khi tham gia/quan sát thực tế | Chủ quan nhưng độc lập với leader |

Đây là nguyên tắc quan trọng nhất. Không được gộp ba nguồn này thành "dữ liệu".
Giá trị lớn nhất của hệ thống nằm ở chỗ **so ba nguồn với nhau và chỉ ra chỗ lệch**.

### 2.2. Evidence-linked — không có bằng chứng thì không có kết luận

Mọi nhận định do AI sinh ra phải trích dẫn được nguồn cụ thể
(`report_id`, `kpi_record_id`, `observation_id`). Không có nguồn → ghi rõ "chưa đủ dữ liệu",
không được suy diễn hay bịa.

### 2.3. AI đề xuất — người quyết định

Mọi output có sức nặng (nhận định, đề xuất, thay đổi SOP, kế hoạch nhân sự) đi qua
hai bước: **AI soạn bản nháp → người điều hành duyệt/sửa/bác**.
Quyết định đã duyệt được lưu kèm người duyệt và thời điểm.

### 2.4. Đóng vòng — mọi sáng kiến phải đo được

Một sáng kiến không có tiêu chí đo kết quả thì không được tạo.
Vòng đời: `Nhận định → Sáng kiến → Triển khai → Đo → Kết luận (giữ / sửa / bỏ)`.

---

## 3. Phạm vi quản lý

### 3.1. Bộ phận (departments)

Mỗi bộ phận có một leader chịu trách nhiệm báo cáo:

| Mã | Bộ phận | Tiếng Anh |
|---|---|---|
| `FO` | Tiền sảnh / Lễ tân | Front Office |
| `HK` | Buồng phòng | Housekeeping |
| `FB` | Nhà hàng & Bar | F&B Service |
| `KIT` | Bếp | Kitchen |
| `ENG` | Kỹ thuật & Bảo trì | Engineering & Maintenance |
| `SM` | Kinh doanh & Marketing | Sales & Marketing |
| `HR` | Nhân sự & Đào tạo | HR & Training |
| `FIN` | Tài chính & Kế toán | Finance & Accounting |
| `SEC` | An ninh | Security |
| `SPA` | Spa & Giải trí | Spa & Recreation |
| `LND` | Cảnh quan & Cây xanh | Landscape |
| `GX` | Trải nghiệm khách | Guest Experience |

> Danh sách trên là khung mặc định. Cần chốt lại theo sơ đồ tổ chức thực tế của resort.

### 3.2. Ba trục quản lý

**Trục 1 — Quy trình (Process)**
Thư viện SOP theo bộ phận, có phiên bản. Theo dõi độ lệch giữa SOP viết trên giấy và
cách làm thực tế. Đề xuất cập nhật SOP khi thực tế đã chạy khác.

**Trục 2 — Nhân sự (People)**
Sơ đồ tổ chức, khung năng lực theo vị trí, lộ trình phát triển cá nhân,
kế hoạch kế nhiệm cho vị trí then chốt, tín hiệu rủi ro nghỉ việc.

**Trục 3 — Chiến lược (Strategy)**
Danh mục sáng kiến cải thiện: phát triển nhân sự, thay đổi kiến trúc/cảnh quan,
sản phẩm dịch vụ mới, tái cấu trúc quy trình, đầu tư thiết bị.
Mỗi sáng kiến gắn với một luận điểm và một cách đo.

---

## 4. Kiến trúc Agentic AI

```
        ┌─────────────────────────── NGUỒN VÀO ───────────────────────────┐
        │                                                                  │
   Báo cáo leader          Số liệu hệ thống           Quan sát thực địa
   (REPORTED)              (MEASURED)                 (OBSERVED)
        │                       │                            │
        ▼                       ▼                            ▼
   ┌──────────────────────────────────────────────────────────────────┐
   │  1. Intake Agent — chuẩn hoá về lược đồ chung, gắn nhãn nguồn    │
   └──────────────────────────────────────────────────────────────────┘
                                │
                                ▼
   ┌──────────────────────────────────────────────────────────────────┐
   │  2. Reconciliation Agent — đối chiếu 3 nguồn, nêu chỗ vênh       │
   └──────────────────────────────────────────────────────────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
   ┌──────────┐          ┌──────────┐            ┌──────────┐
   │3. Signal │          │4. Process│            │5. People │
   │  Agent   │          │  Agent   │            │  Agent   │
   │KPI, xu   │          │SOP drift │            │năng lực, │
   │hướng,    │          │đề xuất   │            │kế nhiệm, │
   │bất thường│          │chuẩn hoá │            │rủi ro    │
   └──────────┘          └──────────┘            └──────────┘
        └───────────────────────┼───────────────────────┘
                                ▼
   ┌──────────────────────────────────────────────────────────────────┐
   │  6. Strategy Agent — tổng hợp thành phương án (chi phí/tác động/ │
   │     rủi ro), xếp ưu tiên, trích dẫn bằng chứng                   │
   └──────────────────────────────────────────────────────────────────┘
                                │
                                ▼
            ┌───────────────────────────────────────┐
            │   BẢN BRIEF CHU KỲ  →  NGƯỜI DUYỆT    │  ← điểm dừng bắt buộc
            └───────────────────────────────────────┘
                                │
                                ▼
   ┌──────────────────────────────────────────────────────────────────┐
   │  7. Initiative Agent — theo dõi sáng kiến đã duyệt đến khi đo    │
   │     được kết quả, nhắc mốc, báo lệch tiến độ                     │
   └──────────────────────────────────────────────────────────────────┘
```

### Mô tả từng agent

**1. Intake Agent** — Nhận báo cáo ở dạng tự do (văn bản, Excel, form, ảnh chụp)
và chuyển về lược đồ `CycleReport` chuẩn. Không diễn giải, không đánh giá.
Thiếu trường nào thì đánh dấu thiếu, không tự điền.

**2. Reconciliation Agent** — Đối chiếu con số leader khai với số liệu hệ thống,
và đối chiếu nội dung báo cáo với quan sát thực địa cùng kỳ.
Output là **danh sách điểm vênh** kèm mức độ, không phải kết luận ai đúng ai sai.

**3. Signal Agent** — Chạy trên KPI theo thời gian: phát hiện vượt ngưỡng,
đảo chiều xu hướng, bất thường theo mùa. Chỉ báo tín hiệu, không giải thích nguyên nhân.

**4. Process Agent** — Giữ thư viện SOP. So SOP với cách làm thực tế phản ánh qua
báo cáo và quan sát. Đề xuất bản cập nhật SOP dưới dạng diff để người duyệt.

**5. People Agent** — Duy trì khung năng lực và hồ sơ phát triển.
Đề xuất nội dung đào tạo, ứng viên kế nhiệm, cảnh báo rủi ro nghỉ việc.
**Không** chấm điểm nhân viên, **không** đề xuất kỷ luật hay sa thải.

**6. Strategy Agent** — Tổng hợp output của 2–5 thành các phương án cải thiện.
Mỗi phương án bắt buộc có: luận điểm, bằng chứng trích dẫn, ước tính chi phí,
tác động kỳ vọng, rủi ro, cách đo kết quả.

**7. Initiative Agent** — Theo dõi sáng kiến đã được duyệt: mốc tiến độ,
người chịu trách nhiệm, kết quả đo được so với kỳ vọng ban đầu.

---

## 5. Mô hình dữ liệu cốt lõi

```
Resort
 └─ Department ──── Position ──── Employee
                                     │
                                     └─ CompetencyRecord, DevelopmentPlan

Cycle (tuần / tháng / quý)
 ├─ CycleReport      (REPORTED — do leader nộp)
 ├─ KpiRecord        (MEASURED — trích từ hệ thống)
 └─ Observation      (OBSERVED — người điều hành ghi nhận)
         │
         ▼
    Discrepancy      (điểm vênh giữa các nguồn)
         │
         ▼
    Finding          (nhận định — AI nháp, người duyệt)
         │
         ▼
    Initiative       (sáng kiến) ──── Milestone ──── OutcomeMeasurement
                          │
                          └─ liên kết tới SopDocument nếu là thay đổi quy trình

SopDocument (có phiên bản) ──── SopVersion ──── SopDriftSignal
```

Ba thực thể quan trọng nhất cần làm đúng ngay từ đầu:
`Observation` (đừng để mất dữ liệu quan sát), `Discrepancy` (giá trị lõi của hệ thống),
`Initiative` (điểm đóng vòng).

---

## 6. Chu kỳ vận hành

| Chu kỳ | Việc diễn ra |
|---|---|
| **Tuần** | Leader nộp báo cáo tuần; Intake + Reconciliation chạy; brief ngắn cho người điều hành |
| **Tháng** | Signal + Process + People chạy đầy đủ; Strategy Agent soạn phương án; phiên duyệt sáng kiến |
| **Quý** | Đánh giá kết quả sáng kiến đã triển khai; rà soát lại SOP và khung năng lực |
| **Bất kỳ** | Ghi quan sát thực địa (không chờ chu kỳ — quan sát rẻ nhất khi ghi ngay lúc thấy) |

---

## 7. Bộ chỉ số

Chỉ số dưới đây là khung khởi đầu, cần chốt ngưỡng theo hạng và quy mô resort thực tế.

### Doanh thu & hiệu quả
`OCC` (công suất phòng) · `ADR` (giá phòng bình quân) · `RevPAR` · `GOPPAR` ·
`ALOS` (số đêm lưu trú bình quân) · `F&B capture rate` · `CPOR` (chi phí trên phòng bán)

### Trải nghiệm khách
`GSS` (điểm hài lòng nội bộ) · `NPS` · điểm review OTA (Booking / Agoda / TripAdvisor / Google) ·
tỷ lệ khách quay lại · số khiếu nại và thời gian xử lý

### Nhân sự
Tỷ lệ nghỉ việc · thời gian tuyển trung bình · giờ đào tạo/người ·
`labor cost %` · tỷ lệ vị trí then chốt có người kế nhiệm

### Vận hành & tài sản
Tồn đọng bảo trì · thời gian trung bình xử lý sự cố · tỷ lệ tuân thủ SOP ·
số sự cố an toàn · chất lượng cảnh quan (đánh giá định kỳ)

---

## 8. Ranh giới & Guardrails

Đây là các ràng buộc cứng, được kiểm tra trong code chứ không chỉ ghi trong prompt.

1. **Không tự động ra quyết định nhân sự.** Mọi output liên quan đến cá nhân
   chỉ mang tính hỗ trợ phát triển. Đánh giá, kỷ luật, chấm dứt hợp đồng: 100% do người quyết định.
2. **Dữ liệu cá nhân nhân viên** được phân quyền theo vai trò. Log mọi lượt truy cập.
3. **Không bịa số.** Thiếu dữ liệu thì báo thiếu. Mọi con số phải truy được về nguồn.
4. **Nhật ký kiểm toán (audit trail).** Mọi đề xuất AI và mọi quyết định của người dùng
   đều được lưu: ai, khi nào, dựa trên bằng chứng gì.
5. **Không đẩy dữ liệu nhân sự / tài chính ra dịch vụ ngoài** khi chưa có phê duyệt rõ ràng.
6. **Tuân thủ luật lao động Việt Nam** trong mọi đề xuất liên quan đến giờ làm,
   ca kíp, hợp đồng.

---

## 9. Tech stack

> **Trạng thái: đề xuất, chưa chốt.** Phần này là khuyến nghị mặc định để bắt đầu,
> không phải quyết định cuối cùng. Cần xác nhận trước khi viết dòng code đầu tiên.

| Lớp | Đề xuất | Lý do |
|---|---|---|
| Backend | Python 3.12 + FastAPI | Hệ sinh thái AI/data tốt nhất, SDK Anthropic đầy đủ |
| Database | PostgreSQL | Quan hệ rõ ràng, JSONB cho báo cáo dạng tự do, `pgvector` cho tìm kiếm SOP |
| AI | Claude API (`anthropic` SDK) | Tool use + structured outputs phù hợp kiến trúc agent |
| Frontend | Next.js + TypeScript | Dashboard, form nhập báo cáo, màn hình duyệt |
| Nền tảng | Docker Compose (giai đoạn đầu) | Đơn giản, đủ cho quy mô một resort |

### Lựa chọn model

| Tác vụ | Model | Lý do |
|---|---|---|
| Strategy, Reconciliation, Process, People | `claude-opus-5` | Cần suy luận sâu, nhiều nguồn dữ liệu, kết luận có sức nặng |
| Intake (chuẩn hoá báo cáo), phân loại | `claude-haiku-4-5` | Khối lượng lớn, tác vụ đơn giản, tối ưu chi phí |

Với mọi lời gọi có suy luận: dùng adaptive thinking và `output_config.effort` để điều chỉnh
độ sâu; dùng structured outputs (`output_config.format`) cho mọi output cần lược đồ cố định.

---

## 10. Cấu trúc thư mục dự kiến

```
resort-management-agency/
├── README.md
├── CLAUDE.md                  # bối cảnh cho AI coding agent
├── documents/                 # hồ sơ bối cảnh nghiệp vụ (nguồn công khai + nội bộ)
│   ├── domain/                # từ điển nghiệp vụ, sơ đồ tổ chức, định nghĩa KPI
│   ├── sop/                   # thư viện SOP mẫu theo bộ phận
│   └── decisions/             # ADR — nhật ký quyết định kiến trúc
├── docs/                      # ⚠️ SINH TỰ ĐỘNG — thư mục GitHub Pages phục vụ ra internet
│   └── index.html             # tạo bởi scripts/build-site.py, đừng sửa trực tiếp
├── scripts/
│   └── build-site.py          # bọc báo cáo thành trang HTML hoàn chỉnh cho Pages
├── backend/
│   ├── app/
│   │   ├── domain/            # entity, value object, quy tắc nghiệp vụ
│   │   ├── agents/            # 7 agent, mỗi agent một module
│   │   ├── api/               # route FastAPI
│   │   ├── integrations/      # đọc dữ liệu PMS/POS/HR
│   │   └── guardrails/        # kiểm tra ràng buộc cứng ở mục 8
│   ├── migrations/
│   └── tests/
├── frontend/
└── infra/
```

---

## 11. Lộ trình

Mỗi giai đoạn là một lát cắt dọc chạy được, không phải một tầng kiến trúc.

| GĐ | Nội dung | Kết quả nhìn thấy được |
|---|---|---|
| **0** | Đóng khung nghiệp vụ: sơ đồ tổ chức, mẫu báo cáo, định nghĩa KPI, lược đồ dữ liệu | Tài liệu domain được chốt, không có code |
| **1** | Intake + lưu trữ + brief chu kỳ | Leader nộp báo cáo → hệ thống sinh bản brief cho người điều hành |
| **2** | Ghi quan sát thực địa + Reconciliation | Hệ thống chỉ ra điểm vênh giữa báo cáo và thực tế |
| **3** | Signal Agent + dashboard KPI | Cảnh báo bất thường tự động trên số liệu |
| **4** | Process Agent + People Agent | Đề xuất cập nhật SOP và kế hoạch phát triển nhân sự |
| **5** | Strategy Agent + Initiative Agent | Đóng vòng: nhận định → sáng kiến → đo kết quả |

Nguyên tắc: **không xây giai đoạn sau khi giai đoạn trước chưa có người dùng thật dùng.**

---

## 12. Những điểm cần chốt

Các câu hỏi dưới đây chưa có câu trả lời và sẽ ảnh hưởng trực tiếp đến thiết kế:

1. **Quy mô** — một resort hay nhiều resort? (ảnh hưởng tới multi-tenant ngay từ schema)
2. **Chu kỳ báo cáo chính** — tuần hay tháng?
3. **Sơ đồ tổ chức thực tế** — danh sách bộ phận ở mục 3.1 cần được thay bằng cơ cấu thật.
4. **Nguồn số liệu `MEASURED`** — resort đang dùng PMS/POS/phần mềm nhân sự nào?
   Có API không, hay phải nhập tay / import file?
5. **Người dùng hệ thống** — chỉ người điều hành, hay leader cũng đăng nhập để nộp báo cáo?
6. **Ngôn ngữ giao diện** — tiếng Việt, hay song ngữ Việt–Anh?
7. **Tech stack** — xác nhận hoặc thay đổi đề xuất ở mục 9.

---

## 13. Trạng thái hiện tại

Repo đang ở **giai đoạn 0**. Chưa có code. Hai file `README.md` và `CLAUDE.md`
là tài liệu đóng khung bối cảnh, sẽ được cập nhật khi các câu hỏi ở mục 12 được chốt.
