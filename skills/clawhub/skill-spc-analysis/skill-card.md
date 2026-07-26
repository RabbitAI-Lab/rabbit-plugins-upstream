## Description: <br>
SPC统计过程控制分析；当用户需要对制造业生产过程进行质量监控、过程稳定性评估、异常点识别、多周期数据对比分析时使用 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Manufacturing quality engineers and operations teams use this skill to analyze process data, choose SPC control chart types, detect Nelson rule violations, assess process stability, and compare quality trends across reporting periods. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded Excel files and generated HTML reports may contain sensitive production or quality metrics. <br>
Mitigation: Run the skill in an appropriate working directory, restrict access to generated reports, and remove reports when they are no longer needed. <br>
Risk: Incorrect chart-type selection or malformed data can lead to misleading SPC conclusions. <br>
Mitigation: Validate the Excel data format against the included data-format and control-chart references before relying on the analysis. <br>


## Reference(s): <br>
- [Source repository](https://github.com/duding-engicool/skill-spc-analysis) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-spc-analysis) <br>
- [控制图使用指南](references/control_chart_guide.md) <br>
- [数据格式规范](references/data_format_spec.md) <br>
- [Nelson 8条规则详解](references/nelson_rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance, files] <br>
**Output Format:** [Markdown/text guidance with shell command examples, console summaries, and generated HTML report files containing SVG control charts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts Excel input, a required control chart type, optional worksheet name, optional report output path, and optional USL/LSL values for process capability analysis.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata; artifact frontmatter declares 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
