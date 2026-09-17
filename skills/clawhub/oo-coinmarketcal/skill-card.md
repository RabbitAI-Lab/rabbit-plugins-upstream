## Description:

CoinMarketCal helps agents search and read CoinMarketCal data through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to list CoinMarketCal coins, categories, confirmed events, general events, and ranked events through an authenticated OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Review and verify the oo CLI installer from a trusted OOMOL release or package source before installation, and do not let an agent run the installer automatically.

Risk: Authentication, connection, or billing failures can interrupt connector use.

Mitigation: Only run sign-in, connection, or billing setup steps after a matching command failure and keep those steps under user control.

## Reference(s):

- [CoinMarketCal Skill Page](https://clawhub.ai/oomol/skills/oo-coinmarketcal)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before request construction and returns structured connector responses with execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
