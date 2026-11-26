## Description:

Smart Money analytics on OKX: leaderboard traders, position tracking, trade records, closed-position history, aggregated consensus signals, and signal history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to query OKX Smart Money leaderboard traders, trader positions, trade history, closed-position performance, and aggregated long/short signal trends through the OKX CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the OKX CLI and local OKX authentication or profile state to access live Smart Money analytics.

Mitigation: Install only when comfortable granting the OKX CLI access to local OKX authentication state, keep trading and transfer permissions separate from analytics use where possible, and never paste OKX API keys or secrets into chat.

Risk: The npm package that provides the OKX CLI is an external dependency.

Mitigation: Verify the package provenance for @okx_ai/okx-trade-cli before installation and keep the CLI updated through trusted package-management workflows.

Risk: Smart Money signal aggregation covers linear USDT- and USDS-margined instruments and can omit coin-margined exposure.

Mitigation: Cross-check a trader's full position book with trader-position commands when coin-margined exposure could materially affect interpretation.

## Reference(s):

- [OKX homepage](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-smartmoney)
- [Signal Commands Reference](references/signal-commands.md)
- [Trader Commands Reference](references/trader-commands.md)
- [Smart Money Workflows](references/workflows.md)
- [Templates & Formatting Reference](references/templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON-formatted OKX CLI results and presents read-only analytics as concise Markdown.]

## Skill Version(s):

1.4.8 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
