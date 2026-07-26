## Description: <br>
Boiling Point helps agents launch and trade omnichain tokens through the Token Layer API across Base, Solana, Ethereum, and BNB. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrisciszak](https://clawhub.ai/user/chrisciszak) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to check Token Layer wallet balances, create on-chain token launch transactions, quote trades, submit transactions, and inspect token portfolios or rewards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A funded Token Layer API key can be used to submit real on-chain transactions, and completed on-chain actions may be public and difficult or impossible to reverse. <br>
Mitigation: Use a dedicated low-balance wallet/API key and verify the chain, token ID, amount, recipient, fees, and transaction data before each /send-transaction call. <br>
Risk: The skill supports crypto token launching and trading workflows that can move funds or create public assets. <br>
Mitigation: Install only when the operator intends to let an agent assist with token creation or trading, and require human approval before executing transaction-submission steps. <br>


## Reference(s): <br>
- [Boiling Point Skill Page](https://clawhub.ai/chrisciszak/skills/boiling-point) <br>
- [Boiling Point Homepage](https://boilingpoint.ai) <br>
- [Token Layer Agent Wallets](https://app.tokenlayer.network/agent-wallets) <br>
- [Token Layer API Base](https://api.tokenlayer.network/functions/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with endpoint tables, parameter summaries, and inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires jq, curl, and TOKENLAYER_API_KEY.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
