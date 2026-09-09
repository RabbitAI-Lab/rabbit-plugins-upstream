## Description:

Sends proactive WeChat text, image, file, and video messages to the WorkBuddy-configured boss contact through the ClawBot weixinClawBot channel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noaheleven](https://clawhub.ai/user/noaheleven)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when an agent needs to send confirmed status updates, reports, screenshots, or files to a configured WeChat recipient through WorkBuddy's ClawBot channel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send WeChat text and media using local bot credentials without a built-in confirmation boundary.

Mitigation: Require the agent workflow to preview the exact recipient, message, and attachments, and require explicit user confirmation before running send.js.

Risk: Messages and attachments are sent through Tencent/WeChat infrastructure and may include confidential content.

Mitigation: Use the skill only for content approved for that channel, and avoid sending sensitive material unless the user accepts that external transmission.

Risk: The skill reads local WorkBuddy settings and WeChat cursor state that can contain bot credentials or credential mirrors.

Mitigation: Review local settings before use, keep cursor and settings files out of shared artifacts, and avoid exposing token values in prompts, logs, issues, or commits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/noaheleven/skills/weixinclawbot)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown or terminal command guidance for sending outbound WeChat text and media messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute Node.js commands that read local WorkBuddy settings and send outbound messages or media through Tencent/WeChat infrastructure.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
