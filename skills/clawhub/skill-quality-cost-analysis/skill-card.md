## Description: <br>
自动化质量成本分析工具，支持Excel/CSV多Sheet数据读取、智能列识别、数据清洗、四大分类计算、自动图表选择和HTML报告输出；当用户需要质量成本分析、成本结构拆解、趋势分析或质量成本报告时使用 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality managers, manufacturing engineers, and analysts use this skill to process Excel or CSV quality-cost data, classify costs into prevention, appraisal, internal failure, and external failure categories, generate charts, and prepare quality-cost analysis reports. It supports cost-structure review, trend analysis, anomaly interpretation, and optimization recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The calculator reads pickle files, which can execute unsafe payloads when loaded from untrusted sources. <br>
Mitigation: Run the calculator only on pickle files generated locally by the included data-processing step, and do not accept .pkl inputs from untrusted users or systems. <br>
Risk: Generated chart and report HTML can load Plotly from a CDN at report-view time. <br>
Mitigation: Bundle Plotly locally or approve the CDN dependency before distribution, and treat generated reports as network-dependent until that dependency is removed. <br>
Risk: Quality-cost data may contain sensitive operational or business cost information. <br>
Mitigation: Process only data approved for local analysis, store generated intermediate files and reports in controlled locations, and remove sensitive identifiers when they are not needed. <br>
Risk: The inspected report-generation script is empty while the skill describes HTML report generation. <br>
Mitigation: Verify the installed release includes a working report generator before relying on end-to-end report output. <br>


## Reference(s): <br>
- [质量成本分析框架](references/quality_cost_framework.md) <br>
- [图表选择规则](references/chart_selection_rules.md) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-quality-cost-analysis) <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-quality-cost-analysis) <br>
- [Server-resolved source commit](https://github.com/duding-engicool/skill-quality-cost-analysis/commit/bd9785da8b89844d09c36f582d6f23b9c08a8334) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands plus local pickle, JSON, chart HTML, and report HTML files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes local Excel or CSV inputs, writes intermediate cleaned-data and calculation files, and can generate Plotly-based HTML charts and reports.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata; artifact frontmatter lists 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
