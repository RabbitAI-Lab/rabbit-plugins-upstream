---
name: smart-report
version: 1.1.1
display_name: 智能报告
display_name_en: Smart Report
description_zh: "将数据文件（CSV/TSV/TXT/XLSX/XLS/JSON）转化为单文件交互式 HTML 报告，内置 ECharts 可视化、结论式叙事与可溯源数字台账（fact ledger）；也可批量生成独立交互式图表 HTML（26 类图表、3 套主题）。当用户要求从数据文件撰写报告、周报/月报、分析文档、复盘或汇报材料，或提供数据文件要求出图时使用。"
description_en: "Data-to-report skill. Turns data files (CSV/TSV/TXT/XLSX/XLS/JSON) into single-file interactive HTML reports with ECharts visualizations, narrative analysis and full numeric traceability (fact ledger). Also batch-generates standalone interactive chart HTML files (26 chart types, 3 themes) via its chart CLI. Use when the user asks to write a report, weekly/monthly report, analysis document, review, or presentation material from data files, or provides data files asking for charts."
license: MIT
compatibility: "Python 3.11+；HTML 报告依赖 pandas/numpy/openpyxl/xlrd；docx/pptx 导出另需 python-docx/python-pptx/resvg-py 与 Node≥16；全程离线（ECharts JS 内联，无 CDN）"
permissions:
  file_read: true
  file_write: true
  network: false
safety:
  sandbox: "LLM 生成的 transform 代码经三层校验（关键字黑名单 + AST 白名单 + 安全 builtins）后，在资源受限的子进程沙箱中执行；禁止 import/open/exec/eval/subprocess/网络/文件 I/O，无需用户确认"
input_formats: ["csv", "tsv", "txt", "xlsx", "xls", "json"]
output_format: html
---

# Smart Report

> 将数据文件（CSV/Excel/JSON）转化为单文件 HTML 报告（可选导出 DOCX/PPTX 交付版）：结论式章节叙事 + 交互式 ECharts 图表 + 可溯源数字（事实台账，支持占位符引用模式）。内置 9 套报告模板与 10 种章节积木，图表由内置引擎批量生成（26 类图表、3 套主题、沙箱 transform）。
> 核心契约（transform 沙箱、CLI 关键 flags、错误码速查）见正文下方；完整 flags 语义与 FAQ 见 [REFERENCE.md](./references/REFERENCE.md)，积木定义、模板选择规则、report_spec/台账规范、assembler 用法见 [REPORT.md](./references/REPORT.md)。

***

## Activation Triggers

* 用户提到「写报告」「周报/月报」「分析报告」「复盘」「汇报材料」「数据报告」「report」，或提供数据文件要求产出带图表的文档
* 仅要单独一张图（不要文档交付物）不是本技能的触发场景——引导用户使用图表类技能

***

## 模板索引（MUST 先匹配再动笔）

| ID | 模板 | 触发词 | 图数 |
|----|------|--------|:----:|
| T1 | 经营周报/月报 | 周报、月报、经营分析、KPI 复盘 | 3~6 |
| T2 | 专项分析报告 | 深度分析、为什么、归因、专项 | 4~8 |
| T3 | 用户行为分析 | 用户分析、留存、转化、行为 | 4~7 |
| T4 | 销售业绩分析 | 业绩、达成率、营收分析 | 4~7 |
| T5 | 复盘评估报告 | 复盘、活动效果、ROI 评估 | 3~6 |
| T6 | 异常诊断报告 | 为什么下降、异常、排查 | 3~6 |
| T7 | 调研分析报告 | 问卷、调研、满意度 | 4~7 |
| T8 | 汇报简报 | 汇报材料、给领导看、一页报告 | 2~4 |
| T0 | 自由组装 | 无模板匹配 | 开放 |

**MUST**：匹配模板后先读 `templates/T{x}.md` 再写大纲（模板含章节骨架/降级路径/验收要点）。选择规则见 REPORT.md（受众是领导且要短 → T8；周期性监控 → T1；单次深挖按领域 → T3~T7；模糊 → T2，交付语声明假设）。

***

## 七步工作流（MUST 按序执行）

**Step 1 · 意图解析 + 模板匹配**：确定报告类型、受众、数据文件、时间范围；按选择规则定模板。数据文件不存在 MUST 先向用户索要，不得编造。

**Step 2 · 读模板 → 实例化大纲**：按模板骨架产出章节，每章标注「本章观点 + 积木（B1~B10）+ 图表意图」。数据不支持某积木时走模板内降级路径并在交付语中声明。无图可配的章节自问是否空洞。

**Step 3 · 图表规划 + 批量生成**（选型规则：**首图 = 证明主标题结论的那张图**，由「结论类型 + 数据形态」查下方选型表决定，不因位于概览章而默认仪表盘。gauge/liquid 仅用于达成类单值结论；多 KPI 概览优先一张 bar 每柱一指标；全篇 gauge 超过 1 张时自问是否应合并为 bar）：大纲 → 一份 `charts.json` → 一次 CLI 调用（≥2 张图 MUST 批量，禁止逐张单图调用）：

```bash
python {skill_base}/scripts/cli.py data.xlsx --sheet "Sheet1" \
  --charts-file charts.json --theme default --output-dir ./sr_charts
```

`charts.json` 每项：`type`（必填）+ `title`/`subtitle`/`x_axis`/`y_axis`（字符串或数组）/`transform_code`/`annotation`。transform 含中文/引号 MUST 写 JSON 文件，不直接在 shell 传 `--charts`。`--theme` 与 spec.theme 一致。

**Step 4 · 建事实台账（ledger.json 落盘）**：遍历 stdout 各图的 `plot_stats`/`data_preview`，提取关键数值写入 `ledger.json`（schema 与匹配规则见 REPORT.md）。**硬规则：正文/摘要/结论引用的每个数字必须先入台账再引用，禁止凭记忆写数**；同一数字多处引用从台账复制；派生数字（差值/占比变化）也入账。台账是本报告唯一的数字来源，Step 6 组装时由 assembler 程序校验（见 --ledger）。
台账引用有两种模式（由 `--ledger-mode` 选择）：**scan**（默认，向后兼容——写死数字，assembler 扫描比对）与 **placeholder**（推荐——叙事中写 `{{台账id}}` 或 `{{台账id:,.1f}}`，assembler 替换并校验精度，杜绝漏检/误检）。新报告优先用 placeholder 模式。

**Step 5 · 逐章叙事**：每张图两步——① 先带 `--dry-run` 调用取 `plot_stats`（多图模式下对缺 stats 的图单图补跑 dry-run）→ ② 写 2~4 句章节叙事（① 图是什么 ② 最显著事实 ③ 口径说明），正式生成时 `--annotation` 注入图表说明。写作规则：**章节标题写结论**（主谓宾+数值，如「营收同比增长 23%」，数字取自台账）；**执行摘要最后写**（从各章结论汇总 3~5 句）；章节叙事说「这意味着什么」，annotation 说「这张图」。

**Step 6 · 组装**：写 `report_spec.json`（字段规范见 REPORT.md），调用 assembler：

```bash
# 基础 HTML（scan 模式，向后兼容）
python {skill_base}/scripts/report_assembler.py --spec report_spec.json \
  --charts-dir ./sr_charts --output ./sr_report/report.html \
  --ledger ledger.json

# 推荐：placeholder 模式 + 多格式导出（html + docx + pptx）
python {skill_base}/scripts/report_assembler.py --spec report_spec.json \
  --charts-dir ./sr_charts --output ./sr_report/report.html \
  --ledger ledger.json --ledger-mode placeholder \
  --format html,docx,pptx
```

`--format` 接受 `html|docx|pptx` 逗号组合或 `all`，默认仅 `html`。docx/pptx 为**静态交付版**：图表经 Node SSR 渲染为 SVG 再光栅化 PNG 内嵌（需 Node ≥ 16 与 resvg-py；缺依赖时报 5007 并继续产出 HTML，不中断）。HTML 恒为主交付物；docx/pptx 按用户需求选用——用户只要网页/交互版 → 仅 html；要 Word 归档 → 加 docx；要汇报演示 → 加 pptx。用户未指定时默认仅 html，交付语中提示可选格式。

**Step 7 · 验收（机械可判定）**：
* ✅ assembler stdout 为 `{"report": {"success": true, ...}}` 且 `report_path` 指向的文件存在且非空
* ✅ spec 中每个 `chart_path` 的图表 HTML 存在且非空（assembler 已强制校验，缺失会报错）
* ✅ 正文关键数字 100% 可溯至 ledger.json（assembler `--ledger` 程序校验；scan 模式漏溯源报 5004 LEDGER_MISMATCH，placeholder 模式裸数字报 5005、未注册占位符报 5004，比 agent 自查更硬）
* ✅ `--format` 含 docx/pptx 时：stdout `exports` 列出的文件存在且非空；`export_errors` 中的格式须在交付语中说明原因（缺依赖属可降级，不算失败）
* ✅ 章节覆盖模板骨架全部必备章节
* ❌ 图表 CLI 或 assembler 失败 → 读 `error.details.suggestion`，修正后重试；**同一环节最多重试 2 次**
* 🛑 **仍失败（唯一必须的用户介入点）**：把 `code_name`、`suggestion`、已尝试的修复如实报告用户并给出建议，等待决策。不得静默改用自写脚本兜底。

***

## 图表规划知识（Step 3 直接依赖）

### 契约（5 条，MUST）

1. 列名解析后会被规范化：转小写、特殊字符→`_`（如 `总学时`→`总_学时`），中文保留；`--x-axis`/`--y-axis`/transform 必须引用规范化后的列名
2. transform 沙箱：可用变量仅 `df`/`pd`/`np`，支持多语句，必须产出名为 `result` 的 DataFrame；禁止 import/open/try/类定义（黑名单 + AST 白名单强制校验，违规返回带 `suggestion` 的错误）
3. pie/bar 等按「1 个分类列(name) + 1 个数值列(value)」读数据；分类频次图先 transform 聚合成 name/value 两列，再指定 `--x-axis name --y-axis value`
4. 成功时 stdout：`success`/`html_path`/`chart_type`/`title`/`data_rows`/`data_preview`（绘图数据前 10 行）+ `plot_stats`（完整统计摘要，写叙事用）
5. 校对口径直接读 stdout 的 `data_preview` + `data_rows`，不要打开 HTML 搜数据——预览即被绘制内容的真值

### 黄金示例

```bash
# 分类频次 → pie/bar（最高频）
--transform-code "result = df['类别列'].fillna('未标注').value_counts().rename_axis('name').reset_index(name='value')"

# 分组聚合 → bar
--transform-code "result = df.groupby('分组列')['数值列'].sum().rename_axis('name').reset_index(name='value')"

# 长→多系列（多列趋势）
--transform-code "result = df.pivot_table(index='<time>', columns='<category>', values='<value>', aggfunc='sum').reset_index()"
```

**口径陷阱**：聚合前想清楚「按数据行 vs 按去重实体」——统计实体属性先 `drop_duplicates`；生成后对照 `data_preview` 检查（各行 value 之和等于原始行数而非实体数，就是忘了去重）。

### Chart Types 选型表（26 类）

选型前核对 Required Format；不匹配则用 transform 适配。heatmap/boxplot/radar 等多列图表，各列量纲差异大时先归一化。

| ID | Best For | Trigger Keywords | y_axis | Required Format |
|----|----------|------------------|:------:|-----------------|
| `line` | 时间趋势 | trend, 趋势, 变化, 走势 | 1~N | 1 时间列 + 1~N 数值列 |
| `bar` | 类目对比 | compare, 对比, 排名, 差异 | 1~N | 1 类目列 + 1~N 数值列 |
| `area` | 累计变化 | cumulative, 累计 | 1~N | 1 时间/类目列 + 1~N 数值列 |
| `pie` | 构成占比 | share, 占比, 构成, 比例 | 1 | 1 name + 1 value |
| `scatter` | 相关关系 | correlation, 相关, 关系 | 1 | 2 数值列 或 1+1 |
| `radar` | 多维对比 | multi-dimension, 多维, 综合, 雷达 | N | 1 指标列 + N 数值列 |
| `heatmap` | 交叉密度 | density, cross, 交叉, 矩阵, 热力 | N | 2 类目列 + 1 数值列 |
| `treemap` | 层级占比 | hierarchy, 层级, 嵌套 | 1 | 1 name + 1 value |
| `graph` | 实体关系 | relationship, 网络, 拓扑 | special | source + target (+value) |
| `boxplot` | 分布离群 | distribution, 分布, 离群 | N | N 数值列 |
| `waterfall` | 增量变化 | increment, 增量, 瀑布 | 1 | 1 类目 + 1 数值（增量） |
| `gauge` | KPI 进度 | progress, kpi, 进度, 达成 | 1 | 1 数值列（取均值） |
| `sankey` | 流向转移 | flow, 流向, 流量, 转移 | special | source + target + value |
| `funnel` | 转化率 | conversion, 转化, 漏斗, 流失 | 1 | 1 name + 1 value |
| `sunburst` | 单层占比 | proportion, sunburst, 旭日 | 1 | 1 name + 1 value |
| `wordcloud` | 词频关键词 | word frequency, 词频, 关键词, 词云 | 1 | 1 name + 1 value |
| `histogram` | 分布形态 | distribution, 分布, 直方图 | 1 | 1 数值列 |
| `stacked_bar` | 堆叠构成 | composition, stacked, 堆叠 | 1~N | 1 类目 + 1~N 数值 |
| `bubble` | 三变量相关 | bubble, 气泡, 三变量 | 2 | 2 数值 + 1 size |
| `pareto` | 二八分析 | pareto, 帕累托, 二八 | 1 | 1 类目 + 1 数值 |
| `combo` | 双轴组合 | dual-axis, 双轴, 组合 | 1~N | 1 类目 + 1 bar + 1~N line |
| `venn` | 集合交集 | overlap, 交集, 重叠, 韦恩 | 1 | 1 name + 1 value（交集行 `A∩B`） |
| `mindmap` | 层级大纲 | mind map, 思维导图, 大纲 | 1 | 1 parent + 1 child |
| `orgchart` | 组织架构 | org chart, 组织架构, 层级 | 1 | 1 parent + 1 child |
| `liquid` | 百分比进度 | liquid, 水波, 进度, 完成率 | 1 | 1 数值列（取均值） |
| `spreadsheet` | 明细表格 | table, 明细, 清单, 表格 | N | 任意列（x/y 可选筛选列） |

scatter/bubble/boxplot 中未被 x/y 占用的字符串列自动作为身份列进 tooltip（`--label-col`）。

### Transform 常用模式

* 长转宽: `pivot_table`（见上）
* 宽转长: `result = df.melt(id_vars=['date'], var_name='name', value_name='value')`
* 过滤: `result = df[df['metric']=='revenue'][['category','value']].rename(columns={'category':'name'})`
* 重命名: `result = df.rename(columns={'来源':'source','去向':'target','金额':'value'})`
* 前向填充合并单元格: `result = df.ffill()`
* 瀑布增量: `tmp = df.copy(); tmp['delta'] = tmp['profit'].diff().fillna(tmp['profit'].iloc[0]); result = tmp[['month','delta']]`
* 不要原地修改 `df`（用 `df.copy()` 或链式操作）；原始数据已匹配目标格式时不传 transform

***

## Hard Constraints (MUST follow)

1. **MUST 走 CLI 工作流**（`cli.py` 批量出图 + `report_assembler.py` 组装），不要自写脚本替代
2. **MUST 先读模板文件再写大纲**（`templates/T{x}.md`）
3. **脏表头 MUST 用 CLI flags**（`--skiprows N`/`--header-row N`/`--sheet`，语义见 REFERENCE.md）；N 由实际数据决定（先无 flags 跑一次看原始布局）
4. **列重命名/重塑/聚合 MUST 用 `--transform-code`**；解析层只解决"哪行是表头"
5. **MUST report unsupported scenarios**: 不支持的场景（如嵌套 JSON 超 1 层、Word/PPT 之外的私有格式）先向用户说明并给建议，不得静默绕过；docx/pptx 导出缺可选依赖时如实报 5007 并交付 HTML，不伪装成功
6. **MUST NOT 硬编码绝对路径**；运行时解析路径（`{skill_base}` 相对）
7. **不要主动传 `--lang`**；CLI 自动跟随数据语言，仅当用户明确要求时才传
8. **数字 MUST 溯源台账**（见 Step 4 硬规则）；解读的每个数字都必须能在 `plot_stats`/`data_preview` 里找到出处；placeholder 模式下正文的数值一律写 `{{id}}`/`{{id:fmt}}` 引用，禁止手写数字（格式符须与台账精度一致，如 `{{total:,.1f}}`）
9. **执行摘要最后写**；`x_cardinality` 是去重个数，按 x 列语义表述（x 是「姓名」则说「59 名学生」而非「59 个类别」）

***

## 默认策略（不向用户确认）

生成报告是廉价可逆动作（重生成秒级，零外部副作用）。模板选择（按选择规则）、图表类型（按选型表）、取值口径（按列名/单位/数值范围推断）均由 agent 内部决定，不打断用户。

**事后审阅代替事前确认**：交付语中显式列出关键假设（所选模板及理由、图表选型依据、聚合口径、降级替换）。用户不同意任一假设，可一句话要求换模板/换口径/换类型重生成。

***

## Exit Criteria（机械可判定）

* ✅ **成功**: assembler stdout 为 `{"report": {"success": true, ...}}`，`report_path` 文件存在且非空，`--ledger` 校验通过（stdout 含 `ledger` 统计），章节覆盖模板骨架 → 附交付语（关键假设清单）交付
* ℹ️ `--dry-run` 不算交付：仅用于取 `plot_stats` 写叙事，之后必须正式生成并组装
* ❌ **失败**: `success: false` 或 exit code 1 → 读 `error.details.suggestion`，修正后重试；同一环节最多重试 2 次
* 🛑 **仍失败（唯一必须的用户介入点）**: 如实报告 `code_name`/`suggestion`/已尝试修复，等待用户决策

***

## CLI 关键 flags 速查

| Flag | 语义 |
|------|------|
| `<file_path>` `<chart_type>` | 数据文件 + 图表类型（单图模式） |
| `--charts-file <path>` | 多图模式：从 JSON 文件读 `--charts` 数组（推荐，避免 shell 转义） |
| `--transform-code "<code>"` | pandas 转换代码（沙箱执行，必须产出 `result` DataFrame） |
| `--x-axis` / `--y-axis` | 轴列名（引用规范化后的列名） |
| `--title` / `--subtitle` / `--annotation` | 结论式标题 / 口径副标题 / 图表说明 |
| `--skiprows N` / `--header-row N` / `--sheet` | 脏表头定位（N 由实际数据决定） |
| `--theme default\|classic\|dark` | 主题（与 spec.theme 一致） |
| `--sort none\|value` / `--label auto\|all\|key` / `--y-scale` | 排序 / 数值标签 / 折线非零基线 |
| `--lang zh\|en` | 图表语言（默认自动跟随数据，勿主动传） |
| `--dry-run` | 只校验并输出 `plot_stats`/`data_preview`，不写 HTML |

## 错误码速查

| 段 | 代码 | 含义 |
|----|------|------|
| 文件 | 1001/1002/1003/1004 | 文件不存在 / 非普通文件 / 格式不支持 / 超限 |
| 数据 | 2001/2002/2003 | 解析失败 / 合并失败 / 数据为空 |
| 转换 | 3001/3002/3003/3004 | 执行失败 / 无 result / result 非 DataFrame / result 为空 |
| 图表 | 4001/4002/4003 | 生成失败 / 类型不支持 / 轴字段缺失 |
| 报告 | 5001~5007 | spec 非法 / 图表 HTML 非法 / 组装失败 / 台账未溯源 / placeholder 裸数字 / SSR 静态化失败 / 缺可选依赖 |
| 兜底 | 9999 | 未分类错误 |

所有错误统一以结构化 JSON 输出（`error`/`code`/`code_name`/`details.suggestion`），退出码 1。

***

## 指针

* **REPORT.md**：10 种积木定义、模板选择规则、report_spec 字段规范、ledger.json 台账 schema 与校验规则、assembler 用法与错误码
* **REFERENCE.md**：CLI 全参数、flags 语义、错误码表、FAQ
* **templates/T0~T8**：每套模板的章节骨架、降级路径、验收要点
