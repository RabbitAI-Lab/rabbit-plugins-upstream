## Description:

Telegram Bot lets agents operate Telegram Bot actions through the OOMOL `telegram` connector and `oo` CLI for reading, sending, updating, and deleting bot data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to perform Telegram Bot API tasks through an OOMOL-connected account, including messaging, webhook and update management, and chat administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Install the `oo` CLI only from a verified, pinned, or package-manager source, and review the installer before execution.

Risk: Write and destructive Telegram actions can change chat state, remove messages, alter permissions, revoke invite links, or change webhook delivery.

Mitigation: Confirm the exact action, target chat or message, and payload with the user before running tagged write or destructive actions.

Risk: Telegram action payloads may be incorrect if they are constructed from stale assumptions.

Mitigation: Inspect the live connector schema with `oo connector schema` before building each payload.

## Reference(s):

- [ClawHub Telegram Bot Skill](https://clawhub.ai/oomol/skills/oo-telegram)
- [Telegram Bot Documentation](https://core.telegram.org/bots)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Execution depends on the `oo` CLI, an authenticated OOMOL account, and a connected Telegram Bot account.]

## Skill Version(s):

1.0.4 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
