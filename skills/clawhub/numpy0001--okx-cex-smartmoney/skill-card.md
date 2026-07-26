## Description: <br>
Provides OKX Smart Money analytics for leaderboard traders, trader positions, trade and closed-position history, aggregate consensus signals, and signal trends through the OKX CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[numpy0001](https://clawhub.ai/user/numpy0001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill for read-only OKX Smart Money analysis, including finding top traders, reviewing trader performance and positions, and summarizing long/short consensus across selected crypto instruments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an OKX OAuth session or API-key profile for read-only Smart Money analytics. <br>
Mitigation: Use the OKX CLI authentication flow or an existing least-privileged profile; do not paste OKX credentials into chat, and review account permissions before use. <br>
Risk: Smart Money signal aggregation covers USDT- and USDS-margined linear contracts, so coin-margined exposure can be absent from consensus views. <br>
Mitigation: Cross-check a trader's full position book with trader position commands before treating signal output as complete. <br>


## Reference(s): <br>
- [OKX](https://www.okx.com) <br>
- [Trader Commands Reference](references/trader-commands.md) <br>
- [Signal Commands Reference](references/signal-commands.md) <br>
- [Smart Money Workflows](references/workflows.md) <br>
- [Templates and Formatting Reference](references/templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, markdown, configuration] <br>
**Output Format:** [Markdown with OKX CLI command snippets and tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only analytics commands should be run with --json and rendered as concise Markdown tables.] <br>

## Skill Version(s): <br>
1.3.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
