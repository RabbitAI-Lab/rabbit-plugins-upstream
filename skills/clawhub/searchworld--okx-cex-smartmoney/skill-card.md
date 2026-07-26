## Description: <br>
Provides OKX Smart Money leaderboard, trader analytics, position tracking, trade records, closed-position history, aggregated consensus signals, and signal history through the OKX CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[searchworld](https://clawhub.ai/user/searchworld) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and trading analysts use this skill to query OKX Smart Money leaderboard, trader, position, trade-history, and signal analytics through the OKX CLI. The skill guides authenticated read-only queries and presents results as concise Markdown tables. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on the user's local OKX authentication profile for Smart Money queries. <br>
Mitigation: Confirm the OKX CLI package is trusted, use an OKX profile with the least permissions needed, and guide users through the documented config or OAuth flow instead of asking them to paste secrets into chat. <br>
Risk: The skill is read-only by instruction but may inspect local OKX auth and profile status to decide how to run queries. <br>
Mitigation: Review the proposed commands before execution and keep authentication setup in the OKX CLI configuration flow. <br>
Risk: Signal aggregation excludes coin-margined contracts, which can understate a trader's exposure for an asset. <br>
Mitigation: Cross-check with trader position queries when full exposure matters, especially for BTC or ETH positions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-smartmoney) <br>
- [OKX homepage](https://www.okx.com) <br>
- [Trader Commands Reference](references/trader-commands.md) <br>
- [Signal Commands Reference](references/signal-commands.md) <br>
- [Smart Money Workflows](references/workflows.md) <br>
- [Templates & Formatting Reference](references/templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown tables with inline shell commands and summarized analytics.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses JSON CLI output and requires a locally configured OKX authentication profile for authenticated read-only queries.] <br>

## Skill Version(s): <br>
1.4.0 (source: release evidence and skill frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
