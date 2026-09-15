## Description:

Minerstat lets an agent search and read Minerstat data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Minerstat coin profitability, market data, hardware benchmarks, and mining pool terms from an OOMOL-connected Minerstat account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts.

Mitigation: Review the setup path before installing and prefer a verified, versioned oo CLI installation method.

Risk: The skill queries data through an OOMOL-connected Minerstat account.

Mitigation: Connect Minerstat/OOMOL only when you intend the agent to query that account's mining data.

## Reference(s):

- [ClawHub Minerstat Skill](https://clawhub.ai/oomol/skills/oo-minerstat)
- [Minerstat Homepage](https://minerstat.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector commands return JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: evidence release.version and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
