## Description:

The Official Board connector helps agents search and read The Official Board company, executive, organizational chart, biography, colleague, news, and watchlist data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query The Official Board via an OOMOL-connected account for company lookup, executive search, organizational charts, executive biographies, direct colleagues, recent org chart news, and watchlist changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI, and the security review flags unverified remote installer scripts as the primary risk.

Mitigation: Install only through a verified, reviewed, versioned oo CLI distribution path, and do not let an agent run remote installer commands automatically or from an elevated shell.

## Reference(s):

- [The Official Board homepage](https://www.theofficialboard.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-the-official-board)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector action schemas before constructing JSON payloads; setup may require a verified oo CLI installation and connected OOMOL account.]

## Skill Version(s):

1.0.2 (source: skill metadata and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
