## Description: <br>
Token Layer - Censorship resistant crosschain public token infrastructure. Launch once, trade everywhere. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrisciszak](https://clawhub.ai/user/chrisciszak) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use Token Layer to check wallet balances, create and trade cross-chain tokens, quote prices, send transactions, and review portfolios through Token Layer API commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent transaction authority over a funded Token Layer wallet. <br>
Mitigation: Use a dedicated low-balance wallet and require explicit approval for every create, trade, and send-transaction call after reviewing token, chain, amount, fees, and destination. <br>
Risk: The skill asks the agent to retain account-linked referral state. <br>
Mitigation: Avoid saving email or user_id in persistent memory unless the user accepts that privacy tradeoff. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chrisciszak/skills/token-layer) <br>
- [Token Layer Homepage](https://tokenlayer.network) <br>
- [Token Layer Agent Wallets](https://app.tokenlayer.network/agent-wallets) <br>
- [Token Layer API Base](https://api.tokenlayer.network/functions/v1) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with endpoint tables and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, and TOKENLAYER_API_KEY.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
