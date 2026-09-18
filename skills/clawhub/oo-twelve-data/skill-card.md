## Description:

Twelve Data helps agents inspect connector schemas and retrieve market prices, quotes, end-of-day data, instrument metadata, market status, market movers, and OHLCV time series through a user's OOMOL-connected Twelve Data account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent operators use this skill to query Twelve Data market information through OOMOL without handling raw API tokens. It is suited for read-oriented workflows such as symbol lookup, stock and forex metadata discovery, quote retrieval, exchange status checks, and historical OHLCV analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions execute downloaded Bash or PowerShell installer scripts directly in a shell.

Mitigation: Review the setup path before installing, prefer an official version-pinned signed or checksum-verified oo CLI installer, and run setup only when an auth or connection error requires it.

## Reference(s):

- [ClawHub Twelve Data Skill](https://clawhub.ai/oomol/skills/oo-twelve-data)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Twelve Data Homepage](https://twelvedata.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, JSON payload guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to inspect live action schemas before running read-oriented Twelve Data connector commands; connector responses are JSON.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
