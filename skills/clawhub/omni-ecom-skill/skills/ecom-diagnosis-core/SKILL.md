---
name: ecom-diagnosis-core
description: 电商经营诊断与数据质量闸门。处理天猫、京东、拼多多、抖音、视频号、小红书等平台的 CSV/XLS/XLSX 报表，或分析 GMV、流量、转化、退款、投放 ROI、利润与商品结构时使用；先核对数据口径并确定性复算，再做归因、策略与报告。严禁用缺失成本推断利润，严禁加总未去重访客。
---

# 电商经营诊断核心

先把原始报表变成可复算、可追溯的指标包，再允许专家解释。不要让模型凭展示值心算关键指标。每次任务先锁定客户范围和 `run_id`，避免跨客户读取记忆或底稿。

## 强制流程

1. **建立运行范围与资料清单**：先生成 `client_scope`、`run_id` 和允许读取根目录；再逐个记录文件名、平台、报表类型、sheet、日期范围、行数、关键字段、导出时间和重复文件。未知项写“待确认”。读取前可用 `scripts/context_guard.py` 做路径门禁。
2. **锁定口径**：读取 [指标契约](references/metric-contract.md)。明确 GMV / 支付金额 / 净销售额、人数 / 次数、自然 / 付费、店铺 / SPU 等口径；未锁定前不得跨表加总。
3. **原始报表适配与确定性复算**：对 CSV / JSON / XLSX / 可读 XLS 先运行 `scripts/normalize_reports.py`，让它输出字段映射、来源哈希和规范 `rows`；多工作表必须显式 `--sheet` 或 `--all-sheets`。再运行 `scripts/metric_gate.py`。禁止用旧报告或人工摘录代替原始文件复算。
4. **执行数据质量闸门**：读取 [数据质量闸门](references/data-quality-gate.md)。结果只能是 `PASS`、`WARN`、`BLOCKED`：
   - `PASS`：可进入经营归因。
   - `WARN`：可分析，但每个受影响结论必须带限制说明。
   - `BLOCKED`：只交付数据问题、可确认事实和补数清单；不得输出利润、预算或增长承诺。
5. **异常情景复算**：小体量店铺、转化突变、客单突变或订单结构异常时，至少对比 N0 原始、N1 剔低价污染单、N2 再剔非自然大单。阈值与限制见数据质量闸门；阈值只用于筛查，不自动等同作弊或无效订单。
6. **归因与方案**：读取 [证据与决策输出](references/evidence-and-decision.md)。每项结论标注【事实】【判断】【假设】【建议】、证据 ID、置信度和反证条件。相关性不足以单独证明因果。
7. **交接统一材料**：按包内 `schemas/handoff.schema.json` 回传 `run_id`、`agent_version`、`metrics_bundle`、`evidence_ledger`、`gate_status`、冲突项、缺失项和可执行动作；先运行 `scripts/validate_handoff.py`，不要只回传叙述性摘要。
8. **行动闭环**：每个外部动作都建立 `scripts/action_tracker.py` 行动记录，写清负责人、基线、验收指标、停止条件和审批要求。必须经历提议/审批后才可执行；执行后用 `outcome` 写回实际结果，未达标进入 `rolled_back`，不可判定进入 `blocked`。
9. **先选任务类型再构建报告**：从插件根目录 `config/task-profiles.json` 选择 `store_diagnosis / weekly_report / monthly_report / quarterly_report / annual_report / campaign_review / data_quality_audit / single_topic`，并把 `--task-type` 传给 `scripts/build_report_package.py`。在构建前必须建立 `claim-ledger.json`，运行 `scripts/claim_guard.py validate`；构建器强制接收 `--claim-ledger`，并生成 `claim-receipt.json`。通过后才会生成 `report.json`、`report.md`、至少 3 张图表的 `report.pdf` 和 `pdf-delivery.json`。PPT/Excel 只消费报告包；不得把周报结构硬套月报、年报或新店诊断。`BLOCKED` 只能生成数据质量 PDF，不能由排版把草稿包装成确定性经营结论。
10. **PDF 默认且不可绕过**：周报、月报、年报、店铺诊断和经营复盘无需用户另行要求 PDF。`pdf-delivery.json.status` 不是 `pdf_render_verified` 时停止；不得手工交付“结论等价”的 Markdown。
11. **版本可见**：报告必须读取插件根目录 `version-info.json`，标注 `team_version`、发布日期、上一版本和版本差异；版本元数据与 `.codebuddy-plugin/plugin.json` 不一致时直接失败。
12. **协作可审计且不可提前完成**：综合任务第一可执行动作必须取得真实团队。若 `TeamCreate` 未直接显示，先精确调用 `ToolSearch({"tool_names":["TeamCreate"]})`，再用 `DeferExecuteTool` 执行；取得有效 `team_name` 前禁止读取业务数据、创建任务或调用 Agent。综合任务随后创建阶段任务，并在首批一次创建 `data-analyst / platform-ops / content-live-growth / ad-profit-optimizer` 四位分析专家；为每次调用生成唯一 `attempt_id`，运行 `scripts/wait_for_agent_returns.py --return-file <agent_id>=<attempt_id>.return.json` 在同一主回合等待四位回传。四位齐备后由团长裁决并生成冻结的 R1 报告候选稿，运行 `scripts/review_guard.py prepare` 固化候选稿、裁决和来源 sealed handoff 的 SHA256，再创建 `delivery-review-r1` 复核这些确切文件。TeamCreate 失败或 Agent 返回 `No active team found` 时立即返回 `collaboration_unavailable`；宿主 90 秒内没有成功 `team_name` 时返回 `collaboration_unavailable_timeout`。等待超时返回 `collaboration_wait_timeout`，缺回传凭证返回 `collaboration_unreturned`。用户要求续跑时，先运行 `scripts/collaboration_resume_guard.py`，只允许在同一 run_id、版本和 team-bootstrap 凭证通过时继续。
13. **复核必须绑定 attempt 与最终产物**：韦交达一次性写本次 `review_attempt_id` 专属结果；团长只能运行 `scripts/review_guard.py attest-result --review-attempt-id <本次ID>`，把该结果绑定 WorkBuddy 返回的真实 `agent_task_id`。发布前必须运行 `review_guard.py verify`；复核后报告、裁决或任一来源 handoff 变化时返回 `review_stale_blocked`，修订号升为 R2 并创建新的 `delivery-review-r2` 子任务。`conditional_pass` 不等于通过。报告修订号使用 R1/R2，不与专家团语义版本混用。
14. **公域客户隔离与最终完成闸门**：历史记忆、案例和模板只允许复用匿名结构。报告文件与最终回复展示前必须运行 `scripts/public_output_guard.py --output public-output-receipt.json`，只把当前 `client_scope` 的客户名称作为 `--allowed-term`；命中其他已登记客户名称时返回 `client_scope_leak_blocked`。随后运行 `scripts/completion_gate.py`，必须传入 `claim-receipt.json`；综合任务还必须传入 manifest、attestation、release receipt 和公域隔离凭证。只有数字来源回执通过且 `formal_delivery_complete` 才能展示正式文件或声称主任务完成。

## 硬性口径

- 转化率分母只使用与成交口径匹配的去重访客。SPU 访客通常不可跨商品加总成人数，只能用于结构占比或需求强度信号。
- GMV、净支付、净销售额和回款不是同一个指标；报告首处出现时必须声明定义。
- ROAS 是销售额 / 广告费，不等于利润 ROI。缺毛利、退款、佣金、履约、货损或税费时，只能输出“利润数据不足”。
- 转化率只能是支付买家数（或订单数）/匹配口径访客数；GMV/访客只能叫访客价值。ROAS/ROI 必须使用同一来源、期间和归因范围的归因 GMV/推广花费；跨来源拼接一律阻断。
- 可承受 CPC 必须使用可购买渠道（如搜索）的 GMV、访客和成交口径；不得用全店 UV 价值替代。
- 跨平台种草与成交只能在有明确归因窗口、规则和证据时量化，否则标为假设。
- 平台规则和行业基准需带来源与日期；无法实时核验时明确标注可能过期。

## 工具用法

原始报表适配：

```powershell
python scripts/normalize_reports.py raw_report.xlsx --platform jd --sheet 月主表 --output normalized.json
```

规范 CSV / JSON 每行代表一个期间，至少包含：`period,gmv,visitors,buyers,orders`。比例字段使用 0 到 1 的小数。

```powershell
python scripts/metric_gate.py normalized_metrics.csv --output metrics_bundle.json
python scripts/metric_gate.py --self-test
python scripts/validate_handoff.py handoff.json
python scripts/action_tracker.py list --root runs/<run_id> --status pending_approval
python scripts/claim_guard.py validate --claims claim-ledger.json --output outputs/claim-receipt.json
python scripts/build_report_package.py --handoff handoff.json --client-scope client-demo --task-type weekly_report --claim-ledger claim-ledger.json --output-dir outputs/report
python scripts/connector_smoke.py
```

脚本只计算字段支持的指标，不为缺失成本填默认值。若平台字段尚未映射，先完成字段对照，不要把原始导出直接硬塞给脚本。

## 交付最小集合

- 资料与口径清单
- 数据质量闸门结果
- 可复算指标表
- 证据账本与冲突裁决
- 经营结论、限制和优先级
- 负责人 / 截止时间 / 验收指标 / 停止条件
- 行动 ID、审批记录、执行状态和结果回写
- 报告包（JSON + Markdown + 图表化 PDF + PDF 渲染凭证）及来源索引
- 公域隔离凭证、交付复核回执与 `completion-receipt.json`
- 专家团版本、发布日期和相对上一版本的变更说明
- 待确认事项与待补数据

## 上下文与运行账本

- 客户隔离规则见 [context-isolation.md](references/context-isolation.md)。
- 运行账本使用 `scripts/run_record.py` 创建；输入、证据、审批、产物和事件均按 `run_id` 分目录保存。
- 对外交付只保留证据 ID 和文件指纹，隐藏客户名、本机绝对路径和内部记忆内容。
- 报告包契约与状态规则见 [report-package-contract.md](references/report-package-contract.md)。
