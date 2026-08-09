## Description: <br>
Chart Generator 2 0 0 helps agents generate SVG charts and simple data visualizations such as bar, line, pie, and sparkline-style charts from supplied data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and automation users can use this skill to produce lightweight chart outputs and chart-generation guidance from structured or textual data. The artifact states it is not intended for real-time stream processing or complex decisions that require human judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence rates the skill as suspicious because it requests broad read, write, and command execution authority beyond a tightly scoped SVG chart generator. <br>
Mitigation: Install and run it only in a restricted workspace, grant least-privilege file access, and review proposed commands and file writes before execution. <br>
Risk: The security evidence notes API, credential, file-processing, and command-execution behavior. <br>
Mitigation: Avoid providing secrets or broad workspace access unless the publisher clarifies exact commands, files, API calls, and output behavior. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/chart-generator-2-0-0) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with JSON examples, shell snippets, and SVG chart file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include SVG charts, ASCII chart examples, status metadata, and setup guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter reports 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
