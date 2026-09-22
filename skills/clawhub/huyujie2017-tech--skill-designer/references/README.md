---
加载条件: SKILL.md 导航指向 references/ 时——agent **先读本索引**，按当前意图匹配「加载条件」「标签」再决定加载哪份全文；⛔ 禁止盲目全量加载。
核心主题: references 一级/二级索引、加载决策树、防误召回提示、维护纪律
命中标签: [索引, 检索, 路由, 防误召回, 维护纪律, progressive disclosure]
不回答: 具体方法论内容（见各分册）；SKILL.md 层的意图路由
---

# References 机器索引

> **给谁读**：本文件首先给 **agent** 读。当 SKILL.md 的导航表指向 references/ 时，agent 应先读本索引，根据当前意图匹配「加载条件」和「标签」，再决定是否加载某份 reference 全文。
>
> **不给谁读**：普通用户不需要读本文件。用户**不需要先读任何文档**——本 skill 是元 skill，直接开口即可；[`quickstart.md`](quickstart.md) 只是「零技术门槛启动卡 + FAQ 速查」，非必读前置。
>
> **设计目标**：用一份轻量索引（约 120 行）替代对 20 份顶层 reference + 10 份 blocks 分片的盲目全量加载，降低 token 消耗和误召回。
>
> **每份 reference 头部都有 YAML frontmatter**（`加载条件` / `核心主题` / `命中标签` / `不回答`），与下表口径一致——**以文件头为准，本表为速查**；两者冲突时改本表并同步文件头。
>
> **两级入口（新增，引用键 = 条目 ID）**：本表是**文件级**入口（决定「该开哪一份」，路径即加载入口）；要找**某一条**知识（147 条 D / 17 条 DP / 12 条 L 里的某一两条），走**条目级**入口——`sd_cli knowledge search --block B07 --text 路由` 拿 ID，再 `sd_cli knowledge get D-065` 取正文。条目粒度索引在 `scripts/library_manifest.json`（机器件，**不进上下文**）。**引用一律写 ID**（`D-NNN` / `DP-XXX` / `L-NN`）：条目在库内怎么重组分片，引用都不会断（DP-209 权威源唯一化）。

---

## 一级索引：文件速查表

| 文件 | 一句话摘要 | 典型加载条件 | 关键词标签 | 体量 |
|------|-----------|-------------|-----------|------|
| [`four-step-flow.md`](four-step-flow.md) | **四步施工流门面层（默认用户体验）**：把意图路由 + 主流水线封装成"出方案积木"，用户只看到 ①概念讨论 → ②初步方案 → ③深化设计 → ④施工蓝图；含概念讨论最低标准 + 开场描述喂格映射 | 进入创建/改进 skill 的蓝图引导（**默认路径**）时；问"为什么步骤这么少 / 内部怎么跑"时 | 四步, 施工流, 门面, 体验, 概念讨论, 初步方案, 深化设计, 施工蓝图, 封装, facade, 喂格 | 218 行 / ~5125 词 |
| [`material-distill.md`](material-distill.md) | **经验蒸馏入口（①概念讨论的前置子流程）**：带已验证经验来时——切经验单元（一份材料 3–7 个）→ 蒸馏五问（定价值与不变量）→ 提升决策四结论（创建/继续蒸馏/合并/归档）→ 证据脱敏写入 01-条件「证据来源」。**对象是一段经验**（对象是一个现有 skill → 交给 skill-rebuild） | 用户带复盘/历史资料、说"把这次经历沉淀成 skill"；①概念讨论判定资料含多个闭环时 | 经验蒸馏, 给料, 历史资料, materials, 单元切分, 提升决策, 证据脱敏, C10 | 118 行 / ~2090 词 |
| [`glossary-traps.md`](glossary-traps.md) | **术语陷阱速查（认知盲区索引）**：先给可推断的命名规律（省查表），再单列**不可推断**清单——积木格名≠格内容、蓝图两套骨架、IQS/EVS/BR-5/TRACE 三套评分、条目库与原则库的分层 | 拿不准编号 / 文件归属 / "这两个是不是一回事"时；写蓝图要引用积木格或评分体系时 | 术语, 易混, 编号, 积木格, 评分体系, 骨架, 陷阱 | 88 行 / ~1639 词 |
| [`design-blocks-library.md`](design-blocks-library.md) | **设计条目总库（单一权威源 · 147 条 D-NNN）**：**双索引视图**（按积木格 B01–B10 / 按主题 T1–T10）+ 条目速查 + 标签体系 + 旧编号映射；**条目正文按格分片**在 `blocks/design-blocks-b01…b10.md` | 引导到某一格时按格命中；或 B02/B03/B06 产出画像/模式/决策标签后命中；注入 TOP 2 | 设计条目, 积木盘点, B0X 注入, 最佳实践, 设计模式, 工程纪律, 常见病症, 条目库 | 344 行 / ~6749 词 |
| [`design-principles-library.md`](design-principles-library.md) | **设计原则库（设计观层 · DP 条目）**：原则概述 + 适用场景 + 落地要点 + 证据链；准入三判据 + ② 设计观注入 + B09 检查表 + 蓝图回填引用追踪 | ② 初步方案出稿前按任务标签命中注入 TOP 2–3；B09 评审当检查表；新增 DP 条目时 | 设计原则, 元设计, 设计观, DP 条目, 注入, **有限资源分层** | 192 行 / ~8935 词 |
| [`quickstart.md`](quickstart.md) | **零技术门槛启动卡（非必读前置）**：60 秒速览 + 零技术门槛三件事 + 3 步上手 + 积木链速览 + 2 案例 + **FAQ 常见 13 问速查** | 问"怎么用 / 从哪开始 / 要装什么吗"；**想快速查 FAQ 时** | 入门, 快速开始, **FAQ**, 速查, 零技术门槛 | 92 行 / ~1901 词 |
| [`skill-archetypes.md`](skill-archetypes.md) | 7 套 skill 结构框架范例（minimal/pipeline/tool/knowledge/template/full/suite）+ 选型决策树 + 每节点内容要点 | **B07 画目录骨架时**；问"目录里该有什么 / references 与 assets 怎么分" | 结构框架, archetype, 目录骨架, B07, 施工图, suite, tool 专项字段 | 266 行 / ~4745 词 |
| [`designer-guide.md`](designer-guide.md) | **10 格话术分册入口（通用协议层）**：引导协议（每轮节奏 / AUTO-REQUIRED / 强制阻塞）+ 分册加载规则 + 拼装定位 | 进入创建/改进 skill 的引导对话时**先读它**，再按格进 A/B 分册 | 引导, 协议, 入口, B01-B10, 分册 | ~85 行 |
| [`designer-guide-A.md`](designer-guide-A.md) | **前半程逐格问题库**：Phase 0 三问 + 探链六问 + 写法策略 + B01 该不该做 → B06 方案抉择（含每格开场/收尾话术与「拼完能决定什么」） | 引导进入 Phase 0 / B01–B06 逐格时（先过 designer-guide.md 协议层） | 引导, 话术, B01, B02, B03, B04, B05, B06, Phase 0 | ~175 行 |
| [`designer-guide-B.md`](designer-guide-B.md) | **后半程逐格问题库 + 支撑节**：B07 施工图 → B10 复盘 + description 五件事 / 输出四要素 / 改进诊断 / AUTO-REQUIRED 决策表 / 交接落地 | 引导进入 B07–B10 或需要决策表 / 交接 / 诊断分支时（先过 designer-guide.md 协议层） | 引导, 话术, B07, B08, B09, B10, 决策表, 交接, 诊断 | ~240 行 |
| [`router-full.md`](router-full.md) | **长尾意图路由表（SKILL.md §2 下沉层）**：交接 / skill-creator 把关 / 术语 / 评测口径 / 返评 / 可视化 / 案例 / 复盘 / 恢复 / 工程 / 诊断 / 方法论 18 条低频路由 | SKILL.md 高频 6 条未命中、意图属长尾时查本表 | 路由, 长尾, 交接, 返评, 术语, 案例, 结构图, 复盘, 工程, 诊断 | ~35 行 |
| [`blueprint-template.md`](blueprint-template.md) | 10 张可填积木模板 + Excel 报表 skill 完整示例 | 需要查看/填写蓝图模板、或 init 后告诉用户怎么填空时 | 模板, 蓝图填写, 示例, 分发与安装 | 484 行 / ~8095 词 |
| [`test-playbook.md`](test-playbook.md) | 测试打磨剧本：触发测试 + 效果测试 + 性能对比 | B08 行动 / B09 结果 / 进入闭环验证时 | 测试, 验证, 打磨, BUG_LOG | 349 行 / ~5488 词 |
| [`capability-boundary.md`](capability-boundary.md) | 能力边界专页：做/不做/交别人做 + 20 场景正反例 | 用户拿不准本 skill 管什么、或问"这个场景能不能用"时 | 边界, 路由, 决策树 | 108 行 / ~1803 词 |
| [`flow-recovery.md`](flow-recovery.md) | 流程恢复协议：checkpoint + 断点续跑 + 卡壳恢复 | 主流水线卡壳、跑偏、会话中断恢复时 | 恢复, checkpoint, 状态机 | 94 行 / ~1438 词 |
| [`blueprint-methodology.md`](blueprint-methodology.md) | 积木哲学 × 技能蓝图方法论底座 | 问"为什么这么引导"、核心原则、方法论依据时 | 方法论, 世界观, 积木链 | 248 行 / ~5101 词 |
| [`high-quality-skill-principle.md`](high-quality-skill-principle.md) | 高质量 Skill 核心原则摘要（P1–P40） | 需要原则速查、判断"这条设计对不对"时 | 原则, 速查, 质量门 | 215 行 / ~5005 词 |
| [`engineering-practices.md`](engineering-practices.md) | 工程级 Skill 实践：frontmatter / 脚本 / 隔离 / 作用域 | 问 frontmatter / 脚本封装 / 模块隔离 / 作用域 / 拆文件时 | 工程, frontmatter, 脚本, 隔离 | 375 行 / ~7696 词 |
| [`fix-toolbox.md`](fix-toolbox.md) | 9 反模式 + 9 错误场景的可执行修复产物 + **Part 3 错误码 → 一句话动作（E001–E007）** | 打磨 / 诊断 / 问"我的 skill 哪里不对、怎么改"时；**脚本报错时查错误码** | 修复, 反模式, 诊断, **错误码** | 172 行 / ~3388 词 |
| [`lessons.md`](lessons.md) | **跨任务经验库（B10 晋升入口）**：已晋升的通用规则条目库（触发格/信号/证据/引用计数），新任务 Phase 0 后注入 TOP 3 | B10 复盘晋升时写入；新任务开工按触发格命中时注入 | 经验库, 复盘, 晋升, B10, 注入, 跨任务, 分型粒度, 存活度, 运行期 | 132 行 / ~4945 词 |
| [`trace-evaluation-guide.md`](trace-evaluation-guide.md) | **五维质量门双口径**：BR-5 蓝图就绪度（设计期，B09 主用）+ SkillHub TRACE 自查（发布期） | **B09 质量门评分时**；准备发布 / 对照官方评分标准自查 / **收到外部返评后生成补丁清单**时 | **BR-5**, 蓝图就绪度, **B09**, TRACE, 评测, 质量门, 发布前检查, 返评, 补丁 | 216 行 / ~3831 词 |

---

## 二级索引：标签 → 文件

按常见意图快速定位：

| 标签 | 优先加载文件 |
|------|-------------|
| **四步施工流（默认体验）** | four-step-flow.md（门面层）→ 按步内联 designer-guide / flow-recovery / capability-boundary / trace-evaluation-guide |
| **新手起步** | quickstart.md（可选，用户可直接开口）→ designer-guide.md（协议层）→ 按格进 A/B 分册 → blueprint-template.md |
| **引导对话中** | designer-guide.md（协议层）→ designer-guide-A.md（B01–B06）/ designer-guide-B.md（B07–B10）→ design-blocks-library.md（按格 / 按标签命中）→ design-principles-library.md（设计观）|
| **B07 画目录 / 选结构** | skill-archetypes.md → render_structure.py（出结构图） |
| **B09 质量门（设计期）** | trace-evaluation-guide.md §一–§四（BR-5 五维）→ check_blueprint.py（机器报缺口）→ b09_summary.py（出图） |
| **测试验收** | test-playbook.md → fix-toolbox.md → trace-evaluation-guide.md（E 维） |
| **边界判断** | capability-boundary.md |
| **中断恢复** | flow-recovery.md |
| **方法论/原则** | blueprint-methodology.md → high-quality-skill-principle.md |
| **工程实现** | engineering-practices.md → design-blocks-library.md（工程条目 D-009 / D-061 / D-095 / D-096 / D-097 / D-116） |
| **诊断修复** | fix-toolbox.md → test-playbook.md → design-blocks-library.md（常见病症库）|
| **复盘晋升 / 跨任务规则** | lessons.md（B10 收尾晋升；新任务 Phase 0 注入 TOP 3） |
| **发布前自查 / 冲高分（发布期）** | trace-evaluation-guide.md §五–§六 → test-playbook.md → fix-toolbox.md |

---

## 加载决策树

```
用户意图
  │
  ├─ If 进入四步施工流（默认蓝图体验）→ four-step-flow.md（门面层）→ 按步内联对应 reference
  ├─ If 问怎么用 / 从哪开始 / FAQ → quickstart.md
  ├─ If 进入 B01–B06 引导（含 Phase 0 / 六问 / 写法策略）→ designer-guide.md（协议层）→ designer-guide-A.md
  ├─ If 进入 B07–B10 引导 / 需要决策表 / 交接 / 诊断 → designer-guide.md（协议层）→ designer-guide-B.md
  ├─ If 需要模板或填写示例 → blueprint-template.md
  ├─ If B07 画目录 / 选结构框架 → skill-archetypes.md + render_structure.py
  ├─ If 命中具体条目（按标签 / 按格）→ design-blocks-library.md → blocks/design-blocks-bXX.md（分片）
  ├─ If B09 质量门 / 给蓝图打分 → trace-evaluation-guide.md §一–§四（BR-5 设计期口径）
  ├─ If 进入测试 / 验收阶段 → test-playbook.md
  ├─ If 问能不能用 / 边界 → capability-boundary.md
  ├─ If 长尾意图（交接 / 返评 / 可视化 / 结构图 / 工程 / 修复 / 方法论等）→ router-full.md 先路由
  ├─ If 卡壳 / 中断 / 恢复 → flow-recovery.md
  ├─ If 问为什么 / 核心原则 → blueprint-methodology.md / high-quality-skill-principle.md
  ├─ If 问工程实现 / frontmatter → engineering-practices.md
  └─ If 发布前自查 / 冲高分（成品）→ trace-evaluation-guide.md §五–§六（TRACE 发布期口径）
```

---

## 防误召回提示

- **four-step-flow.md 是门面层，不是逐格话术库**：它定义"用户看到哪四步"，不回答"某格具体怎么问"（那是 designer-guide.md）；逐格深挖时不要反复整篇加载它。
- **quickstart.md 不是必读前置**：用户可以直接开口说需求，不必先读它。只在用户主动问"怎么用/要装什么吗"或查 FAQ 时才加载；引导过程中不应频繁加载。
- **skill-archetypes.md 只在 B07 用**：它回答"目录长什么样"，不回答"每格问什么"（那是 designer-guide.md）。
- **blueprint-methodology.md 不是操作手册**：它回答"为什么"，不回答"这一步具体怎么问"。操作细节在 designer-guide.md。
- **engineering-practices.md 不是安全审查主场**：它讲"工具隔离 / 接口白名单"，OWASP 安全审查在 test-playbook.md §八。
- **high-quality-skill-principle.md 是速查层**：需要完整话术时去 designer-guide.md，不要在本文件里找逐格问题。
- **trace-evaluation-guide.md 有两套口径，别用错**：B09 评蓝图用 **§一–§四 BR-5 设计期**（问"约定了吗"）；只有发布前自查或收到平台返评才用 **§五–§六 TRACE 发布期**（问"做到了吗"）。本 skill 是设计指南，**默认走设计期**。

---

## 维护纪律

1. 新增 reference 必须在本表登记，否则视为孤儿引用（`references/blocks/` 下的分片由 `design-blocks-library.md` 索引登记，且分片文件名须在 SKILL.md 出现一次，否则 validate 第 8 项报孤儿）。
   **例外（v3.18.0）**：`design-blocks-library.md`、`design-principles-library.md`、`lessons.md`、`blocks/design-blocks-b01~b10.md` 共 **13 份是生成物**（头部有 `<!-- GENERATED by compile_library.py … -->`），**禁止手改**；它们由 `library/*.json` 经 `python scripts/compile_library.py --write` 渲染，`knowledge verify` 的 **C5** 逐字节把关。
2. 修改某 reference 的「加载条件」或「标签」时，必须同步更新本表和该文件头部的加载条件段落。
3. 本文件体积应控制在 150 行以内；若 reference 增加导致膨胀，改为按标签分片索引。
4. **改完条目必跑两步**（v3.18.0+）：先 `python scripts/compile_library.py --write`（权威源 → 全部 md 视图）→ 再 `python scripts/sd_cli.py knowledge index --write` 重建条目索引 → `sd_cli knowledge verify` 机器核对 C0–C5（索引↔权威源指纹 / ID 编号连续 / 条目库四方一致 / **生成物逐字节等于渲染结果**）。**md 与索引都是派生件，只改权威源不同步 = 派生件撒谎**（报 E009/E013 熔断）。
