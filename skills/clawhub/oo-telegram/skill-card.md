## Description:

Telegram Bot (core.telegram.org). Use this skill for Telegram Bot requests involving reading, creating, updating, and deleting data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Telegram Bot accounts through OOMOL, including message sending, chat administration, webhook management, updates, and bot profile checks. It supports both read-only bot inspection and user-confirmed write or destructive Telegram actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform broad Telegram write, moderation, webhook, and delete actions through an intermediary service.

Mitigation: Grant only the bot capabilities needed for the intended chats and require explicit confirmation before any send, edit, moderation, webhook, or delete action.

Risk: The setup path includes remote installer commands for the oo CLI.

Mitigation: Prefer a verified or package-manager install path for the oo CLI before using the connector.

## Reference(s):

- [Telegram Bot homepage](https://core.telegram.org/bots)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-telegram)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
