## Description:

Sends proactive text, image, file, and video messages through a locally configured WorkBuddy ClawBot WeChat bot channel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noaheleven](https://clawhub.ai/user/noaheleven)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when they need an agent to send WeChat messages or attachments through an existing WorkBuddy ClawBot channel. It is intended for deliberate outbound notifications where the local recipient, credentials, and session state have already been reviewed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send real WeChat messages and attachments using local WorkBuddy credentials.

Mitigation: Require manual confirmation before sending any message or file, and verify the recipient configured in settings.json before use.

Risk: Local botToken and claw-state cursor files can expose the WorkBuddy ClawBot channel if shared.

Mitigation: Keep settings.json and claw-state cursor files private, and do not include them in backups, issues, commits, or shared artifacts.

Risk: Network or sandbox bypasses can increase exposure when sending outbound messages or uploads.

Mitigation: Avoid disabling sandbox or network controls unless the operator understands and accepts the outbound messaging exposure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/noaheleven/skills/weixinclaw-proactive-push)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger outbound WeChat text or media delivery when the generated command is executed with local WorkBuddy credentials.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
