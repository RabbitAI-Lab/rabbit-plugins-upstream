## Description:

This skill lets agents search and read Avoma meetings, recordings, transcriptions, meeting insights, and users through the OOMOL-connected Avoma connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Avoma meeting data, recordings, transcriptions, insights, and user records through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute changing code on a user machine.

Mitigation: Install the oo CLI only from a verified release or package manager, and apply version and integrity checks before running connector actions.

Risk: Avoma meeting and transcription data may contain sensitive business or personal information routed through the OOMOL connector.

Mitigation: Connect Avoma only when authorized for the target account and avoid requesting meeting, recording, transcription, or user data beyond the user's task.

## Reference(s):

- [ClawHub Avoma Skill](https://clawhub.ai/oomol/skills/oo-avoma)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Avoma Homepage](https://www.avoma.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Avoma Connection Setup](https://console.oomol.com/app-connections?provider=avoma)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; read actions return Avoma data visible to the connected account.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
