## Description:

Manage Grid bots (spot/contract/coin-margined) and DCA Martingale bots (Spot DCA 现货马丁 / Contract DCA 合约马丁) on OKX. Covers create, stop, amend, monitor P&L, TP/SL, margin/investment adjustment, and AI-recommended parameters. Requires API credentials. Not for regular orders (okx-cex-trade), market data (okx-cex-market), or account info (okx-cex-portfolio).

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage OKX grid and DCA trading bots through the OKX CLI, including creating, amending, stopping, listing, and monitoring bot positions. It is intended for bot workflows only, not regular orders, market data, or account portfolio tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent live financial trading authority for OKX Grid and DCA bots, including leveraged bot creation and stop actions that can sell assets or close positions.

Mitigation: Use demo mode first, grant only limited API permissions, start with small sizes, and require explicit confirmation of live/demo mode, leverage, stopType, and whether assets or positions will be sold or closed before every create, amend, or stop action.

Risk: API credentials could be exposed if users paste secrets into chat during setup or troubleshooting.

Mitigation: Do not accept credentials in chat; guide users to `okx config init` and verify authentication with the documented local status commands.

Risk: Incorrect bot identifiers, bot types, TP/SL pairs, or insufficient-balance handling can cause failed commands or unintended trading outcomes.

Mitigation: List existing bots before acting, use `algoId` and `algoOrdType` from OKX command output, respect mutually exclusive TP/SL parameters, and report funding shortfalls instead of transferring funds automatically.

## Reference(s):

- [OKX](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-bot)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, API Calls]

**Output Format:** [Markdown with inline shell commands and JSON CLI outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live or demo trading mode annotations, OKX bot identifiers, and command verification steps.]

## Skill Version(s):

1.4.8 (source: server release metadata and skill metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
