---
加载条件: SKILL.md §2 意图路由命中的意图不在高频 6 条内时——先查 Part 1 再执行；**拿不准"这句话算不算叫我"时查 Part 2**（触发意图识别）。高频 6 条不经过本表。
核心主题: 长尾意图路由表（SKILL.md §2 的下沉层）：Part 1 内容路由（交接 / skill-creator 把关 / 学习借鉴 / 术语 / 评测 / 返评 / 可视化 / 案例 / 复盘 / 恢复 / 工程 / 诊断 / 方法论）；Part 2 触发意图识别（槽位匹配 + 22 条真实语料 + 边界）
命中标签: [路由, 长尾, 交接, 借鉴, 学习优秀skill, 返评, 术语, 案例, 结构图, 复盘, 工程, 诊断, 方法论, **触发意图, 槽位匹配, 真实语料, 触发边界**]
不回答: 高频 6 条路由（见 SKILL.md §2）；具体方法论内容（按路由加载对应分册）；一等固定口令（见 SKILL.md §0）
---

# 长尾意图路由表

> SKILL.md §2 高频 6 条之外的低频意图在此。每条 = **信号 → 动作 → ⛔ 禁读 → ⚠ 前置检查**，与主表同构（对齐 design-blocks-library D-065）。高频 6 条**不得**绕道本表。

| 用户意图 / 信号 | 动作 | ⛔ 禁读 | ⚠ 前置检查 / 护栏 |
|------------------|------|---------------------|----------------------|
| 要蓝图 brief / 对接创建类 skill | 走完 B01–B10，`check_blueprint.py` 通过后交接（designer-guide-B §九） | ⛔ 别跳过 B01–B10 直接出 brief | `check_blueprint.py` 通过 |
| **想学习 / 借鉴某个优秀 skill 的设计**（"这个 skill 哪里设计得好""参考 XX 抄个思路"） | **拆解分析交给 skill-rebuild**；成果回流走 [`../example/design-blocks/README.md`](../example/design-blocks/README.md) 四步法：亮点按 B01–B10 归位 → D-NNN 编号进 design-blocks-library → 证据原件存 `example/design-blocks/<skill-name>/`（其中 `absorbed.json` 是 skill-rebuild 导出件原名，保留以利溯源，类比引用 package.json） | ⛔ 别在本 skill 内对成品 skill 做改造实现（那是 skill-rebuild 的活）；别绕过条目库直接散装引用 | 先查切片 README「⚠️ 已覆盖 · 不必重复收录清单」，防重复入库 |
| 正在用 skill-creator 写/改 skill | 软提示一次蓝图价值；拒绝则当"原则守门员"把关 | ⛔ 别强推、别拦截 | 只软提示一次 |
| 问某个术语什么意思 | **一句话白话答**，不甩链接；术语对用户**首现即自动带括号白话注释**，不等用户问 | ⛔ 别甩链接 | 需展开才加载 blueprint-methodology §十 |
| **拿不准编号 / 文件归属 / "这两个是不是一回事"**（B04 vs B05、IQS vs EVS vs TRACE、两套骨架…） | 加载 [glossary-traps.md](glossary-traps.md) | ⛔ 别凭编号字面猜 | 先套 §一命名规律，再查 §二不可推断清单 |
| 准备发布 / 冲 SkillHub 高分（**成品**） | 加载 [trace-evaluation-guide.md](trace-evaluation-guide.md) §五–§六（TRACE 发布期） | ⛔ 别用 BR-5 口径评成品 | `validate_skill.py --self` |
| 收到外部平台返评 / 要按评分生成补丁清单 | `trace_patch.py <反馈.json>`（默认 ship 模式）→ 回填 `09-结果.md` §9.2 → 进 B10 | ⛔ 别手工改评分 | 反馈.json 字段格式合法 |
| 设计期 BR-5 低分，想知道补哪一格 | `trace_patch.py <反馈.json> --mode design` | ⛔ 别按 ship 模式输出"改哪个文件" | 补的是积木格，不是文件 |
| 想看蓝图可视化 | `visualize_blueprint.py --mode completion\|dual-track`（completion 进度图｜dual-track 双轨进度图，③ 用） | — | B07 后或施工蓝图前 |
| 想看合成大图（蓝图 + 结构 + 评分同屏 HTML） | `visual_session.py`（命令见 SKILL.md §4） | — | ④ 施工蓝图前 |
| **想看真实案例 / 最终成品长什么样** | 单文件 [`../example/fin-information-pipeline.md`](../example/fin-information-pipeline.md)（意图沟通 + 施工方案 + 亮点切片）；**按顶部导航表跳读** | ⛔ 别整包加载 | 隐私扫描（匿名化） |
| **想看 skill 最终长什么样 / 文件结构图** | `render_structure.py`（`--archetype` 选 7 套范例 / `--list` 预览，见 SKILL.md §4） | — | B07 后 |
| 不知道目录该有什么 / 该选哪种结构 | 加载 [skill-archetypes.md](skill-archetypes.md)（7 套 + 决策树） | ⛔ 别在 B07 前加载 | B07 时选型 |
| B09 评分后要摘要图 | `b09_summary.py`（缺分自动补算，见 SKILL.md §4） | — | — |
| **B10 复盘收尾 / 沉淀跨任务规则** | **复盘晋升回路**：三问检查 → 写入 [lessons.md](lessons.md)（机器写回：`check_blueprint.py --tick-lesson LXX`）→ 新任务 Phase 0 后注入 TOP 3 | ⛔ 别把特例当通用规则 | 三问全过才晋升 |
| 卡壳 / 跑偏 / 会话中断恢复 | `check_blueprint.py` 读缺口 → 加载 [flow-recovery.md](flow-recovery.md) | ⛔ 别重头问 | 从缺口续跑；**同一卡点回退≤2 次（SKILL.md §2③）** |
| 问 frontmatter / 脚本封装 / 作用域 / 拆文件 | 加载 [engineering-practices.md](engineering-practices.md) | — | 按需加载 |
| 打磨 / 诊断、要可执行修复 | 加载 [fix-toolbox.md](fix-toolbox.md) | ⛔ 别只给理论 | 先对症下药找根因 |
| 问"为什么这么引导" / 核心原则 | 加载 [blueprint-methodology.md](blueprint-methodology.md)、[high-quality-skill-principle.md](high-quality-skill-principle.md) | ⛔ 别当操作手册 | — |

---

## Part 2 · 触发意图识别路由表（说法 → 是否开工）

> **为什么单独有一张表**：`description` 受 1024 字符硬限制，塞不下用户真实会说的几十种说法。
> 解法是**双层触发证据**（条目 D-127 / 原则 DP-207）：description 放一等口令与判定口诀（平台召回层），本表放**长尾真实说法**（agent 路由层）。
> SKILL.md §0 口令卡已指向本表；`scripts/evals.json` 中 `source: router` 的用例由本表兜底验证。
> ⛔ 本表**不是**给用户读的清单，是给 agent 判定用的规则；命中即开工，**不向用户播报"我查了路由表"**（SKILL.md §2 路由表播报纪律）。

### 2.1 槽位匹配（意图 = 主语槽 × 动作槽 × 产物槽）

一句话口诀：**主语槽 S + 动作槽 V 同时命中即开工；句中没有"设计"二字也算。**

| 槽位 | 命中词 | 说明 |
|---|---|---|
| **S 主语槽** | skill / 技能 / 助手 / 智能体 / agent / 工作流 / 流程 / SOP / 经验 / 复盘 / **积木skill / 积木设计师** | 「流程」「SOP」「经验」「复盘」都算主语——"把这个流程变成 skill""把这次复盘沉淀下来"是最高频的真实开口，且**本版有经验蒸馏专属入口** |
| **V 动作槽** | 设计 · 做 · 建 · 写 · 变成 · 固化 · 沉淀 · 蒸馏 · 提炼 · 改进 · 优化 · 打分 · 体检 · 评估 · 出主意 · 拿个主意 · 想想办法 · **抄个思路 · 借鉴** | 「变成/固化/沉淀/蒸馏」是**转化类**动词，最容易漏——这些句子里根本没有"设计"二字 |
| **P 产物槽**（辅助） | 蓝图 · 方案 · 实施方案 · 设计方案 · 结构 · 目录 · SKILL.md | 出现 P 时，即便 S 弱（如"帮我想个方案"）也应结合上下文判为开工 |

**判定规则（按顺序短路）**：
1. 出现完整称呼「积木skill」「积木设计师」→ **无条件开工**
2. S + V 同时命中 → **开工**（按 V 的性质分流：设计/做/变成/固化/沉淀 → 新建；改进/优化 → 改进路由；打分/体检 → B09 质量门路由）
3. V + P 同时命中，且上下文是"做东西"而非"找东西" → **开工**
4. V 命中「沉淀/蒸馏/复盘」且 S 是「经验/这次跑通的」→ **开工，且走经验蒸馏入口**（[material-distill.md](material-distill.md)，不是从零创建）
5. 只命中 S，V 是「安装/推荐/找/搜索/管理」→ **不触发**（交给 find-skills 类）
6. 只叫助手昵称「积木」而跟 skill 无关 → **不触发**

### 2.2 真实语料库（已落地 skill 的原始需求口径）

下表来自**真实走完四步施工流并落地**的项目，可当作"这句话算不算叫我"的判例。
⚠️ 语料已做匿名化与口语化还原，**不作为需求内容引用**，只用作触发判定参考。

**通用语料（10 条）**

| 真实开口（口语化还原） | 命中槽位 | 判定 | 落地出处 |
|---|---|---|---|
| 「我想做个个人投资者工作台，界面简洁点」 | S(工作流) + V(做) | ✅ 新建 | `investor-workbench` |
| 「帮我把每周的汇总做成带可视化周报的自动化」 | S(流程) + V(做成) | ✅ 新建 | `personal-workbench` |
| 「我是基金经理，每天要读大量财经信息，想让它自动分类排序归档」 | S(流程) + V(自动…归档) | ✅ 新建 | `fin-information-pipeline` |
| 「读书笔记整理成结构化卡片，还要能主题检索和定期回顾」 | S(流程) + V(整理成) | ✅ 新建 | 对照实验 baseline |
| 「设计一个信息收集情报员」 | S + V(设计) | ✅ 新建 | `info-collector` |
| 「帮我把这个量能分析的方法固化下来」 | S(方法) + V(固化) | ✅ 新建（转化类，无"设计"二字） | `stock-volume-12step-analysis` |
| 「尽调时每次都要列资料清单，能不能自动生成」 | S(流程) + V(生成) | ✅ 新建 | `dd-checklist-generator` |
| 「我想把这次故障复盘的经验蒸馏成一个 skill」 | S(skill) + V(蒸馏成) | ✅ 新建（转化类典型） | `lovstudio-skill-distiller` |
| 「把这个每日晨报流程变成一个技能」 | S(流程) + V(变成) + P(技能) | ✅ 新建 | 工作流固化类通例 |
| 「帮我想个主意，这事值不值得做成 skill」 | V(出主意) + P(主意) | ✅ 咨询（进 ①概念讨论，先做边界判定） | 边界决策树入口 |

**口语说法（5 条 · 无"设计/蓝图"术语的真实开口）**

| 真实开口 | 命中槽位 | 判定 | 说明 |
|---|---|---|---|
| 「帮我设计一个skill实施方案」 | S(skill) + V(设计) + P(方案) | ✅ 新建 | 直接点名产物「方案」 |
| 「我想设计一个skill蓝图」 | S + V(设计) + P(蓝图) | ✅ 新建 | 直接点名产物「蓝图」 |
| 「正式创建skill前给我出一下主意」 | S + V(出主意) | ✅ 咨询 | 「创建前」正是本 skill 的**设计期**定位 |
| 「把一个初步的任务想法变成一个skill」 | S(想法) + V(变成) + P(skill) | ✅ 新建 | 转化类动词典型 |
| 「我想把这个任务流程变成一个skill」 | S(流程) + V(变成) + P(skill) | ✅ 新建 | 无「设计」二字 |

**本版专属语料（12 条 · 对应本版独有入口）**

| 真实开口 | 命中槽位 | 判定 | 本版出口 |
|---|---|---|---|
| 「这次跑通了，沉淀一下」 | S(经验) + V(沉淀) | ✅ **经验蒸馏入口** | [material-distill.md](material-distill.md) 切经验单元 → 蒸馏五问 |
| 「把这段复盘做成 skill」 | S(复盘) + V(做成) | ✅ **经验蒸馏入口** | 同上；对象是一段经验（对象是现有 skill → skill-rebuild） |
| 「一次丢给你几份历史资料，帮我提炼出能复用的做法」 | S(资料) + V(提炼) | ✅ 经验蒸馏（多材料） | material-distill 批量切单元 |
| 「给我的 skill 打个分」 | S + V(打分) | ✅ **B09 质量门** | `check_blueprint.py` 机器算 IQS → BR-5 人工评 |
| 「体检一下这个 skill，哪里不合格」 | S + V(体检) | ✅ **B09 质量门** | trace-evaluation-guide §一–§四 |
| 「赶时间，半小时能出个方案吗」 | — | ✅ **轻量通道**（① 里问通道） | 压缩③、简化④，约 30 分钟 |
| 「有没有类似场景的设计经验可以参考」 | V(参考) | ✅ 注入条目库 | design-blocks-library（126 条）+ design-principles-library（DP） |
| 「这个 skill 目录该怎么搭」 | S + P(目录) | ✅ B07 选型 | [skill-archetypes.md](skill-archetypes.md) 7 套 + 决策树 |
| 「参考 XX 这个 skill 抄个思路」 | V(借鉴) | ✅ **借鉴路由** | 拆解交 skill-rebuild；回流走 `../example/design-blocks/README.md` 四步法 |
| 「B04 和 B05 是不是一回事」 | — | ✅ 术语陷阱 | [glossary-traps.md](glossary-traps.md) |
| 「帮我把蓝图/评分/结构同屏看一眼」 | P(蓝图) | ✅ 合成大图 | `visual_session.py` |
| 「准备发 SkillHub 了，帮我过一遍门禁」 | — | ✅ 发布门禁 | `sd_cli package`（validate→prepare_release→卫生扫描） |

### 2.3 边界：这些说法**不**归本 skill

| 说法 | 为什么不算 | 交给谁 |
|---|---|---|
| 「帮我装个 XX skill」 | V 是安装，不是设计 | `marketplace-skill-installer` / `find-skills` |
| 「有没有处理 PDF 的 skill」 | V 是找/发现 | `find-skills` |
| 「把这个 skill 的实现代码重写一遍」 | 改的是代码，不是设计 | `skill-rebuild` 类 |
| 「就这一次，帮我写个一次性脚本」 | 无复用价值 | 直接做，不设计 |
| 「讲讲 skill 设计的理论」 | 要理论，不要蓝图 | 本 skill 产蓝图不讲理论 |
| 「积木，帮我看招商银行」 | 只叫昵称，跟 skill 无关 | 对应领域 skill |
| 「帮我把这个 skill 的文件压缩打包」 | 是文件操作，不是设计 | 直接做 |

## 关联

- 高频 6 条路由 → SKILL.md §2；references 一级索引 → [README.md](README.md)
- 触发一等口令与判定口诀 → SKILL.md §0「照着说这句就能开始」
- 机器可验证证据 → `scripts/evals.json`（跑 `sd_cli evals`）；方法论条目 → **D-127（做法层）** / **DP-207（设计观层）**
