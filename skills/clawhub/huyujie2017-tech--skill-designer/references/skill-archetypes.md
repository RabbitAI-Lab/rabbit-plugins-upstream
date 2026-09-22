---
加载条件: 进入 B07 计划积木画目录骨架时；用户问"目录里该有什么 / 该放几个文件 / references 和 assets 怎么分"时。
核心主题: 7 套典型目录骨架范例（archetype）——先选型，再把 B07 的实际内容填进去。
命中标签: [结构框架, archetype, 目录骨架, B07, 施工图, 可视化]
不回答: 不回答逐格引导问题（见 designer-guide.md）；不回答 frontmatter 字段（见 engineering-practices.md）。
---

# Skill 结构框架范例库（B07 施工图选型用）

> 用法三步：**① 选型**（看下面决策表，或让设计师按 B03 模式推荐）→ **② 填内容**（B07 的目录骨架 / 五段骨架 / 资源分配）→ **③ 出图**
> `python scripts/sd_cli.py structure <蓝图目录> -o structure.svg`（`--format md` 出文本树，`--list` 看全部框架）
> 机器数据源是 `scripts/archetypes.json`（单一数据源，改它必须跑 `validate --self`）。

---

## 〇、设计模式 → 结构框架 映射矩阵（B03 → B07 的固化桥梁）

> **为什么**：B03 选了内容模式（A–F）× 交互模式（SCK），B07 选 archetype——中间这段**靠设计师临场判断**。本矩阵把它固化成可查表：B03 定完模式，B07 直接查表得推荐结构，再配依据。**查表是起点，用户仍可拍板调整。**

| 内容模式 (A–F) | 交互模式 (SCK) | 推荐 archetype | 五段骨架侧重（该结构最值钱的一段） |
|---|---|---|---|
| **A 流程配方** | Pipeline | pipeline / full | Workflow 写**决策树 + checkpoint**（分支明确、步骤带中间确认） |
| **B 领域知识包** | Inversion | knowledge | Resource Routing 写**强路由表**（references 是主体，`If…load…before…`） |
| **C 工具编排** | Tool Wrapper | tool | Failure Handling 写**四状态 + 重试/降级**（超时、限流、鉴权、部分成功）；**Resource Routing 写命令/接口速查表**（◎v3.7.0 专项，见 二·3） |
| **D 模板渲染** | Generator | template | Validation 写 **schema 校验** + **错误输出**（失败也产文件） |
| **E 带自检** | Reviewer | minimal / pipeline + 自检 | Validation 写 **golden checklist + 抽检回路**（评审/纠错类） |
| **F 技能组合** | Pipeline | full（router） | Workflow 写**意图路由表** + 多 skill 仲裁（冲突仲裁五序） |
| **多子域套件** | Pipeline / 混合 | **suite** | SKILL.md 写**结构化场景路由契约**（信号/首读/禁读/动作前检查/常见错误） |

> 组合信号：A+E → pipeline（Workflow 决策树 + Validation golden）；C+E → tool + 自检（失败路径 + 校验回路）；B+F → full（knowledge 主体 + 路由）。**查表给起点，依据给用户，用户拍板。**

---

## 一、选型决策表（按顺序匹配，命中即停）

| 顺序 | 如果…… | 选 | 一句话 |
|------|--------|-----|--------|
| 1 | 无文件产出 且 无外部调用 且 知识 < 5K | **minimal** | 只有一个 SKILL.md |
| 2 | 有外部 API / 工具调用 | **tool** | 脚本管调用、references 管契约 |
| 3 | 有文件产出 且 格式固定 | **template** | assets 放模板、scripts 管渲染校验 |
| 4 | 知识量大（专家经验为主，需拆分查阅） | **knowledge** | references 是主体 |
| 5 | 多步骤带 checkpoint 且 无外部调用 且 无文件产出 | **pipeline** | 细则下沉、主文件留路由 |
| 6 | 对外发布 / 高风险 / 长迭代 | **full** | 脚本+知识+素材+治理台账四件套 |
| 7 | 覆盖多个**正交子域**（auth/DB/云函数/AI/ops…）**且每个子域有独立用户价值**（不只是技术分层） | **suite** | 路由器 + N 个自治子 skill（重量级，子域 >8）或品类模块（轻量档，2–8 子域）+ 横切协议 |
| — | 都不命中 | **pipeline** | 默认 |

> **minimal 是起点不是终点**。装不下时按「先 references/ → 再 scripts/ → 再 assets/」逐步扩容，别一次上满。

---

## 二、七套框架详解

### 1. minimal — 极简型（单文件）

```
my-skill/
└── SKILL.md     # frontmatter + 五段章节骨架，≤500 行
```

**适用**：思维型 / 导航型 / 哲学型；无脚本、无文件产出、知识量小。
**忠告**：新手最常见的过度工程，就是给纯原则型 skill 硬塞 `scripts/` 和 `references/`。先做单文件，装不下再拆。

### 2. pipeline — 流程型

```
my-skill/
├── SKILL.md              # 意图路由 + Workflow + 检查点约定
├── references/
│   ├── README.md         # agent 索引（先读此表再决定是否加载全文）
│   ├── step-guide.md     # 逐步细则：输入→判断规则→输出→失败怎么办
│   └── edge-cases.md     # 例外：症状→原因→修复
├── scripts/              # 仅当某步「LLM 会出错、脚本能 100% 确定」才建
└── CHANGELOG.md          # 仅发布级；SKILL.md 不引用
```

**适用**：≥3 步、有分支与中间状态。
**忠告**：流程型的成败在 checkpoint——每阶段确认产物，批量操作记录已处理/未处理项。

### 3. tool — 工具编排型

```
my-skill/
├── SKILL.md              # allowed-tools 最小化 + 调用纪律 + 失败升级
├── scripts/
│   ├── call_api.py       # 统一 JSON 输出 + 异常自处理 + 退出码语义化
│   ├── precheck.py       # 环境与依赖预检
│   └── install.sh        # ◎分发与安装：下载后哈希/签名校验 + 校验失败处置
├── references/
│   ├── README.md
│   ├── api-contract.md   # 端点 / 参数 / 错误码 / 限流 / 重试策略
│   └── commands.md       # ◎命令/接口速查表：能力域分组 + 参数命名约定 + 常见参数速查
└── CHANGELOG.md
```

**适用**：调外部 API / DB / CLI。
**忠告**：头号反模式是「只写成功路径」——超时、限流、鉴权失效、**部分成功**四种失败必须各有明确动作。

**◎ tool 型必填专项字段**（v3.7.0，源自 westock-data 1.0.7 正向对标——我们的模板原样漏了这两项）：

| 专项 | 必填内容 | 为什么不能省 |
|---|---|---|
| **① 命令 / 接口速查表** | `references/commands.md` 按**能力域分组**（不是按数据域）+ **参数命名约定**（同一概念全库同名）+ **常见参数速查**；SKILL.md 主路由**再压一张 ≤10 行的速查表** | 主路由只放"能力域 → 详查命令"指针，agent 不必加载全文就能拼对调用；命名不约定的后果是同一参数在两份文档里两个名字 |
| **② 分发与安装信任链** | `scripts/install.*`：下载产物**必须校验**（哈希 / 签名二选一）+ **校验失败如何处置** + 验证命令；多平台脚本（sh / ps1 / cjs…）**校验语义必须一致** | 只写依赖名 = 把"依赖没装 / 产物被篡改"留给 agent 即兴发挥；三份脚本各写各的校验，等于没有校验 |

> **对照 Resource Routing 段的写法**：① 速查表 = 正向决策表【命中某能力域 → 详查 commands.md§X → 拼出调用】；② 信任链 = 同一缺省处置，写入 01-条件「资源约束三件套」（依赖 / 缺失时处置 / 验证命令）。
> **本 skill 自证**：`scripts/sd_cli.py` 依赖 —— 缺失处置______；验证命令 `python scripts/sd_cli.py --help`。

### 4. knowledge — 知识密集型

```
my-skill/
├── SKILL.md              # 只放：核心工作流/资源路由/关键约束/交互策略/失败处理/验证要求
├── references/
│   ├── README.md         # 必备：文件/摘要/加载条件/标签/体量
│   ├── domain-a.md       # 一主题一文件，>300 行加目录
│   ├── domain-b.md       # 与 a 正交，不重叠
│   └── gotchas.md        # 症状→原因→修复（来源：B02 追问五问之③）
└── CHANGELOG.md
```

**适用**：领域知识包、LLM 本身不知道的规则。
**忠告**：资源路由写成强指令——`If the user mentions X, load references/x.md before choosing Y.`，避免「see references/x.md」式弱路由。

### 5. template — 模板产出型

```
my-skill/
├── SKILL.md              # 必须含「## 输出文件约定」四要素
├── assets/               # 不进上下文
│   ├── templates/        # 占位符 + 填充规则
│   └── examples/         # golden sample，供校验比对
├── scripts/
│   ├── render.py         # 读模板→填占位符→落盘→返回结构化结果
│   └── validate.py       # 比对 schema/格式，非零退出码 = 不通过
├── references/
│   ├── README.md
│   └── style-rules.md    # 可判定的规则，不写「美观大方」
└── CHANGELOG.md
```

**适用**：Generator / 格式固定的文件产出。
**忠告**：最容易漏「错误输出」——失败时产出什么、写到哪，必须和成功路径一样明确。

### 6. full — 全栈工程型

```
my-skill/
├── SKILL.md              # ≤500 行：意图路由表 + 五段骨架 + 全局安全红线
├── scripts/
│   ├── cli.py            # 统一入口 + --dry-run + 自动重试
│   ├── retry.py          # 只重试环境/IO 类，业务错误不重试
│   └── validate.py       # --self / --json / --fix
├── references/
│   ├── README.md         # agent 索引，控制在 150 行内
│   ├── design-guide.md
│   ├── best-practices.md
│   └── gotchas.md
├── assets/templates/
├── MISTAKES.md           # 错误台账：NEVER→后果→改为 Y（TOP5 注入 SKILL.md）
├── REQUIREMENTS.md       # 需求看板（可选）
├── SOLUTIONS.md          # 方案看板 + ADR（可选）
└── CHANGELOG.md
```

**适用**：对外发布、高风险、多模块、需长期迭代。
**忠告**：治理文件（MISTAKES / REQUIREMENTS / SOLUTIONS / CHANGELOG）**都不得被 SKILL.md 正文引用**——只由人或工具按需读取，否则污染上下文。

### 7. suite — 套件型（大领域多子域）

```
my-suite/
├── SKILL.md              # 路由器：意图路由契约 + 全局护栏 + 工程宪法
├── references/
│   ├── README.md         # 套件索引：子 skill 清单 + 加载条件（先读此表）
│   ├── <sub-skill-a>/SKILL.md   # 子 skill 自治（自己的 frontmatter + 五段骨架 + references/）
│   ├── <sub-skill-b>/SKILL.md
│   └── protocols/        # 跨场景横切协议（可选但推荐）
│       ├── change-safety.md     # 变更安全：任何代码/配置变更前必读
│       └── deployment-gate.md   # 部署门禁：部署/发布前必过检查
└── CHANGELOG.md
```

**适用**：领域覆盖多个**正交子域**（auth / 数据库 / 云函数 / AI / ops…），每个子域自成体系、可独立使用。顶层 SKILL.md 只做**路由 + 护栏**，领域细节全部下沉子 skill。
**忠告**：
- 路由器配**结构化场景路由契约**——每场景含 触发信号/优先级/首读/再读/**禁读**/动作前检查/常见错误（见 [design-blocks-library.md](design-blocks-library.md) D-065），而不是"意图→动作"两列表；
- 子 skill 用**稳定 id** 引用（`references/<skill-id>/SKILL.md`），同域内用相对路径互引；
- 跨所有子场景的强制红线（变更安全 / 部署门禁 / 敏感数据）**独立成 protocols/ 协议层**，由路由器统一声明"任何改动前必读"；
- **路由器防膨胀**：子域细节绝不塞进顶层 SKILL.md，否则路由表会被稀释、护栏失效。
**活样板**：cloudbase-2.32.4（腾讯云开发技能包，30+ 子 skill）→ [`example/absorbed/cloudbase/`](../example/absorbed/cloudbase/README.md)。

**suite 两档选型**（2026-09-03 tencent-docs-1.0.41 切片补充）：
- **重量级**（上表）：子域 >8 且每个子域需独立使用 → 路由器 + N 个**自治子 skill**（各有自己的 frontmatter + references）。
- **轻量档**：**2–8 个正交子域** → 不拆子 skill，用「路由器 + N 个 `entry.md` 品类模块 + 组件级规范」——子模块是**文档**而非子 skill，token 成本按需发生：

```
my-suite/
├── SKILL.md              # 路由器：意图路由 + 硬纪律 + 错误码兜底（~240 行足够）
├── <domain-a>/entry.md   # 品类全工作流（状态探测→前置契约→执行→校验）
├── <domain-b>/entry.md
├── references/           # 跨品类公共层：公共接口 / 鉴权状态机 / 错误码表
└── scripts/              # 本地脚本工具箱（易错操作封装，单行 JSON 输出）
```

轻量档纪律：**每层明确"不做什么"**（品类层不复述全局规则、规范层不重复契约内容）；同一信息只在一处呈现，其余用链接引用；SKILL.md 内嵌目录自述图 + 每文件一句话职责。活样板：[`example/absorbed/tencent-docs/`](../example/absorbed/tencent-docs/README.md)。

---

## 三、常见误用

| 误用 | 正解 |
|------|------|
| 一上来就按 full 建全套 | 从 minimal 起步，装不下再扩容 |
| 把模板放进 references/ | 输出素材放 `assets/`（不进上下文），知识才放 `references/` |
| 每个 reference 都塞进 SKILL.md 引用 | 只从 SKILL.md 直接链接关键 reference，避免深层引用 |
| references 文件超长不加目录 | >300 行必须加目录，否则 Agent 注意力会迷失 |
| 治理文件写进 SKILL.md | CHANGELOG 等放包根、不被引用 |
| 大领域硬塞进单个 SKILL.md / full | 子域正交且多 → 升 **suite**：路由器 + 自治子 skill |
| 套件路由器膨胀（把子域细节塞进顶层） | 顶层只留路由 + 护栏；领域细节下沉子 skill |
| **因技术复杂而拆 suite**（阶段间无独立用户价值） | 拆的前提是**每块单独拿出来有人会用**；不然合为单 skill，把差异下沉为配置项（见 designer-guide B06 拆合判据） |
| 为渠道 / 模型 / 品牌 / 路径差异各建一个 skill | 差异属**可变配置**，应合并为一个 skill + 配置项，不是拆成多个 |

---

## 四、演进路径与毕业信号（minimal 不是终点）

> **minimal 是起点不是终点**——但何时该毕业？用**可判定的触发信号**，而不是"感觉装不下了"：

| 当前 | 触发信号 | 毕业到 |
|------|---------|--------|
| minimal | 知识 > 5K、要拆 references | knowledge |
| minimal | 出现"脚本能 100% 确定、LLM 会出错"的逻辑 | +scripts（pipeline / tool） |
| pipeline | 需要外部 API / DB | tool |
| pipeline | 有固定格式文件产出 | template |
| 任意 | 对外发布 / 高风险 / 长迭代 | full |
| 任意 | 多 skill 协作 / 意图路由复杂 | full（router） |
| full / knowledge | 覆盖多个**正交子域**、子 skill 需独立使用 | **suite** |

**反向也成立（full 的"过度工程"检测）**：对照 [fix-toolbox.md](fix-toolbox.md) 反模式 8——README/CHANGELOG/scripts 齐全但没必要 → 瘦身回 pipeline / minimal。**毕业是双向的：能上也能下。**

---

## 五、每 archetype 典型失败模式（选型时顺手预警）

> 常见误用表（§三）是**全局**的；这里是**每个结构最常犯的死法**，选型到该结构时主动查一遍，避免"结构选对了、写法还是死"。

| archetype | 典型死法 | 防法 |
|-----------|---------|------|
| **minimal** | 硬塞 scripts/references（过度工程） | 先单文件，装不下再拆 |
| **pipeline** | 只有机械 Step 1/2/3，无决策树 | 每个分支点写判断规则 + checkpoint |
| **tool** | 只写成功路径（超时/限流/鉴权/部分成功四态缺失） | Failure Handling 四状态 + 重试策略各给明确动作 |
| **knowledge** | 弱路由（`see references/x.md`）→ 知识永远不被加载 | 强路由句式：`If 用户提 X → load x.md before 选方案` |
| **template** | 漏错误输出（失败时产什么、写到哪没说清） | 失败也产文件（error.log）+ 非零退出码 |
| **full** | 治理文件（MISTAKES/CHANGELOG）被 SKILL.md 引用、污染上下文 | 治理文件放包根、SKILL.md 正文不引用 |
| **suite** | 路由器膨胀：把子域细节塞进顶层 SKILL.md | 顶层只留路由 + 护栏，领域细节下沉子 skill |
| **suite** | 路由不准：场景模糊、误路由到"看似相关实则错误"的子 skill | 结构化场景路由契约：加 **禁读 doNotUse** 列 + 动作前检查 |
| **suite** | 跨场景红线漏执行（改代码前没跑变更安全协议） | 横切协议独立成 `protocols/`，路由器统一声明"任何改动前必读" |
| **suite** | 轻重不分：2–8 个子域硬拆自治子 skill（过度套件化） | 先上轻量档（`entry.md` 品类模块）；子域 >8 且需独立使用再毕业重量级 |

---

## 关联

- [designer-guide.md](designer-guide.md) — B07 逐格话术（含"先选 archetype 再画目录"）
- [blueprint-template.md](blueprint-template.md) — 07-计划模板与填写示例
- [engineering-practices.md](engineering-practices.md) — 知识分层阈值、脚本四原则
- [fix-toolbox.md](fix-toolbox.md) — 过度工程 / 自由度错配的修复产物