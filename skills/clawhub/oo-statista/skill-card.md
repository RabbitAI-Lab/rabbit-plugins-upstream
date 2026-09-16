## Description:

Statista helps an agent search Statista content and retrieve statistic chart data and metadata through an OOMOL-connected Statista account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need an agent to search Statista statistics, Consumer Insights survey questions, Market Insights indicators, or retrieve statistic data by identifier.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Prefer a package manager or pinned release with checksum or signature verification; inspect installer contents first and run setup only after deciding to trust OOMOL's CLI installer.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-statista)
- [Statista Homepage](https://www.statista.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector action schemas before execution and returns connector responses containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
