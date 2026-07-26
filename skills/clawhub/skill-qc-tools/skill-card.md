## Description: <br>
质量管理QC手法辅助工具；支持柏拉图、鱼骨图、直方图、控制图、散布图等图表自动生成；用户需进行质量分析、问题诊断或数据可视化时使用；覆盖QC七大手法 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality managers, manufacturing engineers, and analysts use this skill to prepare quality-analysis inputs, generate QC charts, and interpret defects, root causes, process distributions, control limits, and variable correlations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The local chart generator writes chart and optional analysis files to a user-provided path. <br>
Mitigation: Run it from a controlled project workspace and choose explicit output paths that do not target sensitive filenames or broad system directories. <br>
Risk: Quality data supplied to the script may include operational or sensitive production details. <br>
Mitigation: Use only data approved for local processing, and remove sensitive identifiers when they are not needed for the analysis. <br>
Risk: QC charts and statistical summaries can be misleading when the input data is incomplete, malformed, or not representative. <br>
Mitigation: Validate the JSON input and review chart interpretations with appropriate quality or process expertise before acting on the results. <br>


## Reference(s): <br>
- [QC手法操作指南](references/qc_guide.md) <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-qc-tools) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-qc-tools) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON input examples, generated chart files, and optional JSON analysis output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local QC chart files such as PNG, PDF, or SVG and can export analysis results as JSON.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
