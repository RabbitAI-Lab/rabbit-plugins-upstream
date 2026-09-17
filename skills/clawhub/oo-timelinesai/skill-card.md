## Description:

TimelinesAI (timelines.ai). Use this skill for ANY TimelinesAI request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate a TimelinesAI workspace through the OOMOL TimelinesAI connector, including workspace, chat, message, message-status, WhatsApp-account lookup, and confirmed plain-text message sending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote script execution for installing the OOMOL CLI.

Mitigation: Review the OOMOL CLI installation source first and prefer a signed or package-manager install path with checksum verification; do not let an agent run the remote installer automatically.

Risk: Message-sending actions can change TimelinesAI or WhatsApp state.

Mitigation: Confirm the exact payload and intended effect with the user before running send-message actions.

## Reference(s):

- [TimelinesAI homepage](https://timelines.ai/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-timelinesai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action execution; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
