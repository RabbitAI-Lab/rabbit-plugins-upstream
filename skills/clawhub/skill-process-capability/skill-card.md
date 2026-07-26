## Description: <br>
过程能力分析技能；计算CP/CPK/PP/PPK等指标，支持正态/二项分布建模，控制图/直方图/能力图可视化；用于质量工程师进行过程能力评估、数据建模或生成质量分析报告 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality engineers and manufacturing analysts use this skill to evaluate process capability from CSV, Excel, or inline measurement data, calculate capability and performance indices, fit distributions, and produce charts or reports for quality review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The scripts can write or overwrite requested report and chart files. <br>
Mitigation: Provide output paths intentionally and avoid pointing outputs at important existing files. <br>
Risk: Capability metrics can be misleading when sample size, data order, distribution assumptions, or specification limits are inappropriate. <br>
Mitigation: Confirm USL and LSL values, preserve time order for control charts, and review normality or fit-test results before using metrics for decisions. <br>


## Reference(s): <br>
- [过程能力指标详解](references/metrics_guide.md) <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-process-capability) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-process-capability) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/duding-engicool) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON metrics, CSV or Excel reports, and PNG charts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads user-provided quality data and writes requested report or chart files.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
