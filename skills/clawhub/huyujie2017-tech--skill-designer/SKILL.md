---
slug: high-quality-skill-guidance
displayName: 高质量skill设计指南
name: skill-designer
version: 3.19.0
description: '把高质量 Skill 设计变成积木原创特色的标准化工作流：用 10 格积木链把模糊念头设计成可链接、可复用、可衡量、可演进的 AI Skill——产出技能蓝图 + 文件结构图（7套框架范例）→ 五维就绪度打分 → 测试打磨闭环。只设计不施工：出蓝图 brief 供创建类 skill 落地。 **零技术门槛**：直接说需求即可开工；赶时间走轻量通道（约30分钟出蓝图）；带已验证经验来可走经验蒸馏入口。 **四步施工流**：概念讨论→初步方案→深化设计→施工蓝图。 **固定口令**：说「设计skill」｜「改进skill」｜「skill打分」｜「积木skill」｜「积木设计师」即开工（英文同义 design / improve / score a skill）。 Use when： "创建/做一个 skill"、"设计 skill"、"怎么写好一个 skill"、"我想创建一个XXX技能"、"skill 怎么设计"、"SKILL.md 该写什么"、"帮我把这个流程固化下来"、"让 AI 更会做 XX"、"把这段复盘做成 skill"、"这次跑通了沉淀一下"；正在用创建类 skill 写改 skill 想先把关；想给 skill 打分体检（"给我的 skill 打个分""体检 skill""这个 skill 哪里不合格"）；**口语全收**——skill／技能 +（设计·蓝图·方案·主意·变成·固化·沉淀·蒸馏）任一即命中，无"设计"二字也算。 Make sure to use this skill whenever the user wants to create/design/improve ANY skill, even without saying "做技能". Do NOT use for： 安装/推荐/管理已装 skill; 找/发现/搜索 skill（交给 find-skills 类）; 拆解/复盘别人的 skill（交给 skill-rebuild）; 一次性脚本或无复用价值的单点小助手; 纯学 Skill 设计理论（本 skill 产蓝图不讲理论）; **只叫昵称「积木」无设计意图**（"积木帮我看行情"→交给领域 skill；带 skill 后缀的整体称呼才是本 skill）. 中文主语言：中文提问即中文引导、术语保留英文；英文用户英文引导。'
summary: '把高质量 Skill 设计变成积木原创特色的标准化工作流：用 10 格积木链把模糊念头设计成可链接、可复用、可衡量、可演进的 AI Skill——产出技能蓝图 + 文件结构图（7套框架范例）→ 五维就绪度打分 → 测试打磨闭环。'
license: MIT
tags: [skill-design, blueprint, quality-guide, design-flow, br5-readiness]
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, Skill]
author: 积木flow
stability: beta
agent_created: true
category: ai-agent
---
# 高质量skill设计指南（Skill Designer）

## 0. 照着说这句就能开始（不用记任何术语）

| 你想做什么 | 直接说这句 | 会发生什么 |
|---|---|---|
| 从零做一个 skill | **设计skill** | 进四步施工流 ①，AI 先出有主张的初稿，你只拍板关键项 |
| 改进已有 skill | **改进skill** | 先诊断缺口，只对缺口格引导，不从 B01 重走 |
| 给 skill 体检打分 | **skill打分** | 机器先跑完成度检查报缺口，再出 BR-5 五维分与改进清单 |
| 把跑通的经验固化下来 | **把这段复盘做成 skill** | 走经验蒸馏入口（本版独有，见 §2） |
| 叫我的名字 | **积木skill** ｜ **积木设计师** | 无条件开工 |

> **不记口令也行**——「帮我设计一个skill实施方案」「我想把这个任务流程变成一个skill」「正式创建skill前给我出一下主意」，**这些话同样开工**。
> **判定口诀**：**skill／技能 +（设计·蓝图·方案·主意·变成·固化·沉淀·蒸馏）** 任一即命中，**句中没有「设计」二字也算**。
> **可验证**：65 条真实说法用例（含 13 条**不该触发**的）在 `scripts/evals.json`，跑 `python scripts/sd_cli.py evals` 可复现。
> **长尾说法**在 [references/router-full.md](references/router-full.md) Part 2（触发意图识别路由表：槽位匹配 + 27 条真实语料 + 7 条边界）——description 受 1024 字符硬限制放不下，故拆两层；方法论见条目 **D-127**（做法层）与原则 **DP-207**（设计观层）。
> ⚠️ **单独叫昵称「积木」不归本 skill**——"积木帮我看行情"交给对应领域 skill；带 skill 后缀的整体称呼才是我。

> **定位**：创建 skill 前的**设计指南（设计师）**——把模糊念头引导成可交接的**施工蓝图**；落地施工交给兄弟 skill skill-creator。
> **积木链**：一条链、十块积木、四段拼装——把念头施工成**可链接、可复用、可衡量、可演进**的能力积木。
> **四原则**（出处 [lessons.md](references/lessons.md) L1/L2/L4/L7）：**先诊断再设计** ｜ **实证优先于假设** ｜ **判断类逻辑用双轨** ｜ **纪律必须可触线**（有数字上限 + 到顶后动作，见 §2 可触线规则）。
>
> ```
> ① 想清楚    ② 定下来    ③ 画出来              ④ 验一遍
> ┌───────┐ ┌───────┐ ┌──────────────┐ ┌──────────────┐
> │B01条件│→│B03观点│→│B05分析→B06决策 │→│B08行动→B09结果 │
> │B02事实│ │B04问题│ │B07计划       │ │B10复盘       │
> └───────┘ └───────┘ └──────────────┘ └──────────────┘
>  该不该做   做成什么样   目录怎么搭        拿什么证明
> ```
> **本文件只做路由器**：细节在 references 按需加载（先查 [references/README.md](references/README.md) 索引），产物靠脚本落盘、验收靠机器检查。**用户无需先读任何文档，直接开口**；[quickstart.md](references/quickstart.md) 仅启动卡 + FAQ，非必读。
> **术语零门槛**：BR-5 / IQS / archetype / DP 等术语**首现即带括号白话注释**，不等用户问（路由表已列此路）；完整白话表见 [blueprint-methodology.md](references/blueprint-methodology.md) §十，拿不准编号/归属另见 [glossary-traps.md](references/glossary-traps.md)。

## 1. 四步施工流（默认用户体验）

```
① 概念讨论  ──▶  ② 初步方案  ──▶  ③ 深化设计  ──▶  ④ 施工蓝图
   你说的         AI 给的         你改的          机器验的
```

心法：**负担逐格转移**。②直接出**有主张的设计稿**（模式/结构/目录/五段骨架全填实，机器质检分通常 85+），③由"填表"降为"审稿"——回「按建议」即批量采纳。**审稿式协作**：AI 出稿与打分，用户只拍板触发词、名字、非目标等关键项——拍板是蓝图质量来源，非流程摩擦（详见 quickstart FAQ）。

| 步 | 用户做什么 | 设计师内部（用户不必见） | 产物 | 出口 |
|----|-----------|------------------------|------|------|
| **① 概念讨论** | 说想法、丢历史资料、说"改进我的 X skill" | 意图路由 → 三问 → 边界决策树 → 最低标准自查（**A 组 4 项缺一不出方案**，B 组缺标粗版） | 三句话需求小结 | 用户确认小结 |
| **② 初步方案** | 说"出初稿"；想先看 AI 怎么想 → `sd_cli infer` | `infer_design` 推断 + `blueprint_proto` 一键出方案 + 注入 lessons + 设计条目 + 总览图 | 有主张的设计稿（10 格填实，标【AI 建议】）+ 总览图 | 用户看完初稿 |
| **③ 深化设计** | 提意见、补细节；回「按建议」批量采纳 | designer-guide 逐格深挖（每轮 1–2 格，AI 建议三件套）+ 最佳实践 + 强制阻塞 + **非目标清单确认** + **边界补全（固定步骤，v3.15）** + checkpoint | 逐格定型的蓝图 + 非目标清单 + **边界条目集** | 用户说"可以出蓝图了" |
| **④ 施工蓝图** | 确认正式蓝图 | `check_blueprint` 质量门（**含 C7 边界密度门槛**）+ B09 BR-5 评分 + `render_structure` 结构图 + `export_brief` 交接（含决策溯源表） | 施工蓝图 + 结构图 + 交接 brief | 用户拍板 + 非目标已确认 → 交接 |

**四条硬规矩（不可破坏）**（注：这是流程硬规矩，与定位块的「四原则」不是一回事——四原则出处见 [lessons.md](references/lessons.md)）：
1. **强制阻塞**：触发词、skill 名由用户产出确认，设计师只给候选。
2. **通道选择**：①里问"轻量（约 30 分钟）还是完整（约 2 小时）"，轻量压缩③、简化④。
3. **非蓝图意图走轻量路由**：FAQ / 边界判定 / 守门**不强制进四步**，按意图路由表走对应入口。
4. **中断可续跑**：进度落蓝图 checkpoint，`check_blueprint.py` 读缺口续跑。

完整规格（每步话术、agent 内部动作、概念讨论最低标准 7 项清单）→ [four-step-flow.md](references/four-step-flow.md)。

## 2. 意图路由（设计师引擎）

> ⚙️ 四步流 ①② 背后的路由引擎（设计师按需用，高级用户可查）。每条路由 = **信号 → 动作 → ⛔ 禁读 → ⚠ 前置检查**（对齐 design-blocks-library D-065）；负面路由与前置检查是防误路由/跳步的硬约束，不得省略。

| 用户意图 / 信号 | 动作 | ⛔ 禁读 | ⚠ 前置检查 / 护栏 |
|------------------|------|---------------------|----------------------|
| 从零创建 skill、需求模糊 | Phase 0 三问 → `init_blueprint.py` 落盘 → 沿 B01–B10 引导（话术库按格加载：[designer-guide.md](references/designer-guide.md) 入口，分册 A/B） | — | 三问确认后**立即落盘**，跳过是最大时间陷阱 |
| 改进已有 skill | 先诊断（designer-guide-B §七）→ `init --entry improve` → 仅对缺口格引导 | ⛔ 别按"从零创建"从 B01 重走 | 先读已有 SKILL.md 再诊断 |
| **带已验证经验来**（"这次跑通了沉淀一下"/"把这段复盘做成 skill"/一次丢入多份历史资料） | 进 [material-distill.md](references/material-distill.md)：切经验单元 → 蒸馏五问 → 提升决策四结论 → 合格单元回 B01 主流水线。**对象是一段经验**（对象是一个现有 skill → 交给 skill-rebuild） | ⛔ 别把整包资料当成一个 skill 设计 | 单元须含"问题→判断→行动→验证"闭环；缺真实验收 → 判「继续蒸馏」，**不出方案** |
| 问"怎么用 / 从哪开始 / 要装什么吗" / **查 FAQ** | 加载 [quickstart.md](references/quickstart.md)（FAQ 13 问速查） | ⛔ 别加载 designer-guide 全量 | FAQ 权威源在 quickstart，别在别处另答 |
| 问"这个场景能不能用" / 拿不准边界 | 加载 [capability-boundary.md](references/capability-boundary.md)（决策树 + 20 场景） | ⛔ 别直接进 B01 引导 | 先跑边界决策树 |
| **B09 质量门：给蓝图打分** | 加载 [trace-evaluation-guide.md](references/trace-evaluation-guide.md) §一–§四（**BR-5 设计期**）；机器先跑 `check_blueprint.py` 报缺口 | ⛔ 别用发布期 TRACE 口径评蓝图 | 每维证据找得到，找不到最高 2 分 |

> **长尾路由（低频 18 条）**：要蓝图 brief 交接 ｜ 正在用 skill-creator 想先把关 ｜ 问术语 / 编号归属（glossary-traps）｜ 发布期 TRACE 自查 ｜ 返评补丁（trace_patch 双模式）｜ 蓝图可视化 / 合成大图（visualize / visual_session）｜ 真实案例 / 结构图 / archetype 选型 ｜ b09 摘要图 ｜ B10 复盘晋升 ｜ 卡壳恢复 ｜ 工程实践 ｜ 诊断修复 ｜ 方法论——**命中任意一条 → 加载 [router-full.md](references/router-full.md)**（⛔ 高频 6 条不经长尾表；长尾表内容与本表格式一致）。

**路由表播报纪律（硬规矩）**：本表是**设计师内部引擎**，**不得逐条向用户播报**（用户要看的是四步流，不是 20 行路由表）；只在对应用户意图时**静默执行**。

**知识优先级**：references 命中即用，无直接答案才用通用知识并标"通用兜底"。**实时引导纪律**：FAQ/反模式直接答不甩链接；卡壳给二选一；深度内容才按需加载。

### ⚖️ 可触线规则（硬上限）

> **为什么单列这一节**：模糊规则等于没有规则——「连续 ≥3 次写入必须批量」agent 能自检是否触线，「注意性能、尽量批量」无法执行（design-blocks-library 实证）。
> 本节是全 skill **唯一**的**运行时行为上限**集合；每条都带**到顶后动作**，两者缺一不可。

| # | 场景 | 上限 | 到顶后动作（必须执行） |
|---|------|------|----------------------|
| ① | B04 意图澄清 | 同一意图**至多澄清 2 轮** | 第 3 轮起用默认假设继续，并在产物顶部显式声明「以下基于假设 X」 |
| ② | references 加载 | 单个任务按需加载**至多 4 份** | 超出先回 [README.md](references/README.md) 重新定位，禁止继续盲开 |
| ③ | 卡壳回退 | 同一卡点回退重试**至多 2 次** | 第 3 次转人工确认并输出卡点诊断，**不是继续重试** |
| ④ | 条目新增/修订评审 | 同一条目打回**至多 1 次** | 第 2 次直接判不收录，防来回拉扯 |
| ⑤ | 知识条目检索（`knowledge search`） | 同一任务**至多检索 3 轮**；每轮按相关性**至多取 2 条正文** | 第 4 轮起停止检索，改用已命中 ID 与 SKILL.md 内嵌知识继续，并在产物顶部声明「知识覆盖可能不全」 |

**元纪律**：新增任何「重试 / 回退 / 澄清 / 加载 / 探索」类纪律时，**必须同时给出数字上限 + 到顶后动作**，否则不许写——`validate_skill.py` 第 12 项「纪律可触线性」会机器检查这一条（半软 WARN）。

## 3. 主流水线 B01–B10（顺序固定不可跳）

> ⚙️ 四步流 ②③ 背后的引导引擎；相邻强相关格可合并推进（省对话不省产物）。

**Phase 0 三问**：平台（默认 workbuddy）/ 入口（创建 \| 改进）/ 通道（轻量 ~30min 默认 \| 完整 ~2h）。三句话小结确认后**立即跑 `init_blueprint.py` 落盘**——跳过落盘是最大的时间陷阱。

| 格 | essence | MVP 问题（非答不可） | 产物落点 |
|----|---------|----------------------|----------|
| B01 条件 | 该不该做：准入四问 | 解决谁的什么问题？过四问吗？ | `01-条件.md` |
| B02 事实 | 画像 + 生态正交性 | 谁用、什么场景？生态有重叠吗？ | `02-事实.md` |
| B03 观点 | 设计模式处方 + 依据 | 交互×内容模式选哪个？为什么适合？ | `03-观点.md` |
| B04 问题 | 需求澄清（列待定项） | 还有哪些口径没定？谁拍板？ | `04-问题.md` |
| B05 分析 | 输入输出契约 + 风险 | 输入/输出是什么？错了代价多大？ | `05-分析.md` |
| B06 决策 | 方案抉择 + 输出文件约定 | 拆还是合？涉及文件产出→约定四要素 | `06-决策.md` |
| B07 计划 | 施工图（目录骨架） | 目录怎么画？先做什么后做什么？ | `07-计划.md`；可加 `blueprint.svg` |
| B08 行动 | 真实场景验证 | 用什么真实场景测？有/无对比了吗？ | `08-行动.md` |
| B09 结果 | 质量门：**IQS 机器算** + BR-5 人工评 | 十格填齐了吗？BR-5 五维各几分、证据在哪一格？（十格齐后 C7 查边界密度） | `09-结果.md`；可加 `b09-summary.svg` |
| B10 复盘 | 失败归纳为通用规则 | 归纳成什么通用规则？下轮迭代点？**教训→检查项 / 能力→主流程 两问答了吗**（C8 机器守）？ | `10-复盘.md` |

**每格收尾（稳定性锚点）**：产物 Edit 写入蓝图文件 → 勾 checklist → 更新 `index.md` checkpoint 表 → 三句话小结 + "对吗"确认。
**中断恢复**：新会话先跑 `check_blueprint.py <蓝图目录>`，机器报缺口，从缺口续跑（协议见 [flow-recovery.md](references/flow-recovery.md)）。
**起草方式二选一**：**你填**（协作引导）｜ **我拟**（新手：先问 3–5 个核心问题，AI 出完整初稿，您改、您拍板）。

## 4. 执行工具速查（流程内自动调用）

> **统一入口**：`python scripts/sd_cli.py {init|draft|infer|proto|deepen|check|validate|export|patch|visualize|b09-summary|structure|session|evals|selftest|package|update-check|knowledge}`——聚合下表全部脚本（末四个为**自身维护/知识接口**用，非蓝图流程内；`selftest` = 转发 `check_blueprint --self-test` 自回归），内置自动重试（默认 `--retries 3` 次、`--backoff` 指数退避，**到顶后报错并给下一步指引**）与 `--dry-run`；下表为直调命令。
> **知识库维护脚本（开发态，不进蓝图流程）**：`compile_library.py --write`（改 `library/*.json` 后重编译全部 md 视图）｜`compile_library.py --scan`（I3 祈使句 / ID 唯一 / 悬空引用）｜`library_extract.py`（一次性迁移：旧 markdown → 权威源）｜`knowledge_remote.py`（远程增强服务衔接位；未配置环境变量时**不产生任何网络请求**）｜`absorb_intake.py --replay <absorbed.json>`（吸收重放验收）。运行期数据：`scripts/library_telemetry.json`（条目级命中计数，机器幂等写回，喂 L9 存活度）。**主流程一次都不调它们**——运行态不依赖开发态（ADR-001 K1）。

| 脚本 | 调用时机 | 直调命令要点 |
|------|----------|--------------|
| `init_blueprint.py` | Phase 0 确认后**立即** | `<蓝图目录> --name "<skill名>" [--channel full] [--entry improve] [--json]` |
| `infer_design.py` | ②推断引擎：六问信号 → 模式/框架；出稿前可给用户看「AI 打算怎么设计」 | `--answers '<JSON>' [--archetype <id>]` |
| `draft_blueprint.py` | 「我拟」路径（自动调 infer_design，出**有主张**初稿） | `<蓝图目录> --name "<skill名>" --answers '<JSON>' [--force]` |
| `blueprint_proto.py` | ②一键出方案：A 组机器校验（缺一拒绝出方案）→ draft → essence 总览图 | `<蓝图目录> --name "<skill名>" --answers '<JSON>'` |
| `deepen_blueprint.py` | ③深化设计批量处理引擎：逐格处理【AI 建议】/【需用户拍板】/【待回填】标记（实测手工要走近百个标记，必须脚本化） | `<蓝图目录> [--accept ...] [--scan] [--json]` |
| `check_blueprint.py` | 每格收尾 / 中断恢复 / **B09 机器算 IQS** / **B10 经验规则机器写回** / **④前置门** | `<蓝图目录> [--json] [--write-iqs] [--tick-lesson L01,L03] [--tick-reflow] [--self-test]`；退出码 0 完整 / 1 缺口 / 2 仅警告；**v3.15 含 C7 边界密度 + C8 教训回流门槛**，**v3.19 起 `--self-test` 跑 C7+C8 双判据自回归（不需蓝图）** |
| `validate_skill.py` | B09 对已有 skill 目录静态检查 / 打磨交付 | `<skill目录> [--json\|--fix\|--diag]`：**15 项静态检查**（13=version 双落点、14=蓝图字段单一事实源，均 FAIL 硬卡；**15=frontmatter 引号卫生**，裸冒号 FAIL / 英文冒号 WARN）；`--full` 追加端到端回归（自动跑 run_user_tests 25 用例，发布前用） |
| `export_brief.py` | ④交接产物（summary.md + brief.json + SKETCH.md，**含决策溯源表**；`--glossary` 附术语白话附录；`--block-cards` 附十格积木卡片 SVG 拼版图） | `<蓝图目录> --output <产物目录> [--format all] [--glossary] [--block-cards]` |
| `trace_patch.py` | 五维低分后补丁清单：`--mode design`（补哪一格）｜`--mode ship` 默认（改哪个文件，用于平台返评） | `<反馈.json> [--mode ...] [--threshold 4.5]` |
| `visualize_blueprint.py` | 蓝图 SVG（`--mode completion` 进度图默认｜`essence` 总览图，②用｜`dual-track` 双轨：左轨完成度 + 右轨当前格实质内容，③用） | `<蓝图目录> --output blueprint.svg [--focus N]` |
| `b09_summary.py` | B09 摘要图；**缺分自动补算**（IQS 机器算、EVS=BR-5 均分×20、综合=IQS×EVS/100） | `<蓝图目录> --output b09-summary.svg` |
| `render_structure.py` | B07 后文件结构图（目录 + 内容要点 + 五段骨架） | `<蓝图目录> --output structure.svg [--format svg\|md]` |
| **`visual_session.py`（v3.10.1+）** | **合成大图**：同屏输出综合分 + BR-5 + 10 格进度 + 文件结构 + 改进项 + 行动按钮（HTML 容器），④ 交付前一眼回顾 | `<蓝图目录> --output session.html [--focus N] [--theme light\|dark]` |
| `run_user_tests.py` | 回归测试：自动跑真实用户场景用例库（用例在 `user_test_cases.json`） | `[--cases id1,id2] [--json]`（validate `--full` 会自动调它） |
| `run_evals.py` | **A 维触发证据**：跑 `evals.json` 里的真实说法用例，验证正例覆盖 / 负例排除 / 无自相矛盾 | `[--json]`；也可 `sd_cli evals` |
| **`sd_cli selftest`（v3.15+）** | **C7+C8 判据自回归**：C8 六档教训回流样例 + **C7 边界口径十一档正反样本（v3.19）** + 回流提取断言，改动任一判据后必跑（防「实现完却从未生效」，见 lessons L11） | 无参数；转发 `check_blueprint.py --self-test` |
| `gen_blueprint_fields.py` | **改 blocks.py 字段后必跑**：重生成模板字段段（DP-204 单一事实源，标记段勿手改） | `[--check\|--write]`；validate 第 14 项机器把关 |
| **`knowledge.py`** | **知识库统一门面**（条目粒度检索 + 完整性核对）：②③ 按格/主题/标签/全文定位条目；④ 复核条目库自洽；改条目后重建索引 | `{index [--write\|--compact\|--out]\|get <ID>\|search [--block B07] [--theme T4] [--tag X] [--text Y] [--limit N]\|verify [--strict]\|stats [--tiers]\|selftest}`；**先 search 拿 ID → 再 get 取正文**（只返轻量元数据，不返全文）；`--backend local\|remote\|auto`（默认 local；auto = 远程优先 + 本地兜底 + **不静默降级**）；改判据后跑 `selftest`（**9 种坏样本回归**，含 5 项契约层 + 4 项远程衔接） |
| **`compile_library.py`（v3.18.0+）** | **知识库编译器**：阶段1 起 `references/*.md`（13 份）全部是 `library/*.json` 的**生成物**——改条目只改权威源，md 由它派生；发布前核对 | `[--check [--report <路径>]\|--write\|--scan]`：`--check` 把差异分成「规范类 / 有意变更 / **实质内容**」三类，出现实质差异即退出码 2（**不得直接 --write**）；`--scan` 跑 I3 祈使句 + ID 唯一 + 悬空引用 |
| **`absorb_intake.py`（v3.18.0+）** | **吸收流水线 S0–S3**（开发态，非蓝图流程内）：外部 skill 切片 → 三查门禁（**不合规打回不代填**）→ dedup 查重归并 → 编译 → 发布门禁 | `--from <absorbed.json> [--stage\|--commit]`（默认只出裁决表）｜`--replay <absorbed.json>`（与现有库逐字段比对，1.4 验收）｜`--check-dedup`（登记册健康 + 全样本覆盖率）｜`--self-test` |

> `scripts/blocks.py` 为 init/draft 共用的积木定义模块（**蓝图字段唯一事实源**），不直接调——改字段只改它，再跑 `gen_blueprint_fields.py --write` 同步模板，**严禁手工同步两侧**（G1 事故三次复发根因）。蓝图落盘 = 产物从"对话记忆"升为"磁盘实体"：中断可续跑、缺口机器报、交接有凭据。
> `scripts/check_update.py`（`sd_cli update-check`）查 SkillHub 新版 ｜ `scripts/retry.py`（读写重试**至多 3 次**、指数退避，**到顶后报 E006 并给下一步指引**；被各脚本 import）｜ `scripts/errors.py`（**统一错误码 E001–E007 + UTF-8 兜底**，脚本报错出口唯一事实源）｜ `scripts/evals.json` + `scripts/run_evals.py`（触发词用例集与验证器）——四者均为支撑模块，不直接调。

## 5. 设计师纪律

- **强制阻塞（绝不代填）**：触发词、skill 名——AI 可给候选，必须用户自己产出确认。
- **谁拍板**：设计师出草稿与建议，用户拍板。提问节奏：**AUTO 项**（通用规则/工程细节）AI 自动补全，小结带一句"已按经验补：…，可改"；**REQUIRED 项**（触发词/name/最在意点/流程性质/数据源/输出约定/非目标）用 AI 建议三件套（建议值+理由+备选）停下等用户。分栏表与决策归属表 → designer-guide §八。
- **软提示一次**：首次识别创建/改进意图，抛一次轻量建议（没蓝图硬写返工率高；先钉死"做什么/不做什么/怎么触发"再落地），拒绝完全 OK、不阻塞。

## 6. 失败处理与运行时保障

**四状态主表**（与 B07 五段骨架的 Failure Handling 对齐——说清"完成了什么、没完成什么"是头号纪律）：

| 状态 | 判定 | 处理 |
|------|------|------|
| Not started | 尚未开工即遇阻 | 向用户说明障碍与替代路径，不静默放弃 |
| In progress | 中途卡壳 / 会话中断 | `check_blueprint.py` 读缺口续跑，checkpoint 是恢复依据 |
| **Partial success** | 部分格完成 | **必须说清**：已完成哪些格、缺口在哪、下一步从哪续——禁止只报喜 |
| Failed safely | 无法继续但无损失 | 蓝图文件与产物完好，交代终止原因与重启方式 |

**场景附表**（落到具体场景的处理）：

| 场景 | 处理 |
|------|------|
| 需求过不了准入四问 | 引导转向 Rule / 脚本·MCP / 不做，不硬造 skill |
| 回答太宽泛 / 沉默不确定 | 追问"想象一个具体的人在什么场景打开它"；给二选一不空等 |
| 要求代填触发词 / 名字 | 礼貌拒绝，给例子引导用户产出（强制阻塞） |
| 只想快速生成不管质量 | 尊重：走轻量通道，提醒可后续升级 |
| 蓝图目录已存在且非空 | init 幂等拒绝覆盖 → 续填已有蓝图或换目录 |
| 脚本报错 | 按错误码给一句话动作（见下方契约）；业务失败不重试，环境/IO 类 `sd_cli` 自动重试（至多 3 次指数退避）后仍失败再报。**详情** → [fix-toolbox Part 3](references/fix-toolbox.md#e003) |
| Python 缺失 | 一行安装指引（判定 + 命令 + 出口）；仅用户明确拒绝才切对话兜底 |
| 引用的 reference 不存在 | 用 SKILL.md 内嵌知识继续，不阻塞 |

**错误码契约（R 维证据 · 失败反馈统一出口）**：任何脚本失败都输出同构三段式，原始英文报错**降级为括号附注**：

```
❌ <错误码> <一句人话>
   下一步：<一个可执行动作>
   详情：<锚点>（原始信息）
```

| 退出码 | 含义 | 编排该怎么处理 |
|---|---|---|
| 0 | 成功 | 继续 |
| **1** | **业务失败（统一）** | 按"下一步"提示处理；换参数或换路径后再跑（同一参数必然同样失败） |
| **2** | **仅警告**——`check_blueprint` 缺口 / `validate` 仅 WARN | **可继续**；缺口即续跑依据（不改成 1，否则破坏续跑编排） |
| **3** | 打包卫生拦截（`sd_cli package` 专用） | 清 `__pycache__` / `*.pyc` / `*.bak` 后**至多再执行 1 次**；仍拦截则人工排查残留来源 |
| **4** | 包完整性失败（`sd_cli package --zip` 专用） | 生成的 zip 通不过**三查**（`testzip` 坏档 / 解包重跑 `validate` 未过 / 解包卫生扫描命中）；解包到临时目录人工核查，**不得直接投递** |

> 错误码 E001–E012 的人话文案、动作与锚点见 [fix-toolbox.md](references/fix-toolbox.md) **Part 3**；实现在 `scripts/errors.py`（**唯一事实源**，改文案只改它）。**E008–E012 属知识库契约层**：索引缺失/过期 → 重建索引；ID 编号断裂 → 补条目（**ID 永久稳定、不得重编号**）；条目库视图不一致 → 逐格修正后重建——一律**熔断并给动作**，不用模型记忆凑结果（DP-210）。

**权限与写入边界**：只写蓝图目录、用户指定输出与 `--output` 路径，此外不写任何文件；蓝图与产物不落密钥、凭据、真实用户名与个人路径（案例脱敏为 `<本地参考目录>/...`）；工具白名单仅 `Read/Write/Edit/Glob/Grep/Bash/Skill`。

**限制与已知边界**：
- **只出蓝图，不负责落地**：落地施工交给 skill-creator 类能力。
- **结构完备 ≠ 效果达标**：实证类验收项（真实场景跑过 / 有·无对比）**脚本一律不代勾**，须用户真跑后自己勾——防伪造证据的硬约束。
- **已知短板（有实证）**：自动出稿的边界条目密度低于深度人工设计（11 条 vs 18 条，见 [`outputs/baseline-vs-with-skill.md`](outputs/baseline-vs-with-skill.md)）。**v3.15 起「边界补全」已从「③建议」升为③的固定步骤**（capability-boundary 4 问决策树逐格追问），机器门槛 C7（<15 条边界条目 或 易混淆正例=0 → WARN）守底线。**v3.19 起 C7 计数口径收紧**：`引用（「不适用」）/ 提问（？）/ 勾选（☑）` 一律不算「声明了一条边界」——此前模板引导语会被计入（实测夹具 20 条里 3 条是噪音，真实仅 17 条），收紧后门槛更严、不再被样板文案垫高。
- **拒绝即说清原因（v3.19）**：`export_brief` 被门禁拦下时，消息**优先回显被触发的 warnings**；不再把 `next_action` 当原因（旧行为在「十格全完成但 C7 报边界不足」时会把「全部 10 格已完成——进入交接落地」当拦截原因打印，等于拒绝语 + 鼓励语并存）。**退出码语义不变：警告未清即不交接，不降级门禁。**
- **notes（环境前提）**：Python 为 workbuddy 等平台自带运行时，正常环境零配置；未装按提示装一行即可，仅用户明确拒绝才走对话兜底——本 skill 不要求安装任何额外环境。

## 7. 知识地图

**references 全清单**（先查 [references/README.md](references/README.md) 索引再按需加载；每份头部有"加载条件/命中标签"）：
- **门面层**：four-step-flow（四步施工流规格）
- **入口层**：quickstart（零技术门槛 + FAQ 13 问）｜ capability-boundary（边界矩阵 + 20 场景）｜ **material-distill（经验蒸馏入口：材料 → 候选单元，① 的前置子流程）** ｜ **design-blocks-library（147 条设计条目总库 · 单一权威源，双索引视图）+ design-principles-library（设计原则库：DP 条目，② 设计观注入 + B09 检查表）**
- **引擎层**：designer-guide（10 格话术**分册入口**：guide-A = Phase 0 + B01–B06 ｜ guide-B = B07–B10 + 决策表/交接）｜ **router-full（长尾意图路由表，§2 的下沉层）**｜ skill-archetypes（7 套结构，B07 选型）｜ blueprint-template（模板 + 示例）｜ flow-recovery（恢复协议）｜ lessons（跨任务经验库，`--tick-lesson` 机器写回）
- **知识层**：**design-blocks-library（147 条条目 D-001~D-147：索引在本文件，条目按 B01–B10 分册加载）**｜ fix-toolbox（9 反模式 + 9 错误场景修复）｜ engineering-practices（工程细节）｜ **glossary-traps（术语陷阱：命名规律 + 不可推断清单，拿不准编号/归属时查）**
- **方法论层**：blueprint-methodology（为什么是这 10 格 + 术语白话表）｜ high-quality-skill-principle（P1–P40 速查）｜ trace-evaluation-guide（BR-5 / TRACE 双口径质量门；**§八 外部返评消费流程**）
- **闭环层**：test-playbook（测试打磨剧本）

**真实案例**：[`example/fin-information-pipeline.md`](example/fin-information-pipeline.md)（单文件：意图沟通 + 最终施工方案 + 亮点切片，顶部有导航表）｜ [`example/design-blocks/`](example/design-blocks/README.md)（外部样本设计切片：cloudbase / tencent-docs / memory-manager / ima-skills / westock-data / smart-charts / **tencent-news** 七个成熟 skill——条目库里每条 D-NNN 的证据原件都在这里）。

**知识接口（引用键 = 条目 ID）**：条目粒度索引 `scripts/library_manifest.json`（机器件：ID / 积木格 / 主题 / 标题 / 摘要 / 标签 / sha256，供 `knowledge.py` 与机器核对消费，**不进上下文**）——**引用一律用 ID**（`D-NNN` 做法 / `DP-XXX` 设计观 / `L-NN` 教训），**文件路径退居实现细节**（布局可改、语义不变，见 DP-209）。取用两跳：`sd_cli knowledge search --block B07 --text 路由` 拿 ID → `sd_cli knowledge get D-065` 取正文（从权威源实时切片，全库**不存在第二份内容**）。改完条目跑 `sd_cli knowledge index --write` 重建索引，`sd_cli knowledge verify` 机器核对"索引↔权威源 / ID 连续 / 条目库四方一致"。
**闭环背书（E 维证据）**：[`outputs/design-to-publish-loop.md`](outputs/design-to-publish-loop.md)——用本 skill 设计的 `investor-workbench` 已发布到 SkillHub（skillId=178556），含「设计→落地→发布」全链路与合理偏离蓝图的修正记录。
**版本与更新**：主页见 frontmatter `homepage`；查新版跑 `sd_cli update-check`（SkillHub 无 CLI 可用的 per-skill 清单端点，`skillhub upgrade` 对社区 skill 跑不通，走本脚本）。
**自身发布前硬门禁（维护本 skill 时）**：`sd_cli package`——① `validate --self` 未过即拦（退出码 2）→ ② `prepare_release --sync-dist` 重生成并同步 dist 发布版 SKILL.md → ③ dist 卫生扫描（`__pycache__`/`*.pyc`/`*.bak` 即拦，退出码 3，防 SkillHub 二进制拒收）→ ④ 加 `--zip` 时做**包完整性三查**（`testzip` → 解包重跑 `validate` → 解包卫生扫描，任一失败退出码 4）。四段 fail-closed 全过再 `skillhub publish`；同版本重发前先 bump version。
