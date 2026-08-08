## Description:

Sends proactive text, image, file, and video messages through a WorkBuddy-connected ClawBot WeChat bot channel using local WorkBuddy credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noaheleven](https://clawhub.ai/user/noaheleven)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and WorkBuddy users use this skill to have an agent send intentional WeChat bot messages or media to a configured contact through the local ClawBot channel. It is intended for explicit push requests such as sending text, images, files, or videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local WorkBuddy bot credentials and cursor data that can authorize outbound WeChat messages.

Mitigation: Install and run it only when that behavior is intended; keep WorkBuddy settings and cursor files local, and do not paste, share, or commit credential material.

Risk: Outbound text, image, file, or video pushes may send unintended content to the configured contact.

Mitigation: Use explicit ClawBot-specific prompts and confirm the recipient, message content, and media paths before executing the send command.

Risk: Disabling sandbox protections for network access increases exposure during message or media upload.

Mitigation: Keep sandbox protections enabled where possible; if network access must be allowed, use a controlled environment limited to the required WeChat and Tencent endpoints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/noaheleven/skills/weixinclawbot)
- [Artifact README](artifact/README.md)
- [Artifact skill instructions](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional message content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May result in outbound WeChat bot messages or media uploads when the local send script is executed.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
