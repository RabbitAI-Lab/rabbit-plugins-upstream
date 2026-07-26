## Description: <br>
B2B company research producing professional PDF reports from a company URL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tomstools11](https://clawhub.ai/user/tomstools11) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Business users, sales teams, and analysts use this skill to research a company, structure market intelligence, and produce a polished account research PDF. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Company research can contain outdated or incorrect business claims from public sources. <br>
Mitigation: Verify important business claims before relying on the generated report. <br>
Risk: The workflow may install ReportLab, write temporary JSON, and save a PDF in the workspace. <br>
Mitigation: Review the commands and output paths before execution in sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tomstools11/skills/research-company) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Report data schema](artifact/references/data-schema.md) <br>
- [PDF generator script](artifact/scripts/generate_report.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Structured research JSON, shell commands, a generated PDF file, and a Markdown download link] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses ReportLab when installed and writes a local PDF report in the workspace.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
