## Description:

Alpha Vantage (alphavantage.co) support for searching and reading market, company, forex, crypto, commodity, macroeconomic, and related financial data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to let an agent retrieve Alpha Vantage market data, company fundamentals, technical indicators, news sentiment, and symbol search results without handling raw Alpha Vantage API keys directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes commands that pipe remote installer scripts directly into a shell.

Mitigation: Review OOMOL's official installation options and prefer a version-pinned installer with checksum or signature verification before installing the oo CLI.

Risk: Agent-generated Alpha Vantage requests may use an incorrect action payload if the connector schema has changed.

Mitigation: Inspect the live action schema with the oo CLI before constructing each payload.

Risk: Financial data returned by the connector may be incomplete, delayed, or unsuitable as the sole basis for decisions.

Mitigation: Treat returned market and company data as informational and validate important outputs against authoritative sources before acting on them.

## Reference(s):

- [Alpha Vantage homepage](https://www.alphavantage.co)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-alpha-vantage)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include Alpha Vantage response data returned by the oo CLI as JSON.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
