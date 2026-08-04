---
name: data-analysis
slug: data-analysis
version: 1.1.0
homepage: https://clawic.com/skills/data-analysis
description: "Analyze data and generate visualizations �� query databases, build reports, automate spreadsheets"
tags: [analysis, data, visual, template-based, report-generation]
changelog: "v1.1.0: 增加错误处理、降级策略、依赖声明、数据源验证清单。v1.0.2: Added metric contracts, chart guidance, and decision brief templates."
metadata: {"clawdbot":{"emoji":"D","requires":{"bins":["python3"],"pip":["pandas","numpy"]},"os":["linux","darwin","win32"]}}}
---

## When to Use

Use this skill when the user needs to analyze, explain, or visualize data from SQL, spreadsheets, notebooks, dashboards, exports, or ad hoc tables.

Use it for KPI debugging, experiment readouts, funnel or cohort analysis, anomaly reviews, executive reporting, and quality checks on metrics or query logic.

Prefer this skill over generic coding or spreadsheet help when the hard part is analytical judgment: metric definition, comparison design, interpretation, or recommendation.

## Core Principle

Analysis without a decision is just arithmetic. Always clarify: **What would change if this analysis shows X vs Y?**

## Methodology First

Before touching data:
1. **What decision** is this analysis supporting?
2. **What would change your mind?** (the real question)
3. **What data do you actually have** vs what you wish you had?
4. **What timeframe** is relevant?

## Statistical Rigor Checklist

- [ ] Sample size sufficient? (small N = wide confidence intervals)
- [ ] Comparison groups fair? (same time period, similar conditions)
- [ ] Multiple comparisons? (20 tests = 1 "significant" by chance)
- [ ] Effect size meaningful? (statistically significant != practically important)
- [ ] Uncertainty quantified? ("12-18% lift" not just "15% lift")

## Architecture

This skill does not require local folders, persistent memory, or setup state.

Use the included reference files as lightweight guides:
- `metric-contracts.md` for KPI definitions and caveats
- `chart-selection.md` for visual choice and chart anti-patterns
- `decision-briefs.md` for stakeholder-facing outputs
- `pitfalls.md` and `techniques.md` for analytical rigor and method choice

## Quick Reference

Load only the smallest relevant file to keep context focused.

| Topic | File |
|-------|------|
| Metric definition contracts | `metric-contracts.md` |
| Visual selection and chart anti-patterns | `chart-selection.md` |
| Decision-ready output formats | `decision-briefs.md` |
| Failure modes to catch early | `pitfalls.md` |
| Method selection by question type | `techniques.md` |

## Core Rules

### 1. Start from the decision, not the dataset
- Identify the decision owner, the question that could change a decision, and the deadline before doing analysis.
- If no decision would change, reframe the request before computing anything.

### 2. Lock the metric contract before calculating
- Define entity, grain, numerator, denominator, time window, timezone, filters, exclusions, and source of truth.
- If any of those are ambiguous, state the ambiguity explicitly before presenting results.

### 3. Separate extraction, transformation, and interpretation
- Keep query logic, cleanup assumptions, and analytical conclusions distinguishable.
- Never hide business assumptions inside SQL, formulas, or notebook code without naming them in the write-up.

### 4. Choose visuals to answer a question
- Select charts based on the analytical question: trend, comparison, distribution, relationship, composition, funnel, or cohort retention.
- Do not add charts that make the deck look fuller but do not change the decision.

### 5. Brief every result in decision format
- Every output should include the answer, evidence, confidence, caveats, and recommended next action.
- If the output is going to a stakeholder, translate the method into business implications instead of leading with technical detail.

### 6. Stress-test claims before recommending action
- Segment by obvious confounders, compare the right baseline, quantify uncertainty, and check sensitivity to exclusions or time windows.
- Strong-looking numbers without robustness checks are not decision-ready.

### 7. Escalate when the data cannot support the claim
- Block or downgrade conclusions when sample size is weak, the source is unreliable, definitions drifted, or confounding is unresolved.
- It is better to say "unknown yet" than to produce false confidence.

## Common Traps

- Reusing a KPI name after changing numerator, denominator, or exclusions -> trend comparisons become invalid.
- Comparing daily, weekly, and monthly grains in one chart -> movement looks real but is mostly aggregation noise.
- Showing percentages without underlying counts -> leadership overreacts to tiny denominators.
- Using a pretty chart instead of the right chart -> the output looks polished but hides the actual decision signal.
- Hunting for interesting cuts after seeing the result -> narrative follows chance instead of evidence.
- Shipping automated reports without metric owners or caveats -> bad numbers spread faster than they can be corrected.
- Treating observational patterns as causal proof -> action plans get built on correlation alone.

## Approach Selection

| Question type | Approach | Key output |
|---------------|----------|------------|
| "Is X different from Y?" | Hypothesis test | p-value + effect size + CI |
| "What predicts Z?" | Regression/correlation | Coefficients + R² + residual check |
| "How do users behave over time?" | Cohort analysis | Retention curves by cohort |
| "Are these groups different?" | Segmentation | Profiles + statistical comparison |
| "What's unusual?" | Anomaly detection | Flagged points + context |

For technique details and when to use each, see `techniques.md`.

## Output Standards

1. **Lead with the insight**, not the methodology
2. **Quantify uncertainty** - ranges, not point estimates
3. **State limitations** - what this analysis can't tell you
4. **Recommend next steps** - what would strengthen the conclusion

## 错误处理与降级策�?
### 数据获取失败
| 场景 | 处理方式 |
|------|---------|
| SQL 连接超时 | 重试 1 �?�?提示用户检查网络连接和数据库状�?|
| CSV/Excel 文件损坏 | 尝试 `encoding='utf-8'` �?`encoding='gbk'` �?`encoding='latin1'` 依次降级 |
| 数据为空 | 明确告知"查询结果为空"，分析可能原因（筛选条件过严、时间范围无数据�?|
| 字段缺失 | 列出缺失字段，询问用户是否用替代字段或中止分�?|

### 计算异常
| 场景 | 处理方式 |
|------|---------|
| 除零错误 | 返回 N/A 并标注原因，不用 0 �?Infinity 替代 |
| 数据类型不匹�?| 自动尝试类型转换（str→float），失败则标注异常行 |
| 内存不足（大文件�?| 建议分块读取（`chunksize`），或采样分�?|

### 结果异常
| 场景 | 处理方式 |
|------|---------|
| 结果明显偏离预期 | 先检查数据质量（空值、重复、异常值），再检查逻辑 |
| 统计检验不显著 | 如实报告，不 p-hacking，建议增加样本量或调整指�?|

## 依赖声明

### Python 核心依赖
```bash
pip install pandas numpy scipy matplotlib seaborn
```

### 可选依�?| �?| 用�?|
|----|------|
| `scikit-learn` | 回归/聚类/降维 |
| `statsmodels` | 时间序列/统计检�?|
| `openpyxl` | Excel 读写 |
| `sqlalchemy` | 数据库连�?|
| `plotly` | 交互式图�?|

## Red Flags to Escalate

- User wants to "prove" a predetermined conclusion
- Sample size too small for reliable inference
- Data quality issues that invalidate analysis
- Confounders that can't be controlled for

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| 1.1.0 | 2026-06-29 | 增加错误处理、降级策略、依赖声�?|
| 1.0.2 | 2026-06-20 | Added metric contracts, chart guidance, decision brief templates |
