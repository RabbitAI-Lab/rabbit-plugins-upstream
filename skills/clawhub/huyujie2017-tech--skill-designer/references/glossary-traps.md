---
加载条件: 拿不准某个术语/编号/文件归属时；写蓝图要引用积木格、评分体系、骨架文件时；出现"这两个是不是一回事"的疑问时。
核心主题: 认知盲区索引——先给「可推断的命名规律」（省查表），再单列「不可推断清单」（防猜错）。
命中标签: [术语, 易混, 编号, 积木格, 评分体系, 骨架, 陷阱]
不回答: 不回答具体怎么设计 skill（见 designer-guide.md）；不回答边界判定（见 capability-boundary.md）。
---

# 术语陷阱速查（Glossary Traps）— 先规律，后例外

> **为什么有这一页**：绝大多数命名**可以**从规律推断（看懂规律后无需逐条查表）；真正危险的是那一小撮**规律覆盖不到**的——它们看起来"应该能猜"，猜了就错。
> 取自 westock-data D-085（其 `macro-fields.md` 先给字段命名规律、再单列"无法从字段名推断"的拼音缩写表）。

---

## 一、可推断的命名规律（先套规律，能省一半查表）

| 对象 | 规律 | 例 |
|---|---|---|
| **积木格 B01–B10** | `B` = Block，**序号即流水线顺序**，顺序固定不可跳 | B07 一定在 B06 之后、B08 之前 |
| **积木文件** | `NN-格名.md`，两位序号对应格号 | B04 → `04-问题.md` |
| **旧条目编号 A-XXX** | 百位 = 来源批次：`A-0xx` cloudbase / `A-1xx` 混合 / `A-2xx` tencent-docs / `A-3xx` memory-manager-v2 / `A-4xx` ima-skills / **`A-5xx` westock-data** | D-052 = westock-data 第 1 条 |
| **设计原则 DP-XXX** | 百位 = 来源批次：`DP-0xx` ima-skills / `DP-1xx` memory-manager-v2 / **`DP-2xx` westock-data** | DP-201 = westock-data 第 1 条元设计 |
| **脚本命名** | `check_*` 校验 / `init_*` 落盘 / `draft_*` 起草 / `render_*` 渲染 / `trace_*` 评分相关 | `check_blueprint.py` 是校验器 |

---

## 二、不可推断清单（**必须查表，禁止猜**）

### 2.1 积木格：**格名 ≠ 格里装的东西**

这是最高频的坑——格名是抽象动作，内容却是具体产物，**无法从名字推断**。

| 格 | 格名 | 实际装的（易错） |
|---|---|---|
| B04 | 问题 | **需求澄清 / 待定项清单**（不是"提问题"） |
| B05 | 分析 | **输入输出契约 + 风险**（不是"做分析"） |
| B06 | 决策 | 方案选型与取舍（含操作门禁矩阵） |
| B07 | 计划 | 文件结构 + 路由 + 失败处理（**不是**执行） |
| B09 | 评审 | 质量门打分（BR-5 / TRACE，见 2.3） |

> 反例：看到"分析"就往里填 SWOT、看到"问题"就往里填疑问句——都错。**填之前查 `04-问题.md` / `05-分析.md` 模板**。

### 2.2 蓝图的两套骨架**已合一**（事实源 = blocks.py，DP-204 落地）

| 路径 | 骨架源 | 谁用 |
|---|---|---|
| `init` 路径 | `references/blueprint-template.md`（每格「填空字段」段由 blocks.py **生成**） | `init_blueprint.py` |
| `proto` / `draft` 路径 | `scripts/blocks.py`（`fields` 字段表）+ `scripts/draft_blueprint.py`（`build_fillers`） | `blueprint_proto.py` / `draft_blueprint.py` |

> **DP-204（能引用就别同步）**：字段清单的**唯一事实源 = `scripts/blocks.py`**；模板每格字段段由 `scripts/gen_blueprint_fields.py` 生成（`<!-- FIELDS:NN -->` 标记包裹，**勿手改标记段**）。
> 改字段**只改 blocks.py**，然后跑 `python scripts/gen_blueprint_fields.py --write` 同步模板；一致性由 `--check`（已接入 validate）机器把关，不再靠人工 grep。
> **历史教训**（G1 事故三次复发才升级为架构约束）：旧纪律「改任一侧必须同步另一侧」属人工同步，必然漂移——init 出的字段 proto 没有（v3.4.0）、B07「④ 分发与安装」只进模板不进代码（v3.7.0）都是这么来的。

### 2.3 **三套评分体系**（不同层，**不可合并**）

| 体系 | 全称 | 算什么 | 何时用 |
|---|---|---|---|
| **IQS** | Internal Quality Score | 内部质量 = **蓝图完备度**（十格填得齐不齐，每格 10 分，满分 100） | 设计期 |
| **EVS** | External Value Score | 外部价值 = **BR-5 均分 × 20**（填得深不深，20–100） | 设计期 |
| **BR-5** | Blueprint Readiness-5 | 蓝图就绪度五维 | **设计期**评蓝图（B09 质量门） |
| **TRACE** | Trust/Reliability/Adaptability/Convention/Effectiveness | SkillHub 五维评测 | **发布期**评成品 |

> 综合评分 = `IQS × EVS / 100`。**EVS 由 BR-5 换算而来**——所以设计期三个量是联动的，而 TRACE 是**外来框架**、仅用于发布期，**与 BR-5 不是同一层，禁止混用口径评同一对象**。

### 2.4 设计期 vs 发布期（同一份文档里两套口径）

`trace-evaluation-guide.md` 同时装了设计期（§一–§四，BR-5）与发布期（§五–§六，TRACE）。

- 判据：**对象是蓝图 → BR-5；对象是已成型 skill → TRACE**。
- 常见错：用 TRACE 返评的口径去给蓝图打分（反之亦然）。

### 2.5 条目的**两级落点**（入库别落错层）

| 产物 | 落点 | 判据 |
|---|---|---|
| 单点亮点（D-NNN） | `references/design-blocks-library.md` 条目区 + B0X 聚合索引 | 一条讲一个可复用点 |
| 元设计（DP-XXX） | `references/design-principles-library.md` | 解释力 ≥3 条亮点 + 可迁移 + 可表述 |
| 完整案例切片 | `example/design-blocks/<skill-name>/` | 含报告 / 原则 / 图 / 样本导出件 |

> **元设计不重复进 design-blocks-library**（条目库只存亮点）；是否反哺 `design-blocks-library.md` 由用户拍板。

---

## 三、来源与维护

- 本页方法来自 westock-data D-085（认知盲区索引），元设计层 DP-201/DP-203。
- **维护纪律**：新增编号体系/骨架/评分口径时，先问"它能从规律推断吗"——能则补进 §一，不能则补进 §二。
