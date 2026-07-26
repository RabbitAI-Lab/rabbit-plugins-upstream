## Description: <br>
Create, trade, settle, and redeem prediction markets on Base Mainnet using ERC20 collateral through PNP Markets CLI scripts and TypeScript SDK examples. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[proxima424](https://clawhub.ai/user/proxima424) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to create prediction markets, trade YES/NO outcomes, settle completed markets, redeem winnings, and integrate PNP Markets flows into apps, bots, contests, and forecasting workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a wallet private key to submit live Base Mainnet transactions that spend funds. <br>
Mitigation: Use a dedicated low-balance wallet, verify all transaction parameters before execution, and avoid primary wallet keys. <br>
Risk: ERC20 approvals may grant persistent token-spending permissions to market contracts. <br>
Mitigation: Prefer exact or revocable approvals when possible, verify contract and token addresses independently, and revoke unused allowances after use. <br>
Risk: Create, trade, settle, and redeem examples are operational commands rather than dry-run examples. <br>
Mitigation: Run help or information-only modes first, confirm Base Mainnet addresses and wallet balances, and treat example commands as fund-moving actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/proxima424/skills/create-prediction-markets) <br>
- [Publisher profile](https://clawhub.ai/user/proxima424) <br>
- [API Reference](artifact/references/api-reference.md) <br>
- [Use Cases](artifact/references/use-cases.md) <br>
- [Examples](artifact/references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with TypeScript examples, CLI commands, and JSON transaction outputs from scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated commands may submit live Base Mainnet transactions when executed with a funded wallet private key.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; scripts/package.json agrees) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
