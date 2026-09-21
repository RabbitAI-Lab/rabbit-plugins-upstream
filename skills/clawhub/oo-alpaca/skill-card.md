## Description:

Alpaca helps agents access an OOMOL-connected Alpaca account for account, market data, order, position, asset, watchlist, news, and portfolio-history queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent inspect Alpaca trading-account information and market data through the OOMOL oo CLI connector. It is suited to read-oriented workflows such as checking account details, portfolio history, assets, market calendar data, news, orders, positions, and watchlists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive Alpaca account data, including orders, positions, activities, watchlists, and portfolio history.

Mitigation: Install only from the trusted publisher, connect only the intended Alpaca account, and review agent requests before sharing or acting on account data.

Risk: The setup guidance includes a conditional remote pipe-to-shell installer for the oo CLI.

Mitigation: Do not let an agent run the remote installer automatically; review the install source and prefer a verified installation path before authenticating.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-alpaca)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [Alpaca Homepage](https://alpaca.markets/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to fetch live action schemas before sending JSON payloads through the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
