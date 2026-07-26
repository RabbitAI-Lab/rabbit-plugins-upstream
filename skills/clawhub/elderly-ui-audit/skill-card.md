## Description: <br>
Audits web and mobile UI code against Chinese MIIT elderly-friendly design standards, producing a compliance report, suggested changes, and optional style-focused fixes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xuyuting133](https://clawhub.ai/user/xuyuting133) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to scan websites and mobile apps for elderly-friendly UI compliance, especially font sizing, color contrast, interaction targets, captcha alternatives, advertising patterns, navigation, and compatibility. It helps produce an audit report and concrete remediation guidance before teams apply changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated audit findings or suggested changes may need project-specific review before teams act on them. <br>
Mitigation: Review generated reports and recommendations before applying changes. <br>
Risk: The optional fix path may edit style files. <br>
Mitigation: Use fixes only on a clean working tree and review the resulting diff. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/XuYuting133/elderly-ui-audit/tree/main/skills/elderly-ui-audit) <br>
- [Project homepage](https://github.com/XuYuting133/elderly-ui-audit) <br>
- [ClawHub skill page](https://clawhub.ai/xuyuting133/skills/elderly-ui-audit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown responses with an HTML audit report file and optional style-file edits] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write elderly-audit-report.html; optional fixes should be reviewed after execution.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
