## Description: <br>
Evaluate potential BTC bottom zones with AgentKey-powered crypto market, sentiment, on-chain, ETF flow, and technical confluence signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zzallenn](https://clawhub.ai/user/zzallenn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and crypto analysts use this skill to assess whether BTC is near a potential bottom by combining live market, sentiment, on-chain, ETF flow, and technical evidence. It produces research-oriented confluence scoring with uncertainty and invalidation conditions, not financial advice or buy/sell orders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Relevant crypto-analysis requests can contact AgentKey and may require OAuth or an AgentKey API key. <br>
Mitigation: Connect AgentKey only when comfortable with that third-party data path, and avoid using the skill in conversations containing unrelated sensitive information. <br>
Risk: The skill produces analytical BTC bottom research that could be mistaken for financial advice. <br>
Mitigation: Keep outputs framed as confluence analysis with uncertainty, invalidation conditions, and no direct buy or sell recommendations. <br>


## Reference(s): <br>
- [AgentKey Tool Reference](references/agentkey-tools.md) <br>
- [BTC Bottom Signals on ClawHub](https://clawhub.ai/zzallenn/skills/btc-bottom-signals) <br>
- [AgentKey MCP Endpoint](https://api.agentkey.app/v1/mcp) <br>
- [AgentKey Console](https://console.agentkey.app/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown report with a verdict, evidence table, bottom checklist, invalidation conditions, and method summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes AgentKey endpoints used, call count, approximate credits, and separation of confirmed data from inference.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
