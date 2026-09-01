# 百炼®标书开放 API 契约参考

> **契约兼容标注（skill biaoshu-bailian 2.2.3）**
> - 适配后端 API：`/api/open/v1`
> - 契约核对日期：2026-09-01（接入标书查重 Open API；`max_total_pages` 同步到 500；字数计费话术与标书审查规则对齐；生成任务细进度与成品短时下载链接对齐）（后端字段/枚举变化时更新此处并 bump 版本）
> - 关键枚举快照：`risk_level ∈ {high, review, tip}` · `result_type ∈ {suspected, detected}` · `priority ∈ {high, medium, low}`
> - 渲染兼容策略：`report.py` 同时兼容文档值（高/中/低）与实测值、证据多形态、缺字段不崩——契约小幅漂移只需 PATCH，不触发 MAJOR。

> ⚠️ **数据外发与知情同意**：本文档所有接口均为百炼®标书云端服务——上传的招标/投标文件**常含商业、报价与个人信息**，将发送至 `biaoshu.zhiliaobiaoxun.com` 处理，标书生成会消耗账户可用字数；**上传的文件与产出的结果会留存在百炼®标书服务器**（任务结果与成品 .docx 约 7 天后过期，数据以 Api Key 所属账户身份存于平台、可登录官网查看管理）。**首次上传前必须确认用户知悉并同意**；完整披露见 SKILL.md「⚠️ 权限与数据说明」。

`scripts/zcm.py` 已封装下列全部端点；本文档供需要直接发请求、排查错误或理解返回结构时查阅。
所有契约均经后端源码 + 本地实跑核实。

## 目录
- [鉴权与环境](#鉴权与环境)
- [核心模型与约定](#核心模型与约定)
- [端点详情](#端点详情)
- [错误码速查](#错误码速查)
- [注意事项](#注意事项)

---

## 鉴权与环境

- **Base URL（生产）**：`https://biaoshu.zhiliaobiaoxun.com/api/open/v1`
- 每个请求都带鉴权头：

| Header | 值 | 说明 |
|---|---|---|
| `X-App-Key` | Api Key | 必填，形如 `bk_live_xxxxx` |
| `Idempotency-Key` | UUID（可选） | 相同 key 24h 内返回同一 `job_id`，不重复扣费 |

- 服务开关：开放 API 受超级管理员『系统设置』总开关控制，**关闭时整层返回 404**。
- 凭证获取：官网 <https://biaoshu.zhiliaobiaoxun.com/> 注册 → 左侧菜单『Skill 接入 → 获取 Api Key』，面板首次打开自动生成 Key。
  Api Key 可随时在『Skill 接入 → 获取 Api Key』面板查看；重置后旧 Key 立即失效。

## 核心模型与约定

- **project_id**：统一句柄，由「智能解读」产出，是**标书制作与标书审查的招标文件入口**。后续抽包 / 生成 / 合规复用同一 project，不重复解读、不重复计费。标书查重是独立任务，可选上传招标文件作为公共表述基线，不依赖 project_id。
- **job_id**：每个异步任务的对外句柄。提交类接口立即返回 `{ "job_id": "..." }`。
- **任务状态**：`queued` → `running` → `succeeded` / `failed` / `canceled`。
- **上传方式**：本 skill 一律 `multipart/form-data` 直传本地文件（后端另有 `file_url` 入参，**本 skill 不使用**，也不做任何远程抓取）。
- **限流**：每 Api Key 默认 60 req/min、同时进行任务 ≤ 3；超限 429。
- **统一错误体**：`{ "error": { "code": "...", "message": "..." } }`
- **计费**：实际消耗可用字数只发生在 ③生成（正文逐条 + 导出）；①解读、②抽包、④标书审查、⑤标书查重本身不消耗字数。
- **提交门槛**：通过开放 API / Skill 提交时，①解读、③生成、④标书审查、⑤标书查重都要求账户有可用字数才能发起；②抽包与各类查询接口不受该门槛限制。`wallet_balance` 为兼容旧客户端的字段名，当前语义按可用字数理解。
- **结果时效**：任务结果与 .docx 默认保留约 7 天，过期取结果返回 404 `result_expired`。⚠️ 这意味着**结果在此期间留存于百炼®标书服务器**（第三方存储）；上传文件与历史数据以账户身份存于平台，用户可登录官网查看管理——向用户交代结果时请一并说明。

## 端点详情

### `GET /me` — 连通性与可用字数
```json
{"wallet_balance":1397084,
 "limits":{"rate_per_min":60,"max_concurrent_jobs":3,"running_jobs":0}}
```
`wallet_balance` 当前为兼容旧字段名，展示给用户时统一称为“可用字数”。

### `POST /interpretations` — 智能解读（唯一上传入口）
- 入参：multipart 字段 `file`（.pdf/.doc/.docx）。
- 返回：`{"job_id":"..."}`。
- 结果（`/jobs/{id}/result`）：`{"job_id","service":"interpretation","result":{...}}`。
  `result` 含句柄 `project_id`/`result_id`/`status` + **8 个内容维度 + 控标洞察**，
  完整字段见 [附录 A](#附录-a智能解读结果字段)。**记下 `result.project_id`**。

### `POST /bid-documents/{project_id}/packages` — 抽取分包
- 无 body。返回 `{"job_id":"..."}`。
- 结果：
```json
{"service":"bid_document",
 "result":{"packages":[...],"is_multi_package":true,"package_count":2,
           "suggested_pages":50,"max_total_pages":500}}
```
- 把 `packages` 给用户挑选，收集选中的 `package_ids`。
- `is_multi_package=false` 时可跳过选包，generate 不带 `package_ids`。

### `POST /bid-documents/{project_id}/generate` — 生成成品标书
- 入参 JSON：`{"package_ids":[11,12],"total_pages":80}`（非多包可省略 body 或传 `{}`）。
- 返回 `{"job_id":"..."}`。内部串行「选包 → 抽需求 → 大纲 → 逐条正文 → 制式模板填充 → 导出」，耗时长。
- 进度阶段加权：`select / requirements / outline / content / templates / export`。
- **结果是流式 .docx 二进制**（非 JSON），响应头 `Content-Disposition: attachment; filename="bid_<job_id>.docx"`。

### `POST /projects/{project_id}/compliance-reviews` — 标书审查
- 入参：multipart `bid_files`（一或多份 .pdf/.doc/.docx）+ 表单字段 `is_blind_bid` / `is_electronic_bid`。
- 限制：最多 100 份；单份 ≤ 1024 MB；总大小 ≤ 2GB。
- 可选字段：`is_blind_bid`（暗标）、`is_electronic_bid`（电子投标）、`sibling_unit_names`（敏感单位名称）、`semantic_review=false` 或 `enable_semantic_review=false`（关闭语义审查）。
- project 必须已完成解读，否则 409。返回 `{"job_id":"..."}`。
- 结果（`/jobs/{id}/result`）：`result.compliance` 含 `summary`/`issues`/`similarity_issues`/`manual_items` 等，
  完整字段见 [附录 B](#附录-b合规审查结果字段)。

### `POST /bid-duplicate/runs` — 标书查重

- 入参：multipart `bid_files`（2-3 份 .pdf/.doc/.docx）+ 可选 `tender_file`（1 份 .pdf/.doc/.docx）。后端另支持 URL 字段，但 ClawHub 线路不使用，也不做任何远程抓取。
- 限制：投标文件必须 2-3 份；投标文件单份 ≤ 1024 MB；可选招标文件 ≤ 50 MB；总大小 ≤ 2GB；不支持扫描型 PDF。
- 必填字段：`legal_possession_attested=true`，表示用户已确认合法持有并有权处理本次上传的全部文件。
- 可选字段：`enable_image`（图片相似，默认 true）、`enable_metadata`（文档元数据，默认 true）、`enable_semantic`（语义相似，默认 true）、`exclude_tender_baseline`（排除招标文件原文共同表述，默认 true）。
- 返回：`{"job_id":"..."}`。通过 `GET /jobs/{job_id}` 轮询，通过 `GET /jobs/{job_id}/result` 获取结果。
- 结果：`{"service":"bid_duplicate","result":{"run_id":123,"duplicate":{...}}}`；`duplicate` 按文件对展示文本相似、图片相似、元数据、主体线索、风险率、证据片段和修改建议；`scripts/report.py` 可将该结果渲染成本地 HTML/Word 查重报告。
- 责任边界：查重仅提供提交前内部自查线索，不构成围标、串标、违法违规或投标有效性的法律认定；不提供一键降重、同义改写或规避监管的建议。

### `GET /jobs/{job_id}` — 查任务状态（轮询用）
```json
{"job_id":"...","service":"interpretation|bid_document|compliance|bid_duplicate",
 "phase":null,"status":"running",
 "progress":{"percent":47,"stage":"content","stage_label":"生成内容",
   "message":"正在写正文 32/80 节","current_step":32,"total_steps":80,
   "current_step_label":"项目实施方案","unit_label":"节",
   "elapsed_seconds":360,"estimated_total_seconds":300,"estimated_remaining_seconds":0,
   "updated_at":"..."},
 "error":null,"created_at":"...","updated_at":"..."}
```
- `message/current_step/total_steps/current_step_label/unit_label` 为长任务细进度字段；不存在时按 `percent + stage_label` 展示。

### `GET /jobs/{job_id}/result` — 取结果
- 解读/合规/查重返回 JSON；标书制作返回 .docx 二进制流。

### `GET /jobs/{job_id}/download-url` — 获取成品标书短时下载链接
- 仅标书制作任务成功后可用；需 `X-App-Key`，按 Api Key 所属用户隔离。
- 返回：`{"filename","download_url","expires_in","size_bytes"}`。
- `download_url` 是给用户打开的短时链接，形如 `/api/open/v1/jobs/{job_id}/download?token=...`，**不包含 Api Key**。
- 用户点击短时链接时，平台校验 token 绑定的 `job_id/user_id/export_id` 与过期时间；若成品已上传对象存储则 302 跳转 CDN/COS 签名地址，否则使用旧的服务端流式下载兜底。

### `POST /jobs/{job_id}/cancel` — 取消
- 尽力而为；已过的扣费点不退款。

### `GET /knowledge-base` — 开放知识库分类总览

- 返回开放给 skill 的资料库分类与数据量。
- **明确排除**：历史标书库、标书模板库。

### `GET /knowledge-base/{category}` — 按类别查询知识库

- `category` 当前支持：
  - `company_profile`
  - `qualifications`
  - `performances`
  - `financial_reports`
- 返回按类别分组的结构化 JSON。
- 分页类默认 `page=1`、`page_size=50`，最大也只允许 `50`。
- 只返回白名单字段：
  - `company_profile`：公司名称、企业类型、营业期限、统一社会信用编码、注册地址、办公地址、法人名称、职务、法人联系方式
  - `qualifications`：资质名称、证书编号、有效期限
  - `performances`：合同名称、客户名称、合同金额、完成时间
  - `financial_reports`：当前仅开放分类入口，不开放具体字段
- **不返回任何附件信息**：包括但不限于访问地址、文件流、base64、附件存在标记。
- 字段说明与回填边界由 skill 侧 [knowledge-fields.md](knowledge-fields.md) 补充约束。

### 402 insufficient_balance 错误体新增字段

`phone_bound`（bool）；另有 `bind_url` / `recharge_url`（**均携带明文 `bind_key=<app_key>`**）。
🔒 **本 skill 不使用也不转发这些带 Key 的链接**（防凭证经会话记录/截图/链接预览泄露）——可用字数不足一律引导用户自行登录官网购买会员或字数包（不含参数的普通链接）。

### 提交门槛 vs 实际消耗（提交时 402）

可用字数不足时，`POST /interpretations`、`POST /bid-documents/{pid}/generate`、
`POST /projects/{pid}/compliance-reviews`、`POST /bid-duplicate/runs` 四个提交入口都会在**提交时**直接返回 402
`insufficient_balance`（错误体含上述引导字段）；购买会员或字数包后方可操作。

这和“是否实际消耗可用字数”是两件事：
- **提交门槛**：解读 / 生成 / 标书审查 / 标书查重四个入口都要求账户有可用字数才能提交。
- **实际消耗**：仍只有生成会真实消耗可用字数；解读、抽包、标书审查、标书查重本身不消耗字数。
- **不受门槛限制**：抽包（packages）、`GET /me`、任务查询、结果获取等查询类接口不受该门槛限制。

skill 侧提交前也会先调 `GET /me` 做预检，优先把这层差异解释给用户，避免把“可用字数不足拦截”误说成“这一步会消耗字数”。

## 错误码速查

| HTTP | code | 含义与处理 |
|---|---|---|
| 401 | `missing_credentials` / `invalid_credentials` | 缺 `X-App-Key` Header / Api Key 不对 → 检查凭证或重置 Key |
| 403 | `account_disabled` | 凭证或用户被停用 |
| 402 | `insufficient_balance` / `insufficient_points` | 可用字数不足，不扣费不产出 → 购买会员或字数包 |
| 404 | `not_found` | 多为开放 API 总开关未开（整层 404）→ 联系管理员开启 |
| 404 | `job_not_found` / `project_not_found` / `result_expired` | 句柄不存在/非本人/结果过期（7 天 TTL） |
| 409 | `invalid_job_state` / `report_task_conflict` | 任务未成功就取结果 / 未解读就生成 / 未抽包就 generate / 已有标书审查或查重任务运行中 |
| 422 | `validation_error` | 文件缺失/类型不支持 / 缺 package_ids / 查重未确认合法持有 |
| 413 | `bid_file_too_large` / `tender_file_too_large` / `batch_too_large` | 查重或审查上传文件超出单份/总量限制 |
| 429 | `rate_limited` / `too_many_concurrent_jobs` | 触发限流 → 退避重试（看 `Retry-After`）或减并发 |
| 500 | `internal_error` | 服务端异常 → 重试或反馈 |

任务级失败时 `GET /jobs/{id}` 的 `error.code`：`interpretation_failed` / `generation_failed` / `compliance_failed` / `bid_duplicate_failed` / `insufficient_balance` / `insufficient_points` / `canceled` / `worker_lost`（服务重启导致，需重新提交）。

## 注意事项

- **标书制作/审查的招标文件入口**：招标文件经 `/interpretations` 上传并产出 `project_id`；制作与合规都复用它，**不要重复上传同一招标文件**。标书查重可独立上传 2-3 份投标文件，并可选上传招标文件作为公共表述基线。
- **幂等**：网络重试带相同 `Idempotency-Key`（UUID），避免重复建任务/重复扣费。
- **计费**：标书生成消耗 Api Key 所属用户可用字数，与网页同口径；解读、抽包、标书审查、标书查重不消耗字数，但除抽包/查询外，提交前都要求有可用字数。生成前用 `GET /me` 看 `wallet_balance`（兼容字段，按可用字数理解）预判。
- **内容质量依赖知识库**：正文质量取决于 owner 租户的公司资料库；资料缺失会致内容退化（不硬失败）。
- **知识库查询接口**：skill 可独立查询企业信息 / 资质 / 业绩 / 财务报告，再由本地模型做待填项匹配与回填；历史标书库、标书模板库不在本接口开放范围内。
- **知识库安全边界**：只能按 Api Key 所属租户取数，不接受外部 `tenant_id` / `user_id`；接口有单独限流与访问审计日志。
- **来源标记**：经开放 API 产生的数据标记为 **skill** 来源（网页端为「平台」），便于在网页历史/消费流水里区分。

> 字段口径与根目录《百炼®标书Skill服务.md》附录 A/B 一致；`scripts/report.py` 据此渲染报告。

---

## 附录 A：智能解读结果字段

`GET /jobs/{id}/result` 的 `result`（`service=interpretation`）：

```json
{
  "project_id": "123", "result_id": 7, "status": "completed",
  "project_info": [...], "compliance": [...], "disqualification": [...],
  "evaluation": [...], "key_requirements": [...], "business_terms": [...],
  "pricing": [...], "procurement_analysis": {...}, "decision_analysis": {...}
}
```

- **project_info[]** 项目基本信息：`field_name` / `field_value` / `source_page` / `source_text`。
- **compliance[]** 合标项（参与资格）：`category` / `requirement_text` / `source_page` / `source_text` / `is_structured`。
- **disqualification[]** 废标项（红线）：在 compliance 字段基础上多 `type`（资格废标/响应性废标/合规废标）。
- **evaluation[]** 评审项：`component` / `item` / `factor` / `score`(满分) / `weight` / `source_page` / `source_text` / `is_structured`。
- **key_requirements[]** 关键要求：`category` / `requirement_text` / `source_page` / `source_text`。
- **business_terms[]** 商务条款：`term_type` / `term_content` / `source_page` / `source_text`。
- **pricing[]** 报价要求：`component` / `requirement_text` / `source_page` / `source_text`。
- **procurement_analysis{}** 采购背景：`analysis_summary` / `procurement_background` / `procurement_objectives` / `procurement_scope_items[]` / `key_constraints[]` / `key_success_metrics[]`(每条 `{name,detail}`，关键成功指标)（缺失字段可为 null/空）。
- **decision_analysis{}** 控标洞察：
  - 顶层：`participation_recommendation`（建议/谨慎/不建议参与）、`control_risk_level`（高/中/低）、`confidence_level`、`summary[]`、`signals[]`、`evidence_items[]`、`actions[]`、`advantaged_supplier_profile[]`、`our_gap_assessment[]`。
  - `signals[]`：`id` / `dimension`（qualification_barrier/technical_targeting/business_barrier/scoring_bias/acceptance_and_performance_risk/pricing_competitiveness_constraint）/ `title` / `risk_level` / `description` / `reasoning` / `evidence_item_ids[]` / `our_stance`（advantage/risk/neutral/unknown）/ `our_stance_reason`。
  - `evidence_items[]`：`id` / `source_category` / `source_page` / `source_text_excerpt` / `why_it_matters`。
  - `actions[]`：`priority`（high/medium/low）/ `action_type` / `recommendation` / `related_signal_ids[]`。

---

## 附录 B：合规审查结果字段

`GET /jobs/{id}/result` 的 `result.compliance`（`service=compliance`）：

```json
{
  "run_id": 42, "status": "completed", "mode": "standalone",
  "document_id": 123, "interpretation_result_id": 7,
  "summary": {...}, "partial_summary": {...}, "bid_files": [...],
  "issues": [...], "similarity_issues": [...], "manual_items": [...],
  "scope_summary_lines": [...], "error_message": null
}
```

- **summary{}** 汇总：`high_count` / `review_count` / `tip_count` / `similarity_count` / `manual_unchecked_count` / `conclusion`(一句话结论) / `conclusion_phase`(full/rules_only/semantic_partial) / `overview_ready` / `semantic_review.state` / `semantic_review.message_zh`。`semantic_review` 用于提示语义审查是否完整完成；不是 full/complete 时，对用户不得表述为完整审查。
- **partial_summary{}** 阶段性/部分结果摘要：字段可能随引擎变化，常见为阶段性风险计数、阶段状态、说明文案。存在该字段时，HTML 报告总览区应展示，作为“当前结果完整性”的补充。
- **bid_files[]** 被查文件：`id` / `filename` / `content_hash` / `metadata` / `created_at`。
- **issues[]** 合规问题（核心）：`id` / `bid_file_id` / `bid_filename` / `issue_type`(如 `hard_field_presence` 等) / `risk_level` / `result_type` / `title` / `description` / `tender_evidence` / `bid_evidence` / `suggestion` / `confidence`(0-1) / `status` / `user_note`。
  > ⚠️ **实测枚举值**：`risk_level` = **`high`/`review`/`tip`**；`result_type` = **`suspected`/`detected`**。`summary.high_count/review_count/tip_count` 按 `risk_level` 计数。
  > 证据多形态（因引擎而异）：语义类 `tender_evidence/bid_evidence` 主键 **`excerpt`**（另含 `chunk_id`/`section_path`/`section_title`）；硬字段类 `{field,expected_text}`；规则未命中 `{source}`。`report.py` 的 `_ev` 已按 `excerpt > text > field/expected_text > source` 兼容。
- **similarity_issues[]** 多文件雷同（仅多份投标文件时有）：`file_a_id`/`file_b_id` / `file_a_name`/`file_b_name` / `similarity_type`(text_overlap/structure_overlap) / `risk_level` / `title` / `evidence_a{text,page}`/`evidence_b{...}` / `similarity_score`(0-1) / `suggestion` / `status`。
- **manual_items[]** 人工核查清单：`category` / `title`(简短标题) / `description` / `source` / `is_checked` / `note`(备注) / `checked_by` / `checked_at`。
- **scope_summary_lines[]** 检查范围摘要（适合报告开头展示）。

报告推荐布局：总览（风险摘要、检查范围、语义审查状态、部分结果摘要） → 高风险问题(issues 高) → 待人工复核(result_type=semantic) → 格式提示(低) → 多文件相似度 → 人工核查清单。`scripts/report.py` 已实现此布局。
