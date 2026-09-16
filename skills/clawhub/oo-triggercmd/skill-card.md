## Description:

TRIGGERcmd lets agents list available commands and trigger saved commands on named computers through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate TRIGGERcmd from an agent session, including listing connected commands and triggering saved commands with user-confirmed parameters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running remote installer scripts directly in a shell, and those scripts can change after review.

Mitigation: Review installer source before use; prefer a verified, pinned, or inspectable oo CLI installation method when available.

Risk: The trigger_command action can change TRIGGERcmd state by running saved commands on named computers.

Mitigation: Inspect the live action schema and confirm the exact computer, command, and parameters with the user before triggering a command.

## Reference(s):

- [ClawHub TRIGGERcmd Skill](https://clawhub.ai/oomol/skills/oo-triggercmd)
- [TRIGGERcmd Homepage](https://www.triggercmd.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include connector schema checks, JSON command payloads, and connector response summaries.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
