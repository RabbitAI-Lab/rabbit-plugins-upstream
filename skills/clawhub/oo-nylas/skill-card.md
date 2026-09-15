## Description:

Helps agents operate Nylas through an OOMOL-connected account for grant, calendar, and event retrieval using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to retrieve Nylas grants, calendars, and calendar events through an OOMOL-connected account without handling raw credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute remote installer scripts directly in a shell.

Mitigation: Install the oo CLI through a trusted, verifiable method and review installer contents before execution.

Risk: Grant, calendar, and event data may be routed through OOMOL-connected infrastructure.

Mitigation: Connect Nylas only for accounts and data approved for that routing model.

Risk: Future connector actions may write, overwrite, or remove Nylas data.

Mitigation: Require explicit user confirmation of the exact target, payload, and effect before any write or destructive action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-nylas)
- [Nylas homepage](https://www.nylas.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before command execution; command responses are JSON when --json is used.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
