## Description:

Chatwork (go.chatwork.com). Use this skill for ANY Chatwork request: reading, creating, updating, and deleting data through a connected Chatwork account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to let an agent read Chatwork rooms, messages, members, contacts, profiles, and tasks, and to perform approved message and task updates through a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to execute remote installer scripts directly.

Mitigation: Review the installer source before running it and prefer a signed or checksum-verified oo CLI installation method.

Risk: Write and destructive Chatwork actions can change or remove messages and tasks.

Mitigation: Require explicit user approval for the exact target, payload, and expected effect before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chatwork)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Chatwork homepage](https://go.chatwork.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include action payloads and confirmation prompts for state-changing Chatwork operations.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
