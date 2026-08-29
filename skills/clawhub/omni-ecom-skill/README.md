# omni-ecom 全域电商经营专家团

一个由经营总监统筹、五位领域专家协作的 WorkBuddy Team 型专家。先核对真实报表和指标口径，再输出经营诊断、增长动作、投流利润方案与可审阅报告。

## 版本

当前版本：`1.5.11`

本版新增：

- v1.5.11 在 v1.5.10 基础上增加数字来源、公式和归因硬闸门；没有 `claim_guard_passed` 不得进入正式交付。
- v1.5.10 在 v1.5.9 基础上增加团队启动超时边界和中断后安全续跑能力。
- 新增 `team_bootstrap_guard.py`：只接受真实 TeamCreate 返回的 `team_name`，并把宿主模式写入本次运行凭证。
- 新增 `collaboration_resume_guard.py`：按同一 run_id 判断成员回传、sealed handoff、报告、复核和完成凭证处于哪一阶段。
- 新增 `resume_smoke.py`：验证建团缺失、成员未齐、报告待生成、复核待完成和正式完成五种状态。
- TeamCreate 超过 90 秒没有成功 team_name 时返回 `collaboration_unavailable_timeout`，不会无限等待或重复建团。
- 用户说“继续”时，先检查原运行凭证；无法确认原团队身份就创建新的 run_id，不跨运行搬运文件。
- v1.5.9 修复 v1.5.8 完整协作冒烟测试中复核等待、attempt 绑定和正式完成状态未闭环的问题。
- 新增 `claim_guard.py` 与 `claim-ledger.schema.json`：每个数字必须回到来源文件、字段、期间和 SHA256；转化率、访客价值、ROAS/ROI、净 ROAS 公式和归因范围分开校验。
- `build_report_package.py` 强制接收 `--claim-ledger`，生成 `claim-receipt.json`；`completion_gate.py` 必须核验回执与冻结报告哈希。
- 新增 `completion_gate.py`：成员回传、数字来源、PDF验真、韦交达独立复核、公域隔离必须全部通过，才生成 `completion-receipt.json.status=formal_delivery_complete`。
- 新增八类任务配置：店铺诊断、周报、月报、季报、年报、大促复盘、数据质量审计和单项经营专题；报告包显式记录 `task_type/task_profile`。
- 最终完成凭证合并六岗位真实贡献与 Agent 子任务 ID；韦交达在候选报告中标为 `pending_review`，复核通过后在完成凭证中更新为 `contributed`。
- 公域隔离检查新增带文件哈希的 `public-output-receipt.json`，旧的扫描结果不能替代当前产物。
- v1.5.8 将可变 `*.return.json` 回执与不可变 `handoff-*.json` 业务交接彻底分离；报告构建和冻结复核只能使用 handoff。
- v1.5.8 R2 热修进一步按 `attempt_id` 隔离 raw handoff/return，并用 `seal_handoff.py` 绑定真实 Agent 子任务号；迟到或重试 Agent 不再能够覆盖已选中的交接件。
- 团长被禁止代写成员 raw handoff/return 或先写模板让成员只校验；成员不能亲自落盘时必须 fail closed。
- PDF 会把结构化待补数据转换为可读文本，并逐岗展示贡献摘要；交付复核岗在候选稿中明确指向最终放行凭证，避免产生“未复核”的误解。
- `review_guard prepare` 主动拒绝活动 return 文件并返回 `mutable_return_source_blocked`，避免成员结束阶段补写回执导致复核哈希失效。
- 冻结后任何 handoff、裁决或报告变化都必须升报告修订号并创建新的韦交达任务，禁止手写被 guard 拒绝的签收件。
- 韦交达采用一次性复核结果协议，不暂停等待创建后才出现的 task ID；团长只能用 `attest-result` 将原始复核结论绑定 WorkBuddy 的真实子任务 ID。
- 原始 CSV / JSON / XLSX / 可读 XLS 报表适配与字段映射
- `client_scope` / `run_id` 客户隔离和运行账本
- 结构化交接 Schema 与交接校验
- 12 个脱敏行为属性评测用例
- 数据质量闸门：`PASS / WARN / BLOCKED`
- 统一指标契约与证据账本
- N0 / N1 / N2 异常订单情景复算
- ROAS、净 ROAS 与利润 ROI 分离
- 搜索渠道可承受 CPC 测算
- 带验收指标和停止条件的行动清单
- 行动台账：提议 → 审批 → 执行 → 验证 / 回滚 / 阻断，并保留事件记录
- 结构化报告包：JSON + Markdown + 默认图表化 PDF + PDF 渲染凭证，证据、来源指纹、缺失数据和审批状态可追溯
- `BLOCKED` 自动收敛为数据质量报告，不把草稿包装成经营结论
- Connector 基础契约：能力声明、调用记录、对象 ID 映射、凭证引用和 mock dry-run
- 所有新报告自动显示专家团版本、发布日期、上一版本和版本差异
- 综合任务按 v1.0 成功模式强制执行 `TeamCreate → TaskCreate → 四位分析专家并行调度 → 四位真实回传 → 团长裁决 → delivery-review 独立复核`
- `TeamCreate` 缺失或失败时 fail closed，不允许团长以内联分段或岗位署名模拟专家协作。
- 每个成员必须保留 WorkBuddy 返回的 `agent_task_id`；最终报告直接列出各 Agent 子任务 ID，便于逐个打开核查。
- `delivery-review` 在四位分析专家完成并由团长裁决后才携完整材料创建；不再依赖无法保证的待命 Agent 二次唤醒。
- 最终交付前不执行 `TeamDelete`，确保子任务工作轨迹仍可查看。
- 综合模式六岗位必须全部具有独立 handoff；缺数据的岗位也必须参与并回传“数据不足”，不能从过程和报告中消失
- 报告列出六个岗位及其 `contributed / not_invoked` 状态、Agent 子任务 ID、贡献摘要和交接 SHA256
- 综合报告缺少必要成员交接时直接阻断，不能由总监模拟其他岗位
- `scripts/wait_for_agent_returns.py` 支持按 `attempt_id` 指定回传文件，并为韦交达使用独立 `delivery_review` 契约；主任务在四位分析专家与交付专家真实回传前保持同一执行回合。
- 综合报告要求每位成员携带 `agent_return_status / agent_returned_at / agent_return_file / agent_return_sha256`，缺任一回传凭证即 `collaboration_unreturned`。
- 综合任务第一可执行动作必须是 `TeamCreate`；若工具被延迟提供，必须先执行 `ToolSearch({"tool_names":["TeamCreate"]})`，再通过 `DeferExecuteTool` 建团。
- 未取得活动 `team_name`、或 Agent 返回 `No active team found` 时，在读取业务数据前返回 `collaboration_unavailable`，不允许团长单人替代。
- 新增 `scripts/public_output_guard.py`：所有公域报告和最终回复只允许出现当前 `client_scope` 授权的客户名称，跨客户命中即 `client_scope_leak_blocked`。
- 真实客户隔离名单移至本机私有目录 `~/.workbuddy/private/omni-ecom/client-brand-registry.json`；发布包只带匿名示例名单，也可用 `OMNI_ECOM_CLIENT_REGISTRY` 指向指定名单。
- 历史记忆和版式模板只复用匿名结构，不复用历史客户名称、数据和结论。
- 最终报告先冻结为 `R1/R2...` 候选稿，再由韦交达复核清单中列出的确切文件；不再先复核材料后生成报告。
- `scripts/review_guard.py` 使用 `prepare → attest-result → verify`；自由填写复核状态的 `attest` 已禁用，复核必须绑定 `review_attempt_id`、报告修订号和真实 Agent task ID。
- 复核后任一文件发生变化即 `review_stale_blocked`；必须升级报告修订号并新建韦交达子任务。
- `conditional_pass` 不等于通过；`review_release_verified` 后仍需公域隔离和最终完成闸门。
- 正式交付包含 `release-receipt.json`、`public-output-receipt.json` 和 `completion-receipt.json`，记录最新复核任务、六岗位贡献和产物哈希。

## 团队

- 沐风：任务拆解、数据裁决、交叉验证与最终报告
- 沈数清：数据质量、指标复算与经营归因
- 梁运通：天猫、京东、拼多多货架运营
- 洪涨声：抖音、视频号、小红书内容与直播
- 罗效盈：投流、单位经济与利润情景
- 韦交达：周报、月报、PPT、数据表与定版 PDF

## 推荐用法

1. 先指定客户范围和本次决策，不跨客户读取历史底稿。
2. 上传原始导出文件，不只上传截图或旧报告。
3. 说明平台、店铺、统计期间、任务类型和要支持的决策。
4. 先完成来源适配、资料清单、口径映射和数据质量闸门。
5. 闸门通过后，再进入领域分析、冲突裁决和报告交付。
6. 店铺诊断、周报、月报、季报、年报和大促复盘必须选择综合协作模式，并把各成员 sealed handoff 传给报告构建器。

示例：

- 审核这批天猫或京东原始报表的口径和数据质量，列出阻断项、可用指标与待补数据。
- 基于搜索渠道数据和完整成本，测算净 ROAS、可承受 CPC，并给出保守与进取方案。
- 基于通过数据闸门的本周数据，生成经营周报和带验收标准的行动清单。

## 能力模块

- `ecom-diagnosis-core`：资料体检、指标契约、确定性复算、数据质量闸门、证据与决策输出。
- `schemas/`：交接、运行记录和客户范围的机器可校验协议。
- `scripts/action_tracker.py`：创建行动、审批、状态流转和结果回写。
- `scripts/build_report_package.py`：从通过校验的 handoff 生成下游统一报告包。
- `config/task-profiles.json`：统一八类经营任务的时间粒度、比较窗口、决策重点和默认协作模式。
- `scripts/task_profile_smoke.py`：校验八类任务是否齐全、综合/单点协作默认值和报告交付要求是否一致。
- `scripts/generate_pdf_report.py`：从 `report.json` 默认生成至少 3 张图表的 A4 PDF，并输出逐页渲染验收凭证。
- `scripts/collaboration_smoke.py`：验证综合任务不能退化为总监单人报告。
- `scripts/wait_for_agent_returns.py`：阻塞等待指定 Agent 的同一 run_id 完成凭证，超时 fail closed。
- `scripts/team_bootstrap_guard.py`：记录并核验真实 TeamCreate 结果，避免续跑时猜测团队身份。
- `scripts/collaboration_resume_guard.py`：只读判断中断运行可否安全续跑以及下一阶段。
- `scripts/resume_smoke.py`：验证五种续跑状态。
- `scripts/public_output_guard.py`：展示前执行客户名称隔离扫描，命中非当前客户名称时阻断且不回显该名称。
- `scripts/review_guard.py`：准备不可变复核清单、生成韦交达复核凭证，并在发布前检查复核是否过期。
- `scripts/claim_guard.py`：校验数字来源、公式、输入 claim 和归因范围，输出 `claim-receipt.json`。
- `scripts/claim_guard_smoke.py`：回归测试“GMV/访客误写转化率”“概览花费与流量 GMV 拼接 ROI”“未知数字硬编码”等失败场景。
- `scripts/completion_gate.py`：综合验证报告、PDF、数字来源回执、六岗位、复核回执和公域隔离凭证，只在全部通过后签发正式完成凭证。
- `connectors/`：端口与适配器契约，以及仅用于测试的 `mock-platform`。
- `version-info.json`：专家团版本和发布变更的唯一来源。
- `evals/`：脱敏行为属性用例和内置夹具；使用 `scripts/run_evals.py` 批量评测。
- `ecom-report-pdf-layout`：A4 电商经营报告的排版、图表与生成后验证。

## 安装与更新

将完整 `omni-ecom` 目录放入 WorkBuddy 的个人专家插件目录，再通过 WorkBuddy 专家管理能力执行校验和注册。更新后请新建或重载会话，使新角色定义生效。

## 发布前自检

- `plugin.json` 可解析，团队成员与 Agent 文件一致。
- 两个技能目录均包含合法 `SKILL.md`。
- 诊断脚本 `metric_gate.py --self-test` 通过。
- 原始适配脚本 `normalize_reports.py --self-test` 通过。
- 交接校验 `validate_handoff.py` 和行为评测 `scripts/run_evals.py` 通过。
- 多 Agent 协作冒烟测试全部通过：综合报告具备团长、数据、平台、内容直播、投流利润的 sealed handoff，韦交达按独立 attempt 复核，最终完成凭证汇总六岗位。
- 行动审批与报告包验收通过：审批前不能执行，执行后必须有结果回写。
- Connector 冒烟测试通过：权限阻断、dry-run、幂等、对象定位和回读验证。
- 包级检查脚本 `scripts/validate_package.py` 通过。
- 头像为 PNG/JPG、512×512、单张不超过 500KB。
- 包内无客户名称、店铺 ID、密钥或本机私有数据路径。
- `claim_guard.py` 在缺来源、错误公式、跨来源/跨归因 ROI、未知数字和报告哈希变化时正确阻断。
- `completion_gate.py` 在缺数字回执、缺复核、公域隔离过期或任一产物哈希变化时正确阻断。
- 压缩包顶层结构为 `omni-ecom/...`。

WorkBuddy 重载后，可运行 `scripts/verify_workbuddy_load.py` 做配置握手；空输出、超时或 CLI 异常均标记为 `INCONCLUSIVE`，不得当作加载通过。中断后先运行 `scripts/collaboration_resume_guard.py`，不要直接把旧目录当成新任务。
