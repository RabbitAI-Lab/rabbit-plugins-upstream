## Description: <br>
Perpetual futures signal scanner for Hyperliquid-style markets that reports funding rates, open-interest shifts, liquidation events, basis setups, and squeeze signals through a CLI. <br>

This skill is for demonstration purposes and not for production usage. <br>

## Publisher: <br>
[ssidharhubble](https://clawhub.ai/user/ssidharhubble) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Crypto traders, DeFi quants, basis-trade developers, and agents can use this skill as a demo CLI/template for inspecting Hyperliquid-style perp funding, open-interest, liquidation, basis, and squeeze signal outputs. Its bundled data path is mock-based and should not be used for real trading decisions without verified live exchange data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill presents trading signals as market intelligence while the bundled code generates deterministic mock data. <br>
Mitigation: Treat outputs as demo/template results only; replace mock functions with verified live exchange data before any production or trading use. <br>
Risk: Users may make real trading decisions from stale, simulated, or unlabeled data. <br>
Mitigation: Clearly label data source and freshness in the CLI and avoid using the output for trading decisions until live Hyperliquid and comparison-market integrations are implemented and validated. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ssidharhubble/skills/hyperliquid-perp-signals) <br>
- [Hyperliquid info endpoint](https://api.hyperliquid.xyz/info) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON emitted by CLI commands, with Markdown and shell command guidance in the skill documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [CLI outputs include market fields, signal labels, and scores; bundled data is deterministic mock data unless replaced with verified live exchange integrations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
