## Description: <br>
OpenClaw skill for Zalo Bot API workflows (bot token) plus optional guidance on unofficial personal automation tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[codedao12](https://clawhub.ai/user/codedao12) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation engineers use this skill to plan Zalo Bot API workflows, configure token-based bot integrations, handle webhook or polling delivery, and document operational guardrails. It also helps distinguish official bot API work from higher-risk unofficial personal-account automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bot tokens, webhook secrets, cookies, and device identifiers may expose account or bot access if logged, committed, or exported. <br>
Mitigation: Store these values as secrets, avoid logging them, keep them out of workflow exports, rotate compromised credentials, and separate development and production tokens. <br>
Risk: Unofficial personal-account automation can create platform-policy and account-session risks. <br>
Mitigation: Prefer the official Zalo Bot API path and use personal-account automation only after explicit acceptance of the platform and account risks. <br>
Risk: Webhook or polling handlers can process spoofed, duplicated, or retried events incorrectly. <br>
Mitigation: Validate webhook secrets, de-duplicate events by message or event ID, make handlers idempotent, and use retry backoff. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/codedao12/skills/zalo) <br>
- [Zalo Bot Platform Overview](references/zalo-bot-overview.md) <br>
- [Bot Token and Setup](references/zalo-bot-token-and-setup.md) <br>
- [Bot Messaging Capabilities](references/zalo-bot-messaging-capabilities.md) <br>
- [Bot UX Playbook](references/zalo-bot-ux-playbook.md) <br>
- [Webhook and Polling Routing](references/zalo-bot-webhook-routing.md) <br>
- [n8n Automation Notes](references/zalo-n8n-automation.md) <br>
- [Personal Zalo Automation](references/zalo-personal-zca-js.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration, shell commands] <br>
**Output Format:** [Markdown plans, checklists, and operational notes with configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
