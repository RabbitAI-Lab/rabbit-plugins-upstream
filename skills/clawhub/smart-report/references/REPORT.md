# REPORT.md — 积木 · 模板选择 · report_spec · 事实台账 · assembler

SKILL.md 之外的报告层完整规范。模板细节在各 `templates/T{x}.md`。

***

## 1. 章节积木（B1~B10）

积木 = 叙事目标 + 首选图表 + 常用 transform + 写作要点。大纲的每章从积木取材，模板是积木的成套组合。

| ID | 积木 | 叙事目标 | 首选图表 | 常用 transform | 写作要点 |
|----|------|----------|----------|----------------|----------|
| B1 | 指标概览 | 量化结果与达成 | gauge / liquid | mean/sum 聚合 | 先给绝对值再给相对值；达成类给目标基线 |
| B2 | 趋势走向 | 随时间怎么变 | line / area / combo | pivot_table 长转宽 | 指出方向、斜率变化点、峰值谷值及日期 |
| B3 | 结构构成 | 整体由什么组成 | pie / treemap / stacked_bar | groupby → name+value | Top1+Top2 占比必给；超 6 类先合并尾类 |
| B4 | 对比排名 | 谁多谁少差距多大 | bar / pareto | groupby + sort_values | 给头尾两端的具体差值，不只说"最高最低" |
| B5 | 分布形态 | 数据长什么样 | histogram / boxplot | 数值列直取 | 中心、离散、偏态、离群点四要素 |
| B6 | 转化漏斗 | 流程在哪损耗 | funnel | 分阶段计数 | 逐级给转化率，点出损耗最大的一级 |
| B7 | 相关关系 | X 与 Y 什么关系 | scatter / bubble | 双数值列 | 相关≠因果；点出离群点身份（label-col） |
| B8 | 流向转移 | 从哪来到哪去 | sankey / graph | rename → source/target/value | 主流向前 3 条路径必给数值 |
| B9 | 明细清单 | 证据可查 | spreadsheet | 筛选 / TopN | 报告中的表格节；超 100 行先 TopN |
| B10 | 异常识别 | 哪里不对劲 | boxplot / line+标注 | diff / 阈值标记 | 先界定"何为异常"（口径），再列异常点 |

**降级通用规则**：数据不支持首选图表时，按 B6→B4（无阶段列）、B1→B4（无数值目标）、B7→B5（仅单数值列）方向降级，交付语声明。

***

## 2. 模板选择规则

1. 受众是领导且要求短（一页/简报）→ **T8**
2. 周期性 KPI 监控（周/月例行）→ **T1**
3. 单次深挖按领域：用户/留存/转化 → **T3**；业绩/营收 → **T4**；活动/项目复盘 → **T5**；异常排查 → **T6**；问卷/调研 → **T7**
4. 模糊或跨领域 → **T2**（最通用），交付语声明假设
5. 用户给出章节结构或明确不匹配任何模板 → **T0**（摘要 + 方法附录必备，章节按积木自组）

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

assembler 错误码：`5001 REPORT_SPEC_INVALID`（spec 缺字段/非法）· `5002 CHART_HTML_INVALID`（图表文件不可解析）· `5003 REPORT_ASSEMBLE_ERROR`（组装异常）。错误结构与 CLI 同构（`error`/`code`/`code_name`/`details.suggestion`），处理方式沿用 Exit Criteria。

组装产物结构：封面（title/subtitle/时间）→ 目录（锚点）→ 执行摘要 → 各章节（标题/叙事/图表/annotation）→ 附录 → 页脚。图表以 chartOption 提取方式内联（ECharts 只载一份，交互保留：tooltip/legend/dataZoom；单图页的改名面板与保存按钮不进报告）。

***

## 4. 事实台账（Fact Ledger）

Step 4 建，Step 7 验收。agent 内联维护（对话中的 markdown 表），不落盘、不进 spec。

```
| 指标 | 数值 | 出处 | 引用位置 |
|------|------|------|----------|
| 总营收 | 12.4M | chart_01.plot_stats.sum | §1, 摘要 |
| 同比增长 | +23% | chart_02.plot_stats.yoy | §1, 摘要, 结论 |
| TOP1 客户占比 | 31% | chart_03.plot_stats | §2 |
```

* 提取时机：Step 3 的批量 stdout（每图的 `plot_stats` + `data_preview`）
* 硬规则：正文/摘要/结论的每个数字先入台账再引用；多处引用从台账复制
* 派生数字（如差值、占比变化）也入台账，出处标注两来源列
* `plot_stats` 缺失的图（个别类型）用 `data_preview` 手算入台账，出处标 `data_preview`

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
  --output ./sr_report/report.html
```

* `--charts-dir`：spec 中相对 `chart_path` 的解析基准（默认 spec 同目录）
* 成功 stdout：`{"report": {"success": true, "report_path": "...", "sections_count": N, "charts_count": M, "theme": "..."}}`
* 产物单文件自包含（ECharts 内联），离线可开、可打印（print 样式已内置分页避免）
