# REPORT.md — 积木 · 模板选择 · report_spec · 事实台账 · assembler

SKILL.md 之外的报告层完整规范。模板细节在各 `templates/T{x}.md`。

***

## 1. 章节积木（B1~B10）

积木 = 叙事目标 + 首选图表 + 常用 transform + 写作要点。大纲的每章从积木取材，模板是积木的成套组合。

| ID | 积木 | 叙事目标 | 首选图表 | 常用 transform | 写作要点 |
|----|------|----------|----------|----------------|----------|
| B1 | 指标概览 | 量化结果与达成 | 按结论定形态：达成单值→gauge/liquid；趋势→line（叠目标线）；结构→pareto/pie；排名→bar | mean/sum 聚合 | 先给绝对值再给相对值；达成类给目标基线 |
| B2 | 趋势走向 | 随时间怎么变 | line / area / combo | pivot_table 长转宽 | 指出方向、斜率变化点、峰值谷值及日期 |
| B3 | 结构构成 | 整体由什么组成 | pie / treemap / stacked_bar | groupby → name+value | Top1+Top2 占比必给；超 6 类先合并尾类 |
| B4 | 对比排名 | 谁多谁少差距多大 | bar / pareto | groupby + sort_values | 给头尾两端的具体差值，不只说"最高最低" |
| B5 | 分布形态 | 数据长什么样 | histogram / boxplot | 数值列直取 | 中心、离散、偏态、离群点四要素 |
| B6 | 转化漏斗 | 流程在哪损耗 | funnel | 分阶段计数 | 逐级给转化率，点出损耗最大的一级 |
| B7 | 相关关系 | X 与 Y 什么关系 | scatter / bubble | 双数值列 | 相关≠因果；点出离群点身份（label-col） |
| B8 | 流向转移 | 从哪来到哪去 | sankey / graph | rename → source/target/value | 主流向前 3 条路径必给数值 |
| B9 | 明细清单 | 证据可查 | spreadsheet | 筛选 / TopN | 报告中的表格节；超 100 行先 TopN |
| B10 | 异常识别 | 哪里不对劲 | boxplot / line+标注 | diff / 阈值标记 | 先界定"何为异常"（口径），再列异常点 |

**降级通用规则**：数据不支持首选图表时，按 B6→B4（无阶段列）、B1→B4（无数值目标）、B7→B5（仅单数值列）方向降级；B1 有目标值但 headline 非单值结论时优选 B2（line 叠目标线），交付语声明。

***

## 2. 模板选择规则

1. 受众是领导且要求短（一页/简报）→ **T8**
2. 周期性 KPI 监控（周/月例行）→ **T1**
3. 单次深挖按领域：用户/留存/转化 → **T3**；业绩/营收 → **T4**；活动/项目复盘 → **T5**；异常排查 → **T6**；问卷/调研 → **T7**
4. 模糊或跨领域 → **T2**（最通用），交付语声明假设
5. 用户给出章节结构或明确不匹配任何模板 → **T0**（摘要 + 方法附录必备，章节按积木自组）

**输出语言**：模板与章节骨架中的中文章节名（如「执行摘要」「分析一」）仅为语义示例，
实际报告的章节标题与叙事语言跟随用户语言（与 CLI `--lang` 自动跟随数据语言的行为一致）；
用户使用英文或其他语言时，不得照抄中文骨架标题。

***

## 3. report_spec.json 规范

Step 6 由 agent 写出，assembler 消费。用 `json.dumps(..., ensure_ascii=False)` 生成，不手写拼接。

```json
{
  "title": "结论式主标题（数字取自台账）",
  "subtitle": "口径 + 时间范围 + 数据来源",
  "theme": "default",
  "executive_summary": "3~5 句，最后写，从各章结论汇总；T8 用作核心结论",
  "sections": [
    {
      "id": "s1",
      "title": "结论式章节标题",
      "narrative": "2~4 句章节叙事，数字均来自台账；\\n\\n 分段",
      "chart_path": "chart_01.html",
      "annotation": "图表下方说明文字（与 Step 5 注入图表的 --annotation 同源）"
    },
    { "id": "s2", "title": "无图章节", "narrative": "...", "chart_path": null }
  ],
  "appendix": {
    "methodology": "数据来源、清洗方法（transform 要点）、统计口径",
    "caveats": "数据局限、样本说明、未覆盖范围"
  }
}
```

字段规则：

* `title`/`sections`（≥1 节，每节 `title` 必填）缺省 → `REPORT_SPEC_INVALID`
* `theme` 取 default/classic/dark，**必须与 Step 3 的 `--theme` 一致**
* `chart_path` 相对 `--charts-dir` 解析（也可绝对路径）；填 CLI stdout 返回的 `html_path` 文件名；`null` = 纯文字节
* `annotation` 可空；spreadsheet 图表节的 annotation 正常渲染
* `executive_summary`/`appendix` 可空（T8 模板附录可省，口径写脚注/章节内）
* `id` 会净化为锚点（非字母数字→`-`），建议直接用 `s1`/`s2`…；与目录联动

assembler 错误码：`5001 REPORT_SPEC_INVALID`（spec 缺字段/非法）· `5002 CHART_HTML_INVALID`（图表文件不可解析）· `5003 REPORT_ASSEMBLE_ERROR`（组装异常）· `5004 LEDGER_MISMATCH`（数字未溯源台账）。错误结构与 CLI 同构（`error`/`code`/`code_name`/`details.suggestion`），处理方式沿用 Exit Criteria。

组装产物结构：封面（title/subtitle/时间）→ 目录（锚点）→ 执行摘要 → 各章节（标题/叙事/图表/annotation）→ 附录 → 页脚。图表以 chartOption 提取方式内联（ECharts 只载一份，交互保留：tooltip/legend/dataZoom；单图页的改名面板与保存按钮不进报告）。

***

## 4. 事实台账（Fact Ledger · ledger.json 落盘）

Step 4 建、落盘；Step 6 由 assembler `--ledger` 程序校验；Step 7 验收。台账是报告唯一的数字来源。

```json
[
  {"id": "rev_h1", "metric": "总营收", "value": 2670, "unit": "万元",
   "source": "chart_01.plot_stats.sum", "sections": ["s1", "summary"]},
  {"id": "yoy", "metric": "同比增长", "value": 23.0, "unit": "%",
   "source": "chart_02.plot_stats.yoy", "sections": ["s1", "summary"]}
]
```

* 字段：`id`（引用键）/ `metric` / `value`（数字或数字字符串，与文本同量纲：文本写"98.6%"则 value 为 98.6，写"2670 万元"则 value 为 2670）/ `unit` / `source`（图 + plot_stats 字段；手算标 `data_preview`）/ `sections`（引用位置，可省）
* 提取时机：Step 3 的批量 stdout（每图的 `plot_stats` + `data_preview`）
* 硬规则：正文/摘要/结论的每个数字先入台账再引用；多处引用从台账复制；派生数字（差值/占比变化）也入账
* **校验规则**（assembler 对 title/subtitle/摘要/章节标题/叙事/图注/附录全量扫描）：
  - 必须溯源：带小数的数字（98.6% / 17.1 个百分点 / 53.0）、>=100 的整数（2670 / 543 / 108）
  - 忽略：日期（2025-01 / 2025 年 / 6 月 / Q3）、图号（图 2）、章节引用（§1）、纯小整数（<100，含整数百分比）
  - 容差：按文本显示位数四舍五入比对（文本 98.6 可命中台账 98.56）
  - 未溯源 → exit 1 + `5004 LEDGER_MISMATCH`（details.misses 列出数字/位置/上下文）；`--ledger-check warn` 可降级为仅警告

***

## 5. 报告写作规范（叙事层）

* **章节标题写结论**：主谓宾+数值（「营收同比增长 23%」），不用名词短语（「营收分析」）
* **报告主标题**：全文最重要的一条结论；时间范围/筛选条件/数据来源放 `subtitle`
* **执行摘要最后写**：从各章结论提炼 3~5 句，每句都要有台账出处
* **章节叙事与 annotation 错位**：annotation 说「这张图」（类型+覆盖范围+最显著事实+口径），narrative 说「这意味着什么」（解释、影响、下步）
* **结论与建议节**（T2/T3/T4/T5/T6）：建议必须由正文证据支撑，每条建议可指回某章
* 数字表述：`x_cardinality` 按语义表述；百分比给基数；大数用万/亿分位并保持全文一致

***

## 6. assembler 用法

```bash
python {skill_base}/scripts/report_assembler.py \
  --spec report_spec.json \
  --charts-dir ./sr_charts \
  --output ./sr_report/report.html \
  --ledger ledger.json
```

* `--charts-dir`：spec 中相对 `chart_path` 的解析基准（默认 spec 同目录）
* `--ledger ledger.json`：启用数字溯源校验（推荐始终传入）；`--ledger-check warn` 降级为仅警告
* 校验通过时 stdout 报告对象含 `ledger` 统计：`{"checked": true, "entries": N, "citations": M, "misses": 0}`
* 成功 stdout：`{"report": {"success": true, "report_path": "...", "sections_count": N, "charts_count": M, "theme": "..."}}`
* 产物单文件自包含（ECharts 内联），离线可开、可打印（print 样式已内置分页避免）
