# 撰寫慣例

## 一、檔案結構

一篇一資料夾、一章一檔案。不要把整篇塞進單一檔案 —— 第六篇有 8 個項目，合成一個 `06-infrastructure.md` 會讓 Agent 每次載入都浪費大量 context。

```
software-spec/
├── INDEX.md                      # 人看的入口：文件地圖與閱讀順序
├── spec.manifest.yaml            # Agent 看的入口：項目 → 檔案對應
├── spec-coverage.yaml            # 涵蓋度常駐檔案
├── 01-business/
│   ├── 01-background.md          # S01
│   ├── 02-glossary.md            # S02
│   └── 06-assumptions.md         # S06
├── 02-business-design/
│   ├── 08-business-rules.md      # S08
│   ├── 09-state-machines.md      # S09
│   └── 11-requirements.md        # S11
├── 03-system-design/
├── 04-data-design/
├── 05-interface-design/
├── 06-infrastructure/
├── 07-engineering/
│   └── adr/
│       ├── ADR-001-xxx.md
│       └── ADR-002-xxx.md
├── 08-quality-assurance/
└── assets/
    └── （僅放無法用 Mermaid 表達的素材，例如 UI 截圖）
```

**ADR 一則一檔**，不要合併成一個大檔 —— 它們的生命週期各自獨立。

### spec.manifest.yaml

Agent 的載入索引。先讀 manifest 決定要載入哪幾個檔案，而不是全讀。

```yaml
project: shopee-ai-cs
version: 0.4.0
items:
  - id: S08
    title: 業務規則
    file: 02-business-design/08-business-rules.md
    id_prefix: BR
    tags: [business, rules, validation]
    roles: [pm, backend, qa]
  - id: S11
    title: 功能需求與驗收標準
    file: 02-business-design/11-requirements.md
    id_prefix: [FR, AC]
    tags: [requirements, acceptance]
    roles: [pm, backend, frontend, qa]
```

`tags` 與 `roles` 讓 Agent 能依任務性質篩選：後端實作任務不需要載入 S26 UI 規劃。

---

## 二、檔案 frontmatter

每個規格檔案開頭都要有：

```yaml
---
id: S08
title: 業務規則
status: confirmed          # confirmed | draft
version: 3
owner: <負責人>
last_updated: 2026-07-28
depends_on: [S02, S09, S10]
---
```

`status` 只會是 `confirmed` 或 `draft` —— 其他三種狀態（`tbd` / `n/a` / `missing`）的項目根本沒有檔案，只存在於 `spec-coverage.yaml`。

**版本紀錄放在這裡，不要維護全域 Revision History。** 拆檔之後全域紀錄必然過期，而過期的版本資訊比沒有更糟。

---

## 三、depends_on 與影響反查

### 宣告方向

`depends_on` 宣告的是「本文件的內容建立在哪些項目的結論之上」。

例：API 規格（S23）的端點設計來自功能需求（S11）與業務規則（S08），所以 `S23` 的 frontmatter 寫 `depends_on: [S08, S11, S15]`。

### 反查規則

每次修改任一項目後，**必須**掃描所有規格檔案的 frontmatter，找出 `depends_on` 包含被改動項目的檔案，並在回應中列出。

```
改動：S20 資料庫設計（新增 messages.status 欄位）

受影響（depends_on 包含 S20）
  S19 業務資料模型   ER 圖需同步
  S23 API 規格       API-007 回應內容可能需增欄位
  S22 資料遷移       需補 backfill 計畫
```

**不要自動修正這些檔案。** 自動連鎖修改會失控，且會把單一決策放大成大量未經確認的變更。只列清單，由人決定。

### 常見依賴鏈

| 改動項目 | 通常受影響 |
|---|---|
| S02 Glossary | S19、S20（命名一致性） |
| S08 業務規則 | S11、S17、S23、S38 |
| S09 狀態機 | S08、S19、S23、S38 |
| S11 功能需求 | S14、S23、S38 |
| S20 資料庫設計 | S19、S21、S22、S23 |
| S23 API 規格 | S26、S38 |
| S29 非功能需求 | S13、S32、S34 |

---

## 四、ID 命名規範

| 前綴 | 用於 | 來源項目 |
|---|---|---|
| `S01`–`S40` | 考量項目代號 | 固定，不新增 |
| `BR-xxx` | 業務規則 | S08 |
| `FR-xxx` | 功能需求 | S11 |
| `AC-<FR>-<n>` | 驗收標準 | S11 |
| `NFR-xxx` | 非功能需求 | S29 |
| `API-xxx` | API 端點 | S23 |
| `ADR-xxx` | 架構決策 | S35 |

### 三條硬性規則

1. **ID 一旦發出，永不變更。** 章節被合併、搬移、重寫都不影響已發出的 ID。
2. **ID 永不重用。** 廢棄的項目標記為 `deprecated` 並保留條目，不要把號碼讓給新項目 —— 舊的程式碼註解、commit message、測試名稱都還指向它。
3. **編號連續遞增，不補洞。** 刪除 BR-004 之後，下一條仍是 BR-008，不要填回 004。

---

## 五、章節合併

內容都很少的相鄰項目可以合併成一章，但**項目 ID 不能變**。合併後的章節在 manifest 中登記多個 id：

```yaml
  - id: [S13, S14]
    title: 系統架構與模組設計
    file: 03-system-design/13-architecture.md
```

### 允許的合併組合

| 合併 | 條件 |
|---|---|
| S13 + S14 | 模組數量少於 5 個 |
| S19 + S20 | 沒有獨立的業務資料模型需求 |
| S24 + S30 | 事件與批次共用同一套排程機制 |
| S27 + S28 | 無跨境資料、合規需求單純 |
| S32 + S33 | 單一環境、備援策略簡單 |
| S03 + S04 | 尚未建立 Persona，痛點與目標的內容合計不足一頁 |

**不在此表的合併需要先詢問使用者。** 自由合併會導致每次產出的結構都不同，文件之間無法比較，diff 也會爆炸。

以下項目**不得與其他項目合併**，因為它們是 Agent 最常直接查詢的對象：S08 業務規則、S09 狀態機、S11 功能需求、S23 API 規格、S35 ADR。

---

## 六、內容格式

### 圖一律用 Mermaid

不要用 png / jpg / drawio 匯出圖。理由有二：Agent 讀不懂圖片；圖與文字必然不同步，而不同步的圖比沒有圖更誤導人。

`assets/` 只放真的無法用 Mermaid 表達的東西（UI 截圖、設計稿）。

### 結構化資料用表格或 YAML，不用散文

業務規則、功能需求、API、錯誤碼、狀態轉換、設定項 —— 這些都要能被逐條引用與比對，散文形式會讓 Agent 難以精確定位。

```markdown
❌ 付款成功之後才可以建立發票，另外退款每筆訂單只能執行一次。

✅
| ID | 規則 | 違反時行為 |
|---|---|---|
| BR-001 | 付款成功才能建立 Invoice | 拒絕，回傳 409 |
| BR-002 | 退款每筆訂單只能執行一次 | 拒絕，回傳 422 |
```

### 唯一歸屬原則

同一個主題只能有一個正式歸屬，其他地方只放交叉連結。

對人來說重複只是囉唆；**對 Agent 來說，兩處寫得不一樣就是矛盾指令，而它不會報錯，只會挑一個照做。**

| 主題 | 唯一歸屬 | 只能交叉引用的地方 |
|---|---|---|
| Retry / DLQ | S17 | S24、S30 |
| 錯誤碼定義 | S23 | S36 |
| Audit Log 要求 | S28 | S27、S34 |
| Audit Log 實作 | S34 | S28 |
| 資料搬遷計畫 | S22 | S32 |
| 快取策略 | S21 | S29 |
| AI 元件細節 | S18 | S13、S14、S25 |
| Role 業務定義 | S12 | S15 |
| Permission 矩陣 | S15 | S12 |
