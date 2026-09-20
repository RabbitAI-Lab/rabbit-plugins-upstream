## Description:

Helps agents operate Alpha Vantage through an OOMOL-connected account for market data queries and research workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to retrieve Alpha Vantage stocks, ETFs, forex, crypto, options, fundamentals, corporate events, news, and macroeconomic data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes running a remotely fetched installer script directly in a shell.

Mitigation: Review the setup path before installing and prefer a verified package, checksum, or signature flow for the oo CLI.

Risk: The listed write capability is unclear for Alpha Vantage actions.

Mitigation: Treat write-tagged actions as requiring user confirmation until the publisher clarifies whether any provider-side state can change.

## Reference(s):

- [Alpha Vantage homepage](https://www.alphavantage.co)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-alpha-vantage)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; Alpha Vantage responses include data and execution metadata.]

## Skill Version(s):

1.0.5 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
