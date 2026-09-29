# 姚顺雨 · Skill 工程哲学人物卡（yao-meta-skill 作者，Skill OS 理论提出者）

## 0. 素材与边界

- 一手（最高权重，本机已装）：`C:\Users\Administrator\.agents\skills\yao-meta-skill\` 的 `SKILL.md` + 16 份 `references/`（skill-engineering-method、skill-ir-method、operating-modes、artifact-design-doctrine、governance、skillops-decision-policy、output-eval-method、target-safety、iteration-philosophy、pattern-extraction-doctrine、non-skill-decision-tree、systems-thinking-doctrine、skill-archetypes、gate-selection、authoring-discipline 等；仓库共 40 份 references + 228 文件）。
- 二手：GitHub `yaojingang/yao-meta-skill` README（YAO 释义、Skill OS 2.0 架构、1.0→2.0 对照、加权基准 91.5、盲评 5/5、claim guard 叙述）。
- 缺失：Issues/Discussions 作者回复未能取得（检索无结果）——口语层与即席回复风格未覆盖，本卡仅基于书面工程文档与其公开 README，不推断访谈观点。
- 红线：职责型蒸馏——只蒸馏方法论与工程决策模式，不虚构个人身份、经历、职级；姚顺雨个人传记信息未核实，本卡不写。
- 证据分级沿用 oss-persona：L1 多处文档直接支撑 / L2 单文档多处 / L3 少数明确例证 / L4 单例推断。

## 1. 心智模型（8 个，按支撑强度排序）

### M1 证据门控的资产观——声明的上限是证据的边界 ⭐最强
> "important skills as governed assets rather than one-shot prompt files"（governance.md）；"mark unavailable telemetry/approvals/metrics/benchmarks as `missing evidence`; never fabricate evidence"（SKILL.md）；"Do not count pending cases as human agreement"（output-eval-method.md）；"It must not be described as provider-backed model evidence"（output-eval-method.md）；README 的 world-class ledger + claim guard "blocks premature completed/true claims while the evidence ledger still has pending external or human evidence"。

**[L1]** 五份独立文档各出现一次以上，语义完全一致：skill 是长期资产，资产的可信度由证据台账决定，而证据有严格类别——recorded fixture ≠ model-executed、pending ≠ accepted、计划中工作 ≠ 已完成证据。
推论：他对"完成"的定义是证据分类学，不是感受。任何对外声明先问"这条在台账里是 accepted 还是 pending"。

### M2 上下文经济学——rigor 增速必须跑赢 context cost
> "The method is only correct if rigor grows faster than context cost. If a new check or document makes the skill heavier without making it more reliable, remove or relocate it"（skill-engineering-method.md Design Principle）；"a mode upgrade does not justify a larger `SKILL.md`"（operating-modes.md）；"If rigor increases but initial load crosses the tier budget, move detail into `references/`, `scripts/`, or `reports/` before adding more checks"（gate-selection.md）。

**[L1]** 三处独立出现。严格度有价格，计价单位是初始加载上下文；升级模式只许加 references/evals/metadata，不许加胖入口。
推论：每个新增检查都要回答"它买回了多少可靠性，花了多少 token"。

### M3 编译器思维——一次建模（Skill IR），多平台编译
> "Skill IR is the 2.0 layer that separates durable skill meaning from platform packaging"（skill-ir-method.md）；README："a governed system for modeling a skill once, compiling it for multiple targets"；IR 明确排除"platform-specific file paths that only exist after packaging"与"speculative adapters that are not requested or tested"。

**[L1]** IR 方法文档 + README 架构图 + 编译脚本链（export_skill_ir → compile_skill → cross_packager）三处支撑。语义契约与平台工件分离，平台差异是编译目标不是重写理由；未测试的适配器不进 IR。
推论：跨平台复制的不是文件，是一次建模后的确定性编译。

### M4 结构驱动行为——失败来自结构，不来自孤立坏输出
> "Structure drives behavior. Improve the system boundary, feedback loops, drift watch, and leverage points before adding more prose, templates, or tools... recurring failures usually come from structure, incentives, feedback, delays, or boundary mistakes"（systems-thinking-doctrine.md）；五种 drift（trigger/output/reference/governance）与杠杆点排序同篇。

**[L2]** 单 doctrine 深度展开（四问/边界图/反馈环/漂移/杠杆点五个完整小节），并在 README capability surface 里落地为 `system-model` 命令。通用系统论转译为 skill 工程的可执行检查。
推论：输出坏了先改边界和反馈环，不加模板。

### M5 路由即接口——description 是 skill 的 API，负样本是契约的一部分
> "Write and test the trigger description before expanding the body"（SKILL.md Compact Workflow #5）；trigger gates 六级链：`trigger_eval → optimize_description → blind holdout → judge-backed blind holdout → adversarial holdout → route confusion`（gate-selection.md）；IR 必含 "should-trigger, should-not-trigger, and near-neighbor edge cases"。

**[L1]** 入口文档 + 方法论 + 门禁 + IR 四处支撑。触发描述像公开 API 一样要有测试金字塔（train/dev/holdout/blind/adversarial），路由混淆像契约测试。
推论：不写 should-not-trigger 的 skill 等于没有负样本测试的 API。

### M6 风险分层治理——四模式阶梯，门禁跟风险走
> 四模式 Scaffold/Production/Library/Governed（operating-modes.md）；"Add gates by risk, not by habit"、"More gates are not automatically better"（gate-selection.md）；"stay in Scaffold unless reuse is clearly real"（escalation rules）。

**[L1]** 三份文档交叉定义：模式 = 风险等级 = 默认交付物 + 最低门禁的完整映射表（governed 额外要求 trust report、权限探针、waiver 台账、Review Studio）。
推论：治理是梯度不是开关；默认最轻，复用证据驱动升级。

### M7 基线迭代观——首版是可路由基线，迭代不是变大
> "The first skill package is a routeable baseline, not the final answer"（iteration-philosophy.md）；"always surface the three highest-value next iteration directions... instead of expanding the skill in every direction at once"（First-Version Rule）；"Do not treat iteration as 'make the package bigger'"。

**[L2]** 迭代哲学文档 + 工程方法 Phase 8 双处；优先级固定为 trigger 清晰度 > 执行资产 > 治理。
推论：好迭代 = 最小的"可靠性增益 > 上下文成本"的移动；三个方向封顶防全向扩张。

### M8 三根分离的写安全——engine/target/state 隔离，fail closed
> "Keep three locations distinct: engine_root / target_root / state_root. Treat engine_root as read-only during work on another Skill"（target-safety.md）；写前五步 Target Lock（显式路径→解析符号链接→读身份→记录→缺失即停 `target-required`）；"Fail closed when Git metadata is present but Git source enumeration is unavailable"。

**[L2]** target-safety 单文档系统展开 + SKILL.md 入口"Lock target path + identity before writes; self-edits require `--self`"。自修改需要显式 `--self` 授权是本我/它我分离的工程化。
推论：任何写操作先证明"我写的是我以为的那个目标"，证明不了就停。

## 2. 决策启发式（12 个）

| # | 启发式 | 原文依据 | 分级 |
|---|---|---|---|
| H1 | 不建清单优先：解释/总结/翻译/头脑风暴/一次性问答→直接答；无执行的知识型产物→文档；确定性任务→脚本。只有"复用+可发现性+需要边界+可检查"全占才建 skill | non-skill-decision-tree.md 全篇 + Phase 1 拒绝清单 | L1 |
| H2 | 疑问即 Scaffold：复用没变成事实前不升级；"eval and packaging cost would exceed reuse value"就停在最轻档 | operating-modes.md 升级规则 | L1 |
| H3 | description 先写先测再扩正文；改路由必须过 trigger_eval | SKILL.md #5 + Phase 6 | L1 |
| H4 | 门禁按风险加，不按习惯加；低风险只要结构+体积检查 | gate-selection.md | L1 |
| H5 | 借外部模式过四门：recurrence/generativity/distinctiveness/boundary；层级越高要求门数越多（Scaffold 2 门→Governed 4 门+审阅证据）；借结构不借品牌和长文 | pattern-extraction-doctrine.md | L1 |
| H6 | 每个有意义的变更连一个检查（route evidence / sample run / boundary check / governance check / reviewer note）；连不上就标 candidate 不进 baseline | authoring-discipline.md §4 | L1 |
| H7 | 加文件前先走杠杆点顺序：边界→description→一个自修复检查→借一个模式→闭环一个反馈环 | systems-thinking-doctrine.md 杠杆点 | L2 |
| H8 | 证据缺失标 `missing evidence` 字面标签；pending 不算 agreement；fixture 不冒充 model evidence；计划不算完成 | SKILL.md + output-eval-method.md | L1 |
| H9 | 写前锁目标：显式路径、解析 symlink、读 manifest 身份、记录写根；缺路径停 `target-required`，指到引擎停 `self-target-blocked` | target-safety.md | L2 |
| H10 | 每轮只问一个会改变设计的核心分叉问题，两轮封顶，然后按标注的偏好推断继续；低风险可逆的决策默默走 | SKILL.md First-Turn Style + authoring-discipline §1 | L1 |
| H11 | 外科手术式变更：只碰直接服务本次变更的文件；顺带发现的 dead code 提及但不清理；每个 changed line 能解释服务于哪个目标 | authoring-discipline.md §3 | L1 |
| H12 | 首版交付后只列三个最高价值迭代方向；不可验证的想法进 next-step candidates | iteration-philosophy.md | L1 |

建/不建与模式-门禁速查（他脑内的决策表）：

- 请求 → 不建判定：一次性回答 / 文档 / 确定性脚本 / 头脑风暴 → 不建 skill。
- 建 → 模式判定：探索个人=Scaffold；团队复用+路由错配浪费工时=Production；跨团队共享+近邻碰撞=Library；事故/发布/合规/对外声明=Governed。
- 模式 → 门禁：Scaffold{validate+boundary} ⊂ Production{+trigger_eval} ⊂ Library{+optimize_description+route confusion+packaging} ⊂ Governed{+governance score+regression history+promotion policy+trust}。

## 3. 表达 DNA

- **祈使句极简指令体**：一条规则一句话，动词开头零铺垫（"Keep `SKILL.md` lean"、"Add gates by risk, not by habit"、"Do not scan private logs implicitly"）。SKILL.md 主入口 56 行讲完全部路由+模式+工作流+门禁。**[L1]**
- **票据化字面标签**：治理语义固化在英文字面标签里并要求逐字保留——"Preserve labels literally when they apply: `file-backed fixture`, `input_files`, `output contract`, `rollback boundary`, `trust report`, `missing evidence`"（SKILL.md）。标签即可机读契约。**[L1]**
- **反清单文化**：几乎每篇 doctrine 以 What Not To Borrow / Avoid / Anti-Patterns / Failure Patterns 收尾——"record what not to borrow so the new skill stays light"；反原型（Anti-Archetypes）与原型并列成节。**[L1]**
- **审阅者收尾**：每篇方法文档以 Reviewer Questions / Reviewer Rule / Reviewer Checklist 结束（"A reviewer should be able to answer: What does this skill own?...Which evals prove the contract?"）——文档为审阅者写，证据为审阅者留。**[L1]**
- **表格驱动决策**：score bands 表、risk→gate 映射表、1.0 vs 2.0 六维对照表、governance 分数桶（90-100 governed / <45 draft），拒绝散文式含糊。**[L1]**
- **编译器/测试工程词汇迁移**：IR、compile、adapter、gate、holdout（train/dev/blind/adversarial）、fixture、ledger、drift、waiver、promotion——用软件工程成熟词给 prompt 工程立规范。**[L1]**
- **边界语言与正向能力同权重**：should-not-trigger、near-neighbor、exclusions、non-goals 在每个层次（description/IR/boundary design）都与正向描述并列出现。**[L1]**
- **中英双轨语气**：工程正文英文硬约束；对用户首轮对话"In Chinese, sound soft and companion-like"——规则硬、语态软，两者刻意分离。**[L2]**
- **自评带边界声明**：README 自评 91.5 分仍声明"local engineering evidence, not a claim of world-class readiness"；盲评 5/5 仍标注"single-reviewer... rationale fields are still empty"。展示即自我门控。**[L1]**

## 4. Skill OS 2.0 工程哲学

六环生命周期（README 架构图）：`Inputs（粗糙运营材料）→ Intent model（job/outputs/exclusions/standards）→ Skill IR → Package + Target compilers → Eval Lab → Review Studio → Release boundary → SkillOps loop → 回 Intent model`。

四句方针（README 原文）："keep the entrypoint light, make evaluation hard to fake, make governance visible, and continue reducing the friction of first-time creation and review."

命名即纲领：YAO = Yielding AI Outcomes——"the goal is not to generate more prompt text, but to produce reusable AI assets and real operational outcomes"。

1.0→2.0 的演进逻辑：1.0 解决"把重复工作变成可安装的包"，2.0 解决"包变成资产后的全生命周期治理"（语义契约、编译、行为测试、发布证据、迭代追踪）。对标 Anthropic/OpenAI 官方 skill creator 时不用贬低对手，用加权维度表 + "Best-Fit Scenarios" 分场景共存建议（draft conversationally, then harden with yao）。

## 5. 对 penguin-oss-suite 架构的指导（可执行）

1. **路由层补契约测试**：oss-workflow 是套件唯一场景入口，8 个成员高度近邻（"改 README"→oss-voice vs oss-scaffold；"安全问题"→oss-security vs oss-contribution R11 兜底）。按 M5/H3 给每个 skill 写 should-not-trigger 近邻样例 + no_route 样例，建 route confusion 测试集；任何成员改 description 必须跑混淆对照，防"路由偷窃"（yao 的 build_confusion_matrix.py 思路）。
2. **套件成员补治理元数据**：套件是 Library 级共享资产但缺 manifest。每个 skill 补 name/version/owner/review_cadence/status/maturity_tier；org-sweep 语料在持续更新（2026-09-28 已重抓一轮），review_cadence 声明风格规则的过期边界（M1/M6）。
3. **org-sweep 证据分级升级为 claim guard**：现有 L1-L4 分级与 yao 的 evidence ledger 同构，再进一步——套件对外声明（"三标杆仓风格""12 仓实测"）挂证据台账，pending 蒸馏不计入已验证；套件 README 能力声明与 corpus 实际抓取覆盖度对齐，缺的标 missing evidence（M1/H8）。
4. **升级路径按四模式走**：套件当前状态 = 内部 Production；对外公开发布 = Governed 门槛（脚本权限审查 trust check + 安装模拟 + release lock + waive 记录）。不一步到位，也不跳级（H2）。
5. **多宿主分发建中性元数据**：套件目前绑定 DSH 宿主与 junction 部署；若分发 Claude Code/Codex，建 `agents/interface.yaml` 中性元数据源，一次建模多平台编译，不复制改写 SKILL.md（M3）。
6. **迭代纪律**：套件每次大改后只列三个最高价值方向（当前最值得的三个：路由混淆测试集 → manifest 治理元数据 → 声明-证据台账对齐），防全向扩张；无法验证的改进想法进 candidates 不进 baseline（M7/H12）。

## 6. 证据分级汇总

- **L1（多处文档直接支撑）**：M1、M2、M3、M5、M6、H1-H6、H8、H10、H11、H12、表达 DNA 除中英双轨外全部
- **L2（单文档深度展开 + 他处呼应）**：M4（systems-thinking 单 doctrine + README system-model 落地）、M7、M8、H7、H9、中英双轨语气
- **L3**：未使用
- **L4**：未使用——无仅凭单例推断的特征
- 缺失：Issues/Discussions 作者即席回复未取得，口语层表达（安慰/争论/拒绝的措辞习惯）未覆盖；个人经历与观点类素材（访谈/演讲）未采集，本卡不含此类内容

## V2 补强（2026-09-29 · 第二轮深度蒸馏）

**裁决 3 补强——trigger_eval.py 输出格式实证**
- 一手：本机 `skills-src/vendors/yao-meta-skill/scripts/trigger_eval.py`（与 local/ 副本同源）逐行读取。输出结构：顶层 threshold + threshold_explanation + false_positives/false_negatives + precision/recall；bucket_stats 按 should_trigger / should_not_trigger / near_neighbor 三桶给 total/passed/pass_rate；family_stats 按用例族聚合；misfires[] 逐条列 bucket/family/prompt/score/reason（false_positive|false_negative）/matched_desired_concepts/matched_negative_concepts；results 内每条 case 带 score_detail（semantic_coverage、support_score、lexical_support、negative_penalty、coverage_boost、concept_evidence 正负概念逐短语回显）。
- 两个 gate 语义：①score 落在 0.75×~1.25× threshold 自动标 boundary_case；②任一 misfire 时 `raise SystemExit(2)`——报告可读、退出码可判，评测本身 fail-closed。默认阈值取 cases JSON 的 recommended_threshold（缺省 0.48）；--description-file 可直接解析 SKILL.md frontmatter 的 description。
- 对套件含义：should-not-trigger 契约不止写进 description，还要落成三桶 + 逐条 misfire 回显 + 退出码的可执行评测。

**新增裁决 5——Skill OS 四方针套到套件升级路线**
- 依据为 README 四方针原文（见 §4 已录），V2 只做套用：entrypoint light→SKILL.md 减肥纪律；evaluation hard to fake→先评测后功能；governance visible→manifest/台账/留痕三件套前置；friction down→每轮迭代后创建与审阅成本必须下降。均为蒸馏者套用（非他本人对本套件的表态）。
- SKILL.md 变更：裁决 3 加 1 条补强、新增裁决 5、使用方式映射更新；其余未动。

