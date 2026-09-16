## Description:

Token Metrics lets agents retrieve cryptocurrency market data and trading signals through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Token Metrics for current prices, OHLCV records, token listings, market-cap rankings, and trading signals through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer scripts that an agent could run directly in a shell.

Mitigation: Install the oo CLI only through a verified, user-controlled method and review setup commands before execution.

Risk: Token Metrics access is mediated through OOMOL rather than direct user-managed API tokens.

Mitigation: Use the skill only when the user accepts OOMOL-mediated Token Metrics access and has connected the account intentionally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-token-metrics)
- [Token Metrics homepage](https://www.tokenmetrics.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Token Metrics connection](https://console.oomol.com/app-connections?provider=token_metrics)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live Token Metrics results depend on the user's authenticated OOMOL connection and the action schema returned by the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
