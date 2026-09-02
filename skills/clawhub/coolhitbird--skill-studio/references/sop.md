# Skill Create SOP

> 用 `skill-studio` 元技能创建或重构任何 skill 的标准作业流程。
> **开工先读本文件**。所有铁律、决策树、验收门槛都在这里。

---

## 0. 适用范围

| 入口 | 路径 |
|---|---|
| 新建 skill | 走完整 SOP（步骤 1→10） |
| 重构已有 skill | 跳过步骤 1-3，从步骤 4 **审计** 入口进 |
| 快速小补丁（修 description / 改 typo） | 跳过诊断，直接改 + 跑步骤 8 校验 |

---

## 0.5 Skill 与 Tool 的辨析（哲学层）

> **Tool 给 Agent 手和脚，Skill 给 Agent 工作习惯。**

| 概念 | 作用 | 例子 |
|---|---|---|
| Tool | Agent 可调用的动作 | 查文件、跑脚本、调 API、执行命令 |
| Skill | Agent 如何工作的协议 | 什么时候查、查完怎么判断、按什么模板返回、失败时是否停下问用户 |

### 一个好的 Skill 必答 4 问题

| 问题 | 对应位置 |
|---|---|
| 什么时候该用这个 Skill？ | description、metadata |
| Agent 应该按什么步骤做？ | SKILL.md 主体指令 |
| 做事需要哪些外部资料？ | references/、assets/、scripts/ |
| 怎样判断做完了、做对了？ | checklist、template、gate、score、用户确认 |

### 5种模式本质 = 控制 5 类不确定性

| 不确定性 | 失败模式 | 对应模式 |
|---|---|---|
| 知识不确定 | 幻觉 / 规范错误 | Tool Wrapper |
| 输出不确定 | 结构漂移 | Generator |
| 质量不确定 | 审查靠感觉 | Reviewer |
| 输入不确定 | 用户没说清就脑补 | Inversion |
| 流程不确定 | 跳过验收直接交作业 | Pipeline |

**设计 skill 的第一问不是"要不要 references/"，而是"我最想约束 Agent 的哪一种失控"。**

### Skill 的本质与运行机制

> **Skill 本质 = 元提示词（Meta-Prompt）+ RAG（检索增强生成）的封装包。** 不改基座大模型，只锁定"人设+思维链"+扩展"私有知识大脑"。

**配置三要素**：

| 要素 | 角色 | 关键约束 |
|---|---|---|
| Instructions（指令） | 灵魂 | 系统提示，定义角色/流程/输出格式 |
| Knowledge（知识库） | 记忆 | 向量化 Embedding，按需检索 |
| Examples（示例对话） | 对齐 | 2-3 组高质量"问-答"，比一万句"要简洁"管用 |

**运行机制四步**：用户提问 → Skill 激活（指令作为最高优先级 System Prompt 植入）→ 多路召回（知识库 + 原生知识）→ 合并生成。

**关键边界（避坑）**：

| # | 边界 | 后果 |
|---|---|---|
| 1 | 指令冲突时**指令优先于知识库** | 知识库全英文术语 + 指令"必须中文" → 输出中文 |
| 2 | 指令超长（>2000 字）挤占对话历史 | 长对话模型"失忆"，必须精简 |
| 3 | 知识库是**静态快照** | 业务规则变（价格表更新）必须重新上传覆盖，不自动同步 |
| 4 | 普通大模型/Agent 三硬伤 | 知识截止（不知 Claude Skill 新架构）/ 平台专有性（Anthropic 私有协议）/ 执行机制差异（不懂向量检索触发）→ **只能当草稿生成器，最终封装须回到官方 Creator 或本 SOP 流程** |

---

## 1. 核心铁律（违反必出事）

| # | 铁律 | 证据 |
|---|---|---|
| 1 | **自举**：skill-studio 自己必须符合它教别人的所有规范 | 清言两版"巨型 prompt 反巨型 prompt"是反面教材 |
| 2 | **强制力靠脚本不靠词汇** | "MUST reject" 类 prompt 措辞靠不住，模型会善意推定；只有 `validate.py` 真跑校验才是硬钳 |
| 3 | **description ≤ 80 字**（比官方 200 字更严） | metadata 常驻上下文预算 ~100 词，超长稀释触发判定 |
| 4 | **SKILL.md ≤ 500 行**，详节挪 `references/` | 某内部编排 skill 21.6KB ≈ 600+ 行是重灾区实证 |
| 5 | **设计哲学不进 SKILL.md** | 职责边界/诚实边界/为什么这么设计 → 挪 `references/architecture.md` |
| 6 | **铁律条目化**：1 行结论 + 1 行证据 | 某日常运营 skill 3.8KB 是好范本，某内部治理 skill 反例每条带半页解释 |
| 7 | **5种模式知识外置** | 每种模式独立 `references/pattern-*.md`，按诊断结果按需加载 |
| 8 | **真实素材优先**：反例用自己踩过的坑 | 不编造抽象反模式；某内部三件套、某社区运营私信模板被识破都可作为案例 |
| 9 | **专注**：一个 Skill 只解决一个特定可重复工作流，不要试图做所有事 | 多职责混淆触发判定，反例"既能写报告又能审代码" |
| 10 | **description 动词开头 + 关键词** | description 是路由条件不是简介；`Helps users write better code.` 没触发力，`Python code review checklist for security, style, type hints...` 才有 |
| 11 | **善用示例 > 抽象解释** | 具体输入输出示例比长篇大论有效 |
| 12 | **术语全文一致** | 同一概念全文同一术语，避免混用 |
| 13 | **面向 Agent 写作（agentskills.io 通用风格）**：祈使句、第三人称、不解释为什么、不寒暄 | "This skill should be used when..." > "You should use..." |
| 14 | **脚本强健**：含错误处理 + 关键数值注释说明 | `TIMEOUT=30 # seconds` 而非裸数字 |
| 15 | **给予恰当自由度**：开放任务高自由度（文本指导）/ 关键流程低自由度（精确脚本）防出错 | 风险分级，不一刀切 |

---

## 2. 5种模式快速决策表（核心）

> **不要从目录出发，从要控制的不确定性出发。**

| 你最担心的失控 | 大白话 | 推荐模式 | 关键结构 |
|---|---|---|---|
| Agent 不懂某个库/团队规范 | 怕它不懂规矩 | **Tool Wrapper** | `SKILL.md` + `references/` |
| 输出结构每次漂移 | 怕它写得没格式 | **Generator** | `SKILL.md` + `assets/template` |
| 审查结果靠感觉，不可复现 | 怕它审得没标准 | **Reviewer** | `SKILL.md` + `references/checklist` |
| 用户没说清，Agent 脑补 | 怕它没问清楚就开干 | **Inversion** | `SKILL.md`（分阶段访谈） |
| 任务必须按顺序，中间不能跳 | 怕它跳过过程直接交作业 | **Pipeline** | `SKILL.md`（带门槛步骤）+ `scripts/` |

### 组合规则（生产形态）

| 组合 | 场景 |
|---|---|
| Inversion + Generator | 先问清变量，再生成固定结构文档 |
| Tool Wrapper + Reviewer | 按团队规范审查代码 |
| Pipeline + Reviewer | 工作流最后做质量门槛 |
| Pipeline + Inversion + Generator | 先收集需求，再按流程生成正式交付物 |

### 典型生产流程（组合范例）

```
Inversion（先问清上下文）
  → Tool Wrapper（加载领域规范）
    → Generator（生成结构化产物）
      → Reviewer（按标准审查）
        → Pipeline Gate（用户确认后进入下一步）
```

这是"先问清→加载规范→生成→审查→门槛确认"的完整闭环，多数正式交付物 skill 走这条。

### 5种模式详述指向

> 每种模式的执行标准、目录骨架、CLI 用法详见 `references/pattern-*.md`，按诊断结果按需加载。本 SOP 只列决策表，不展开。

| 模式 | 详述文件 | 关键执行标准摘要 |
|---|---|---|
| Tool Wrapper | `references/pattern-tool-wrapper.md` | SKILL.md 是"索引+执行协议"非规则仓库；三好处：激活前上下文轻/规范更新不改主指令/同一协议换不同 reference 复用 |
| Generator | `references/pattern-generator.md` | 6步输出契约：加载风格指南→加载模板→检查缺失字段→补问必要信息→填充每部分→返回完整文档；风格（references/）与结构（assets/）分离 |
| Reviewer | `references/pattern-reviewer.md` | 证据4要素强制：**位置**+**严重程度**+**原因**+**影响/修复方案**（必要时给修正代码）；按 error/warning/info 分组 |
| Inversion | `references/pattern-inversion.md` | 阶段化访谈：复杂任务一问一答/轻量任务一次问3个关键问题/允许"不确定"用默认假设标记/复述已收集信息确认；**未答完不输出最终方案** |
| Pipeline | `references/pattern-pipeline.md` | 每步必含8要素：目标/输入/动作/输出/**通过条件**/失败时怎么办/是否需用户确认/需加载哪些资源；**无门槛=步骤列表非Pipeline** |

---

## 3. 完整工作流（新建 skill）

### 步骤 1 — 诊断访谈（Inversion 模式开场）

不要立即起草。先问用户 3-6 个关键问题，**一次一个**：

- **触发**：什么具体用户请求应该激活这个 skill？（关键词）
- **不确定性**：最大风险是哪一类？（参考决策表）
- **输入/输出**：必须严格定义的是什么？
- **失败兜底**：信息缺失/校验失败/脚本失败时怎么办？
- **门槛**：哪些步骤必须用户确认或质量通过？

**轻量路径**：单模式 + 模板 <50 行 → 跳过完整访谈，直接走步骤 4 快通道。

### 设计列表 11 项表（访谈的标准化输出工具）

> 以后不要从空白 SKILL.md 开始写。先填这张表。

| 设计项 | 要回答的问题 |
|---|---|
| Skill 名称 | 这个 Skill 的能力边界是什么？ |
| description | 用户怎么说时应该触发它？有哪些关键词？ |
| 输入 | Agent 必须拿到哪些信息才能开始？ |
| 输出 | 最终交付物长什么样？ |
| 工作协议 | Agent 应该按什么步骤做？ |
| references | 哪些规则、规范、检查清单应该外置？ |
| assets | 是否需要模板、示例、格式文件？ |
| scripts | 是否需要确定性校验、转换、生成脚本？ |
| gate | 哪些步骤必须用户确认或质量通过？ |
| 失败处理 | 信息缺失、检查失败、脚本失败时怎么办？ |
| 测试样例 | 什么请求应该触发？什么请求不该触发？ |

**填表铁律**：description 是"路由条件"不是"简介"，必须含领域+任务+关键词。反例 `Helps users write better code.` 没触发力；正例 `Python code review checklist for correctness, security, style, type hints, exception handling, and performance issues.`

### 步骤 2 — 模式选择（`diagnose.py` 辅助决策）

用决策树输出推荐模式 + 理由。**多模式命中时组合**，不要硬选一个。

```
输入：任务描述 + 不确定性回答
输出：{
  "primary_pattern": "Tool Wrapper | Generator | Reviewer | Inversion | Pipeline",
  "secondary_pattern": "可空",
  "uncertainty_type": "Knowledge | Output | Quality | Input | Process",
  "reason": "为什么选这个组合",
  "required_dirs": ["references/", "assets/", "scripts/"]
}
```

### 步骤 3 — 架构设计

根据模式决定目录布局：

| 模式 | 必含 | 可选 |
|---|---|---|
| Tool Wrapper | `references/`（规范外置） | — |
| Generator | `references/style-guide.md` + `assets/template.md` | — |
| Reviewer | `references/checklist.md` | — |
| Inversion | `assets/plan-template.md` | — |
| Pipeline | `references/*.md`（每步一份）+ `assets/template` | `scripts/`（校验/转换） |

**铁律**：`SKILL.md` 是"索引 + 执行协议"，不是"规则仓库"。

### 步骤 4 — 起草

```bash
# 调用现有 skill-studio 的 init 脚本生成骨架
scripts/init_skill.py <skill-name> [--path <output-directory>]
```

编辑顺序：
1. 先写 `references/` / `assets/` / `scripts/`（可复用资源）
2. 再写 `SKILL.md`（编排 + 索引）
3. 删掉 init 生成的示例文件（不需要的）

**写作风格**：祈使句、第三人称、不解释为什么、不寒暄。
**示例优先**：具体输入输出示例 > 长篇抽象解释。

### 步骤 5 — 自检清单（人工对照）

- [ ] `description` ≤ 80 字？含触发关键词？
- [ ] SKILL.md ≤ 500 行？
- [ ] 设计哲学挪到 `references/architecture.md`？
- [ ] 铁律条目化（1 行结论 + 1 行证据）？
- [ ] 5 种模式知识外置到 `references/pattern-*.md`？
- [ ] 脚本含错误处理？关键数值有注释说明？
- [ ] 术语全文一致？

### 步骤 6 — 自动校验（`validate.py` 硬钳）

```bash
scripts/validate.py <skill-folder>
```

校验项：
- YAML frontmatter 格式 + 必填字段（`name`、`description`、`agent_created: true`）
- `name` 命名规则（小写/数字/连字符/≤64 字符/与目录同名/无保留词）
  - **保留词黑名单**：`anthropic`、`claude`、`codebuddy`、`workbuddy` 等品牌词
- `description` 字符数（≤80 字，比官方更严）+ 动词开头校验 + 关键词密度
- `dependencies` 字段（如声明 Python 依赖，校验格式与可解析性）
- SKILL.md 行数（≤500 行警告，>600 行拒出包）
- `references/` 是否被引用（避免建了不用）
- 脚本语法快速 lint
- **skilllint 对标**（如可用）：自动检查格式，与 validate.py 互补

**FAIL 即拒出包**，不靠 prompt 措辞"善意放行"。

### 熔断机制（防御性编程）

> 防止生成的 skill 自己变成"大 Prompt"或"骚扰器"，三道硬熔断：

| # | 熔断 | 触发条件 | 动作 |
|---|---|---|---|
| 1 | **SKILL.md 行数红线** | >500 行警告 / >600 行 | 强制报错，要求拆 `references/` |
| 2 | **description 强制公式** | 缺"当用户提及[关键词1]、[关键词2]或[场景]时使用"结构 | 校验不通过，要求重写 |
| 3 | **Pipeline Gate 硬编码** | Pipeline 模式步骤缺 `if not user_confirmed: stop` 等门槛逻辑 | 无法打包 |
| 4 | **Inversion 防骚扰上限** | 连续提问 >6 个未给假设出口 | 强制生成"假设条件"让用户确认，防用户流失 |

### 步骤 7 — 打包

```bash
scripts/package_skill.py <skill-folder> [output-dir] [--target <host|all>]
```

自动跑步骤 6 校验，通过后生成 `<skill-name>.zip`。跨 Agent 分发加 `--target`（claude/copilot/codex/openclaw/cursor/gemini/hermes/coze/workbuddy 或 `all`），机制与宿主目录详见 `docs/07-cross-agent-compatibility.md`。

### 步骤 8 — dogfood 测试

用真实场景跑一遍：
- 触发测试：相关查询能不能被自动触发？目标 ≥90% 命中率
- 多模型测试：Haiku / Sonnet / Opus 表现稳定性
- 反触发测试：不相关查询不该触发（防误激活）

### 步骤 9 — 落地安装

```bash
# 用户级（跨项目可用，默认）
cp -r <skill-folder> ~/.workbuddy/skills/

# 项目级（团队共享，需明确意图）
cp -r <skill-folder> <project>/.workbuddy/skills/
```

### 步骤 10 — 迭代

1. 用真实任务跑
2. 发现挣扎/低效
3. 改 SKILL.md 或 references，**不要回头改脚本除非确有 bug**
4. 重跑步骤 6 + 8
5. 沉淀经验到 `~/.workbuddy/MEMORY.md` 或新建一个 skill

---

## 4. 重构已有 skill（审计入口）

跳过步骤 1-3，从审计开始：

### 步骤 4' — 审计（`audit.py`）

```bash
scripts/audit.py <skill-folder>
```

输出诊断表：

| 检查项 | 阈值 | 实测 | 建议动作 |
|---|---|---|---|
| SKILL.md 行数 | ≤500 行 | _实测_ | 拆 `references/` |
| description 字符数 | ≤80 字 | _实测_ | 砍到 ≤80 字 |
| references/ 是否使用 | 必用 | _实测_ | 必建/挪详节 |
| 设计哲学混入 | 0 | _实测_ | 挪 `references/architecture.md` |
| 铁律条目化 | 1 行结论 | _实测_ | 改 1 行 + 1 行证据 |
| 跨 skill 资产耦合 manifest | 有 | _实测_ | 加 `references/dependencies.md` |

**实测对照（方法论，不暴露本地路径）**：

> 具体本地 skill 的实测数据属于安全资产，不写入可分发的 SOP。审计时由 `audit.py` 跑出当前 skill 的实测值填入上表"实测"列。

| 维度 | 警戒 | 重灾 | 动作 |
|---|---|---|---|
| SKILL.md 体积 | >8 KB | >15 KB | 拆 `references/` |
| references/ 使用率 | 建了不用 | 未建且 SKILL.md >8KB | 必建/挪详节 |
| 铁律条目化密度 | 每条 >3 行 | 每条带半页解释 | 改 1 行结论 + 1 行证据 |
| 跨 skill 耦合 manifest | 互引"须同目录" | 无共享 references | 加 `references/dependencies.md` |

### 步骤 5'-10' — 同新建流程

按审计建议改完后，跑步骤 5 自检 → 步骤 6 校验 → 步骤 8 dogfood。

---

## 5. 反模式清单（实证，不编造）

| # | 反模式 | 实证来源 | 后果 |
|---|---|---|---|
| 1 | **巨型 Prompt**：SKILL.md 塞所有规则/模板/示例/检查清单 | 某内部编排 skill 21.6KB | 失去 Skill 意义，每次触发全量灌上下文 |
| 2 | **模糊 description** | "Helps users write better code." 类 | 没触发力，路由失败 |
| 3 | **无门槛 Pipeline**：只有 Step 1/2/3，没有通过条件 | — | 不是 Pipeline，是步骤列表 |
| 4 | **Reviewer 无证据要求** | — | 输出泛泛而谈的建议 |
| 5 | **Inversion 一次问太多** | — | 用户直接关掉 |
| 6 | **设计哲学混入操作指南** | 某内部 skill "职责边界/诚实边界" | 主控 agent 在"为什么"里找"现在敲哪条命令" |
| 7 | **铁律与解释同段堆叠** | 某内部 skill 每条铁律带半页 justification | 命令查找要滚屏 |
| 8 | **CLI 全量写 SKILL.md** | 某内部编排 skill | 修改一次命令要同步改主文档 |
| 9 | **跨 skill 耦合无 manifest** | 某内部三件套互引"某内部 runtime.py 须同目录" | 新会话触发任一 skill 看不到全景 |
| 10 | **自举失败**：教别人不要做的事自己做了 | 清言两版 skill-studio 草稿 | 元技能丧失权威 |
| 11 | **外部 Skill 不审查就加载** | 第三方 skill 可能含恶意指令/资源/脚本 | 引入前审查 SKILL.md + 资源文件 + 脚本，防 prompt injection 和权限越权 |

---

## 6. 验收门槛（skill 可发布的标准）

| 门槛 | 阈值 | 检查方式 |
|---|---|---|
| 硬性规范全过 | 100% | `validate.py` 退出码 0 |
| 触发率 | ≥90% | dogfood 相关查询命中率 |
| 误触发率 | ≤5% | dogfood 不相关查询命中率 |
| SKILL.md 精简 | ≤500 行 | `wc -l` |
| description 精准 | ≤80 字 + 含关键词 | `validate.py` |
| references 外置 | 详节已挪 | 人工对照 |
| 反模式自查 | 0 命中 | 对照第 5 节清单 |
| dogfood 通过 | 真实场景跑通 | 人工签字 |

---

## 7. 与现有 skill-creator（marketplace 版）的衔接

| 现有 | 本 SOP 增量 |
|---|---|
| `init_skill.py`（生成骨架） | 保留 |
| `package_skill.py`（打包） | 保留 |
| 格式钳靠 prompt 措辞 | 改为 `validate.py` 真校验 |
| 无诊断决策树 | 新增 `diagnose.py` |
| 无审计能力 | 新增 `audit.py` |
| 无 5种模式知识 | 新增 `references/pattern-*.md` |
| 无反例实证 | 新增 `references/anti-patterns.md`（脱敏） |

最终元技能结构（目标）：

```
~/.workbuddy/skills/skill-studio/
├── SKILL.md                          # ≤8KB，只做编排+索引
├── references/
│   ├── pattern-tool-wrapper.md
│   ├── pattern-generator.md
│   ├── pattern-reviewer.md
│   ├── pattern-inversion.md
│   ├── pattern-pipeline.md
│   ├── architecture.md               # 设计哲学/诚实边界（铁律#5 外置）
│   └── anti-patterns.md              # 第 5 节实证清单（脱敏，不暴露本地路径）
├── assets/
│   ├── skill-template/                # init 复制骨架
│   └── design-checklist.md            # 步骤 5 自检表
└── scripts/
    ├── init_skill.py                  # 保留
    ├── diagnose.py                    # 新增：模式决策树
    ├── validate.py                     # 新增：硬钳校验
    ├── audit.py                        # 新增：已有 skill 病灶诊断
    └── package_skill.py                # 保留
```

### 实现路线选择（四路线）

| 路线 | 适用 | 优势 | 代表 |
|---|---|---|---|
| **直接用/二次开发现有工具** | 最快上手 | 站在巨人肩膀 | skillseed（Python，触发校验+经验日志自我进化）/ skill-builder（英文描述→生产就绪，一键装20+AI工具）/ agent-skill-creator（PDF/链接输入，跨17平台，内置验证+安全扫描）/ skill-forge（规划→构建→审查→进化→发布全生命周期） |
| **自建元技能**（本 SOP 主路线） | AI-native 最优雅 | 创建流程本身固化为 Skill | Inversion 模式开场 + Pipeline 分阶段 + references/ 存规范 + `validate.py` 自动校验 |
| **独立 CLI 工具** | 最大控制权，不依赖模型 | 确定性极高 | 官方多 TypeScript/Node.js 或 Go；社区有 Python；核心模块：初始化器/验证器/打包器/（可选）评估器 |
| **基于库/框架** | 加速开发 | 复用现成能力 | Go: GoSkills；Node.js: `@skillbase/compiler`（跨格式编译）/`@reaatech/agents-markdown-scaffold`（模板生成）；MCP: 基于 MCP Server 架构包装为标准协议服务 |

**本 SOP 默认走"自建元技能"路线**，与 marketplace 版 skill-creator 衔接见上表。

### 如何把本 SOP 转为设计文档

本 SOP 是"作业流程"，若要写正式设计文档（DESIGN.md），按此结构映射：

| 设计文档章节 | SOP 对应节 |
|---|---|
| 1. 项目背景与目标 | 第 0 节适用范围 + 第 0.5 节哲学层痛点 |
| 2. 核心设计原则 | 第 1 节铁律 + 第 0.5 节本质/运行机制 |
| 3. 功能需求 | 第 3 节工作流 10 步 + 第 6 步熔断 |
| 4. 系统架构 | 第 7 节最终元技能结构 + 实现路线 |
| 5. 关键设计细节（熔断） | 第 6 步熔断机制 |
| 6. Roadmap | 第 8 节改进路线图 |

---

## 8. 改进路线图（按 ROI 排序）

| 阶段 | 动作 | 收益 | 成本 |
|---|---|---|---|
| P0 | 把本 SOP 落地为 `skill-studio` 的 `references/sop.md` | 让 SOP 自身可被加载 | 低 |
| P0 | 写 `validate.py` 硬钳脚本 | 强制力从词汇升级到机制 | 中 |
| P1 | 写 `diagnose.py` 决策树 | 模式选择从感觉升级到确定性 | 中 |
| P1 | 拆 5 份 `pattern-*.md` references | 渐进式披露真正落地 | 中 |
| P2 | 写 `audit.py` 审计工具 | 衔接已有 skill 重构 | 中 |
| P3 | dogfood：用本元技能重构已有本地 skill | 验证元技能自身 | 高 |

### 四阶段 Roadmap（细化）

| Phase | 动作 | 产出 |
|---|---|---|
| Phase 1 | 完成本 SOP 落地为 `references/sop.md` + 基础模板库（Jinja2） | 设计基线 + 模板骨架 |
| Phase 2 | 开发 CLI 核心引擎（支持单模式生成：Generator/Reviewer 优先，因 assets/checklist 最易抽象） | `init_skill.py` + `validate.py` + 单模式生成器 |
| Phase 3 | 接入 LLM 实现"智能模式匹配"（根据用户描述自动推荐 Pattern） | `diagnose.py` 决策树 |
| Phase 4 | 开发 VS Code 插件或 Web UI，实现可视化编排 | 可视化创作工具 |
