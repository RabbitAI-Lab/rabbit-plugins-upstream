## Description: <br>
How to ask a human before a sensitive action and how to log every autonomous action, so your work is accountable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[contro1](https://clawhub.ai/user/contro1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to decide when sensitive actions need human approval and to record autonomous work for accountability. It is intended for actions such as spending money, changing access, deploying infrastructure, deleting data, sending messages on a user's behalf, running fetched code, or working in production sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Autonomous action logs can include personal data, prompts, credentials, message contents, account identifiers, or sensitive operational details. <br>
Mitigation: Configure the Contro1 bridge deliberately and require redaction rules before use. <br>
Risk: Audit details are sent to an external bridge, which may be inappropriate for sessions with strict privacy or data-handling requirements. <br>
Mitigation: Install and enable the skill only when external audit logging to the configured Contro1 bridge is intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/contro1/skills/contro1-approvals) <br>
- [Contro1 CLI documentation](https://contro1.com/docs/cli) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes approval-request guidance and audit-log examples for external review.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
