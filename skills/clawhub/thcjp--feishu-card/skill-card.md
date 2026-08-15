## Description:

向协作平台用户或群组发送支持 Markdown、标题、按钮、图片和多种风格的人格化富交互卡片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, teams, and automation workflows use this skill to prepare and send Feishu/Lark-style rich cards for notifications, alerts, reports, screenshots, and AI assistant messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad and inconsistent routing text could cause external messages or uploads when users expected only writing help.

Mitigation: Use the skill only when explicitly intending to send a Feishu/Lark-style card to a specified user or group, and require a confirmation step before delivery.

Risk: Card content, screenshots, logs, or local image files may include secrets or sensitive data before being sent or uploaded.

Mitigation: Avoid passing secrets, private logs, screenshots, or sensitive local files unless the recipient and platform upload are intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/feishu-card)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires configured Feishu/Lark-style credentials and explicit recipient IDs; uses text-file workflows for Markdown that contains shell-sensitive characters.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.4.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
