## Description:

pingroom lets an OpenClaw agent use the PingRoom CLI to send phone notifications, ask questions, gate actions on approvals, deliver handoffs, drive live progress cards, and stream incoming pings with user-approved data sharing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pingroom](https://clawhub.ai/user/pingroom)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and OpenClaw users use pingroom when an agent needs to notify or ask a human, request approval before an action, send agreed files, links, or locations to a phone, or keep a human updated while work runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PingRoom commands can transmit message text, attachments, links, locations, room messages, urgent notifications, and approval requests to the PingRoom service and paired phones.

Mitigation: Install and use the skill only when that contact path is intended, send the minimum data needed, and confirm before sharing files, locations, links, public room messages, or urgent notifications.

Risk: PingRoom tokens and credentials.json grant access to the paired PingRoom account or robot profile.

Mitigation: Treat the token or credentials file like a password, scope it to this skill where possible, keep credentials readable only by the owner, and avoid exposing them in logs or room messages.

Risk: Using an unreviewed CLI version or regenerated lockfile could change the behavior of phone notifications, approvals, attachment handling, or credential use.

Mitigation: Use the bundled runtime lockfile, verify the pinned @pingroom/cli 0.12.0 installation, and update dependencies only through a reviewed skill release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pingroom/skills/pingroom)
- [PingRoom OpenClaw connection guide](https://pingroom.io/connect-openclaw.md)
- [Reviewed PingRoom CLI source commit](https://github.com/pingroom/cli/tree/927e0212dc16464da043affde41ed9190c48f86f)
- [Bundled runtime manifest](runtime/package.json)
- [Bundled runtime lockfile](runtime/package-lock.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, JSON]

**Output Format:** [Markdown guidance with shell commands, configuration snippets, and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing instructions for invoking the pinned PingRoom CLI; commands may send messages, attachments, links, locations, approvals, or notifications to the PingRoom service when the user authorizes that sharing.]

## Skill Version(s):

1.2.1 (source: SKILL.md frontmatter, runtime/package.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
