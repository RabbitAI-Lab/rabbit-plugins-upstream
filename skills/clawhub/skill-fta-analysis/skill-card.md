## Description: <br>
Builds and analyzes fault trees for system reliability and safety, including visualization, top-event probability calculation, importance analysis, reports, and JSON/YAML import and export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, reliability engineers, safety engineers, and quality teams use this skill to construct fault-tree data, calculate top-event probabilities, identify important basic events, visualize failure logic, and generate fault-tree analysis reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Untrusted JSON or YAML fault-tree files may contain misleading analysis content or text that is carried into generated reports. <br>
Mitigation: Use FTA input files from trusted sources, review imported data before analysis, and validate required fields and probability ranges before relying on results. <br>
Risk: Generated HTML reports include report text derived from input data. <br>
Mitigation: Open generated HTML reports cautiously when the imported data is untrusted, and review report content before sharing it. <br>
Risk: Local scripts write output files such as images, calculation JSON, converted data, and HTML reports. <br>
Mitigation: Choose output paths deliberately and avoid overwriting important files. <br>


## Reference(s): <br>
- [Fault-tree data format reference](references/fta_format.md) <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-fta-analysis) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-fta-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/duding-engicool) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON/YAML fault-tree data, shell commands, generated image files, JSON calculation results, and HTML reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local analysis artifacts from user-provided FTA data; generated HTML reports should be opened cautiously when source data is untrusted.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
