## Description: <br>
Scan bank statements to detect recurring charges, flag suspicious transactions, and draft refund requests with interactive HTML reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andreolf](https://clawhub.ai/user/andreolf) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to audit bank or card transaction exports, identify recurring charges and suspicious transactions, and prepare refund or dispute request text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated reports and saved state can expose sensitive financial history. <br>
Mitigation: Keep ~/.refund_radar reports private and delete them when they are no longer needed. <br>
Risk: Refund templates may include card or account details if the user enters them. <br>
Mitigation: Avoid entering full card or account numbers; use only minimal identifiers such as the last four digits when needed. <br>
Risk: Running separately installed refund_radar Python code on real statements could process sensitive bank data. <br>
Mitigation: Verify the installed code before using it with real transaction exports. <br>


## Reference(s): <br>
- [Detection Rules Reference](references/detection-rules.md) <br>
- [Refund Template Reference](references/refund-templates.md) <br>
- [Refund Radar ClawHub Listing](https://clawhub.ai/andreolf/skills/refund-radar) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands; generated HTML and JSON report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates local reports and state under ~/.refund_radar; reports can contain sensitive financial history.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact docs list 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
