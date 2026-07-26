## Description: <br>
Request feedback or assistance from Eureka, the primary AI agent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arnarsson](https://clawhub.ai/user/arnarsson) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to ask Eureka for strategic guidance, architectural feedback, help beyond pure coding, or completion reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Messages may be delivered to an unintended or untrusted Telegram destination. <br>
Mitigation: Verify `clawdbot`, `@Eureka_Agent_Bot`, the `mason` reply account, and the numeric reply target before using delivery mode. <br>
Risk: Sensitive project data, credentials, or personal information could be sent to the bot workflow. <br>
Mitigation: Keep requests concise and avoid sharing secrets or private data unless the destination is confirmed and trusted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/arnarsson/skills/eureka-feedback) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Text] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-supplied message content and trusted Telegram delivery settings when using delivery mode.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
