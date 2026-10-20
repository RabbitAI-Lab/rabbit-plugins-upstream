## Description:

Analyzes OKX Smart Money trader rankings, positions, trade history, and aggregated market signals through read-only CLI queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT-0

## Use Case:

OKX users and analysts use this skill to compare traders, inspect positions and trading history, and review consensus signals for selected assets without placing trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials could be exposed during setup.

Mitigation: Use the OKX configuration or OAuth flow; never share credentials in chat.

Risk: Trader and market signals could be mistaken for financial advice.

Mitigation: Treat the results as analytics, not investment recommendations, and verify them before acting.

Risk: Aggregated signals omit coin-margined positions and can understate a trader's exposure.

Mitigation: Inspect the trader's full position list when assessing exposure.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/okx-retail/skills/okx-cex-smartmoney)
- [OKX homepage](https://www.okx.com)
- [Trader commands](references/trader-commands.md)
- [Signal commands](references/signal-commands.md)
- [Smart Money workflows](references/workflows.md)
- [Formatting templates](references/templates.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown tables and explanatory text with OKX CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated read-only analytics; aggregated signals exclude coin-margined positions.]

## Skill Version(s):

1.4.9 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
