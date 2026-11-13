## Description:

Guides agents in using the Hyperliquid CLI to inspect markets and accounts, plan trades, and carry out approved trading or asset-management actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wtfsayo](https://clawhub.ai/user/wtfsayo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to guide AI agents through Hyperliquid market and account inspection, trade planning, and explicitly approved trading, transfers, and account operations through the CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can place trades and move assets, so an incorrect or unintended command can change account state.

Mitigation: Inspect command schemas, run a dry-run, present the planned side effects, and get explicit approval before live mutations; check orders and positions afterward.

Risk: The security summary notes that CLI updating and additional trading-related capabilities are not clearly disclosed.

Mitigation: Review the available referenced material and decide whether the update and trading capabilities fit the intended use before installing or updating.

## Reference(s):

- [Hyperliquid CLI project homepage](https://github.com/hypurr-inc/hyperliquid-cli)
- [Hyperliquid CLI on ClawHub](https://clawhub.ai/wtfsayo/skills/hyperliquid-cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell commands and structured JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI results can be requested as JSON; bounded subscriptions may emit JSONL.]

## Skill Version(s):

1.1.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
