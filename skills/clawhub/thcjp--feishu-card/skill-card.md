## Description:

Sends rich Feishu collaboration cards to users or groups, with support for Markdown, titles, colored headers, buttons, images, and persona-styled messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and automation teams use this skill to send formatted Feishu notifications, reports, alerts, screenshots, and action cards from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured credentials can authorize the agent to send Feishu collaboration messages.

Mitigation: Install only for workflows where agent-directed Feishu sending is intended, and keep credentials scoped and out of message content, logs, and version control.

Risk: Message text, Markdown files, screenshots, or images can expose sensitive information to unintended users or groups.

Mitigation: Review recipients, message body, image paths, and generated reports before sending, especially for alerts, logs, and operational data.

Risk: Button links and callback_url values can send readers or status callbacks to untrusted destinations.

Mitigation: Use trusted HTTPS destinations and verify links and callback URLs before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/feishu-card)
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and command-line examples for sending Feishu collaboration cards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include card title, color, Markdown body, button URL, image path, target user or group ID, persona style, and callback URL guidance.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
