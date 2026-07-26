## Description: <br>
Generates source-backed vocational education major and major-group research reports, including standard research reports and Double High feasibility analyses with Markdown and HTML outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flyboat403](https://clawhub.ai/user/flyboat403) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Vocational education staff, consultants, and planning teams use this skill to gather source material, confirm outlines, and draft structured Chinese-language reports for major planning, talent demand analysis, and major-group feasibility work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan flags the skill as suspicious because it may run an unverified local Python Markdown-to-HTML conversion script found in the workspace. <br>
Mitigation: Review and approve any md_to_html.py script before execution, or instruct the agent to generate standalone HTML without running local code. <br>
Risk: The skill performs web research and creates report files, which may be unsuitable for sensitive workspaces without review. <br>
Mitigation: Use the skill only in workspaces where web research and file creation are acceptable, and review generated sources and files before relying on them. <br>


## Reference(s): <br>
- [Source repository](https://github.com/flyboat403/vocational-report-generator) <br>
- [ClawHub skill page](https://clawhub.ai/flyboat403/skills/vocational-report-generator) <br>
- [Publisher profile](https://clawhub.ai/user/flyboat403) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown reports and standalone HTML with tables, source notes, and structured section outlines] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses staged user confirmations for source material and outline approval before final report generation.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
