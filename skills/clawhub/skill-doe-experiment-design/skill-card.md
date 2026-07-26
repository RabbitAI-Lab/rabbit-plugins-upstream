## Description: <br>
生成全因子与部分因子实验方案；支持自定义因子/水平数、分辨率设置及CSV导出，用于实验设计与数据分析；覆盖DOE、正交实验、田口方法等常见设计 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and analysts use this skill to generate DOE experiment plans for full-factorial and two-level fractional-factorial studies, export CSV run tables, and review basic resolution guidance before running experiments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Advanced fractional-factorial, orthogonal, and Taguchi design claims may not provide the advertised statistical properties. <br>
Mitigation: Validate generated advanced designs with a trusted DOE/statistics tool or qualified expert before using them for lab, manufacturing, or costly decisions. <br>
Risk: CSV level values are numeric codes rather than real-world factor settings. <br>
Mitigation: Map coded levels to actual physical units and review the run table before executing experiments. <br>


## Reference(s): <br>
- [DOE实验设计指南](references/doe_guide.md) <br>
- [Server-resolved GitHub provenance](https://github.com/duding-engicool/skill-doe-experiment-design) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-doe-experiment-design) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; the bundled script emits JSON status summaries and CSV experiment-plan files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [CSV files contain Run and Factor_* columns with numeric level encoding.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter lists 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
