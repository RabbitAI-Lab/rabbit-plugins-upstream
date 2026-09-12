## Description:

Routes Polymarket trade and bet requests through a pm-desk workflow that places orders and arms hard, trailing, and portfolio stop protection through pinned Node/MCP helpers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polyparlay](https://clawhub.ai/user/polyparlay)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and trading agents use this skill to set up a Polymarket desk for placing trades and monitoring protective exits, with dry-run stops enabled until the operator intentionally switches to live mode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live trading and protective exit behavior can affect real-money Polymarket positions, including sell authority when live mode is enabled.

Mitigation: Use a dedicated limited wallet, keep dry-run enabled during review, and switch to live mode only after intentionally confirming the wallet, policy, and exit settings.

Risk: The skill depends on pinned third-party npm packages for order placement and guard behavior.

Mitigation: Verify the packages, versions, and dependency tree before installation and before routing trades through the desk.

Risk: Transaction attribution or builderCode behavior may affect fees, routing, or revenue attribution.

Mitigation: Review the attribution and fee effects before using the desk for live trading.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/polyparlay/skills/polymarket-trade)
- [NautilusTrader Polymarket documentation](https://nautilustrader.io/docs/latest/integrations/polymarket/)
- [NautilusTrader Polymarket examples](https://github.com/nautechsystems/nautilus_trader/tree/develop/examples/live/polymarket)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires node and npm; installs pinned polymarket-place and hypelens-agent-guard dependencies.]

## Skill Version(s):

1.0.1 (source: frontmatter, scripts/package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
