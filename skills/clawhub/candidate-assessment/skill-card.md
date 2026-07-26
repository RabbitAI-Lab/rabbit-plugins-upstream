## Description: <br>
Evaluates how well a candidate's resume matches a target job description and produces a professional hiring assessment report with scores, risk flags, and interview questions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[casperkwok](https://clawhub.ai/user/casperkwok) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiters, hiring managers, and recruiting operations teams use this skill to compare a resume against a target job description, structure the evidence into assessment data, and render a candidate evaluation report for internal review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated reports may contain candidate PII and hiring judgments. <br>
Mitigation: Use the skill in a controlled environment, keep reports private, and apply the organization's recruiting, privacy, and retention policies before sharing or storing outputs. <br>
Risk: The JD reader may install the unpinned pdfmuse package when it is not already present. <br>
Mitigation: Prefer a pinned, preinstalled dependency setup for production or sensitive recruiting workflows. <br>
Risk: Assessment outputs can influence hiring decisions and may contain incorrect or incomplete judgments if resume or JD evidence is limited. <br>
Mitigation: Treat the report as decision support, review the evidence and questions with qualified humans, and verify conclusions before acting on them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/casperkwok/skills/candidate-assessment) <br>
- [Assessment Prompt and Schema](reference/assessment-prompt.md) <br>
- [Report Design Reference](reference/report-design.md) <br>
- [resume-parsing skill](https://github.com/casperkwok/resume-parsing-skill) <br>
- [pdfmuse package](https://pypi.org/project/pdfmuse/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown-guided workflow with shell commands, JSON assessment data, self-contained HTML report, and optional PDF export.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3; PDF export requires Chrome, Chromium, or Edge; outputs may include candidate PII and hiring judgments.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
