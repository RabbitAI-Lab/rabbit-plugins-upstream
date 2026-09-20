## Description:

Microsoft Teams (microsoft.com). Use this skill for ANY Microsoft Teams request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and workspace operators use this skill to read Microsoft Teams data and send or reply to Teams messages through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read Microsoft Teams data and perform message write actions through an OOMOL-connected account.

Mitigation: Install only if OOMOL is trusted with Teams access, and confirm exact recipients, channels, and message contents before write actions.

Risk: The first-time setup includes pipe-to-shell CLI installer commands.

Mitigation: Review the oo CLI installer before running setup commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-microsoft-teams)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL Microsoft Teams connection](https://console.oomol.com/app-connections?provider=microsoft_teams)
- [Microsoft Teams homepage](https://www.microsoft.com/microsoft-365/microsoft-teams/group-chat-software)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
