## Description: <br>
Sends formatted tracked messages to Feishu channels via webhook with automatic retry on failure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wjl1004](https://clawhub.ai/user/wjl1004) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to configure an agent or message-tracker workflow to send tracked events to Feishu channels as structured cards, with retries and optional HMAC-SHA256 signing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Forwarded message content leaves the local environment for a third-party Feishu webhook. <br>
Mitigation: Confirm the webhook belongs to the intended workspace and only forward message content your organization permits to be shared with Feishu. <br>
Risk: Webhook URLs and optional signing secrets can grant unauthorized posting access if exposed. <br>
Mitigation: Keep the webhook URL and optional signing secret private, and rotate them if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wjl1004/skills/message-tracker-plugin) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JavaScript examples and configuration details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Feishu webhook message-forwarding guidance with retry and optional signing configuration.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence and artifact SKILL.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
