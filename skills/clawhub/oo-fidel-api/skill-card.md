## Description:

Fidel API (fidel.uk) helps agents search and read Fidel API data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to inspect Fidel API connector schemas and run read-only brand, card, and transaction lookups through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include mutable remote installer scripts that are piped directly into bash or PowerShell.

Mitigation: Review the oo CLI installation path before installing and prefer an official, versioned, checksum- or signature-verified installer.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-fidel-api)
- [Fidel API Homepage](https://fidel.uk)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill uses live connector schemas to shape action payloads before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
