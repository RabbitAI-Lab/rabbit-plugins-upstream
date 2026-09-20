## Description:

Operates Telegram Bot accounts through OOMOL's Telegram connector and oo CLI for reading bot data, sending messages, and administering chats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Telegram Bot workflows from an agent, including reading bot and chat data, sending messages or media, managing webhooks, and administering chat membership.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can run a remote installer script on the user's machine.

Mitigation: Review the OOMOL CLI installation path before installing and prefer an official package or a downloaded installer that can be inspected and verified.

Risk: Telegram Bot actions can send messages, delete content, ban or promote users, configure webhooks, or act through business-message permissions.

Mitigation: Connect only a Telegram Bot account whose permissions match the intended delegation, and confirm the exact target, payload, and effect before write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-telegram)
- [Telegram Bot documentation](https://core.telegram.org/bots)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector executions produce JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
