## Description: <br>
Cross-chain bridge cost and time comparator for AI agents that pulls bridge quotes or estimates from Across, Stargate, Hop, Connext, Wormhole, and deBridge, then returns a ranked route recommendation with USD cost, estimated time, and hops. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ssidharhubble](https://clawhub.ai/user/ssidharhubble) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to compare bridge routes for token transfers between supported chains and select a cheapest, fastest, or balanced route before separately signing any transaction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can present estimated bridge costs as live quotes for financial routing decisions. <br>
Mitigation: Use the output only as a rough comparison aid and independently verify current quotes directly with bridge providers before signing a bridge transaction. <br>
Risk: Some providers use structural estimates or public endpoints that may be stale, unavailable, or rate-limited. <br>
Mitigation: Re-run comparisons immediately before use, inspect provider-specific quote details, and treat errors or estimates as lower-confidence than direct provider quotes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ssidharhubble/skills/bridge-cost-optimizer) <br>
- [Across suggested fees API](https://app.across.to/api/suggested-fees) <br>
- [CoinGecko simple price API](https://api.coingecko.com/api/v3/simple/price?ids={cg_id}&vs_currencies=usd) <br>
- [deBridge DLN create transaction API](https://dln.debridge.finance/v1.0/dln/order/create-tx) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text CLI summaries and tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Route recommendations include bridge name, estimated USD fee, ETA, hop count, and selection criterion.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
