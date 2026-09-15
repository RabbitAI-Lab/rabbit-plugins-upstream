## Description:

Meituan enables agents to search and read Meituan travel data through the OOMOL oo CLI and a connected Meituan account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to query Meituan travel information, including flights, trains, hotels, attractions, itineraries, and local transportation, with inputs shaped from the live connector schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include remote installer commands piped directly into a shell.

Mitigation: Prefer an official, versioned installer or inspect and verify the downloaded script before running it; avoid running installer commands from an elevated terminal.

Risk: The skill should query Meituan travel data only through the user's connected OOMOL account.

Mitigation: Use normal operation for read-only Meituan travel queries and confirm user intent before any action marked write or destructive.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-meituan)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Meituan Homepage](https://www.meituan.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; travel queries may require a timeout longer than 120 seconds.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
