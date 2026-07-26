## Description: <br>
Defines Telegram messaging conventions for eight agent roles, including account IDs, routing fields, report timing, and message templates for multi-agent progress updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to standardize Telegram progress, completion, and issue reports across multiple agent roles. It is intended for multi-agent development workflows, automated task notifications, team progress updates, and decision requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Messages may be sent to the hard-coded Telegram ID 5440561025, exposing task progress or operational details to an unintended recipient. <br>
Mitigation: Before use, change the target to an approved recipient and require explicit approval for outbound Telegram messages. <br>
Risk: Telegram reports may include task progress, file paths, error details, summaries, credentials, or confidential project information. <br>
Mitigation: Review and redact outbound content; do not send secrets, private paths, stack traces, credentials, or confidential details through Telegram. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/agent-telegram) <br>
- [SkillHub Homepage](https://skillhub.cn) <br>
- [Telegram Bot API](https://api.telegram.org) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Configuration] <br>
**Output Format:** [Markdown instructions with message-call examples and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes role-to-account mappings, fixed Telegram routing fields, and message templates.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter is 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
