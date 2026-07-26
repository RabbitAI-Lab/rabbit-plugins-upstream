## Description: <br>
Hyperliquid trading plugin with background position monitoring and custom automations for market orders, limit orders, position management, funding rates, strategies, and liquidation-risk alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ya7ya](https://clawhub.ai/user/ya7ya) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading operators use Open-broker to let an agent query Hyperliquid account and market data, place or manage trades, and create event-driven trading automations with monitoring and alerts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives agents live financial trading authority on Hyperliquid. <br>
Mitigation: Install only for intentional agent-assisted trading and use a dedicated low-balance or restricted API wallet. <br>
Risk: Persistent custom automations can continue trading after they are started. <br>
Mitigation: Test with testnet and dry-run mode first, keep a clear stop procedure, and monitor active automations. <br>
Risk: Generated TypeScript trading strategies may encode incorrect assumptions or unsafe position sizing. <br>
Mitigation: Inspect generated strategy code before running it live and require explicit risk parameters such as size limits and TP/SL behavior. <br>
Risk: Webhook or dashboard forwarding can disclose trading events to configured endpoints. <br>
Mitigation: Configure webhooks and dashboard URLs only to endpoints controlled by the operator. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ya7ya/skills/openbroker) <br>
- [OpenBroker npm package](https://www.npmjs.com/package/openbroker-plugin) <br>
- [Hyperliquid app](https://app.hyperliquid.xyz/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON-oriented tool calls, TypeScript automation code, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May trigger live Hyperliquid trading actions when configured with wallet credentials; informational commands can return JSON.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
