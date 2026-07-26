## Description: <br>
Trade on UniClaw prediction markets. Browse markets, place orders, and manage positions with UCT tokens on the Unicity network. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jvsteiner](https://clawhub.ai/user/jvsteiner) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agents use this skill to interact with UniClaw prediction markets: register an account, inspect markets, deposit UCT, place or cancel yes/no orders, review balances and positions, and withdraw funds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can move UCT and change live trading state through deposits, orders, cancellations, withdrawals, and the smoke test. <br>
Mitigation: Use a dedicated low-balance or testnet Unicity wallet and manually confirm every deposit amount, order, cancellation, and withdrawal destination before execution. <br>
Risk: Users depend on the UniClaw service endpoint and the third-party publisher for market data and trade execution. <br>
Mitigation: Install only if the UniClaw service and publisher are trusted, and verify the UNICLAW_SERVER value before running scripts. <br>
Risk: The skill handles raw wallet key material with limited safeguards. <br>
Mitigation: Keep wallet directories scoped to this use case, avoid funded production wallets, and do not run the smoke test on a funded account unless live state changes are acceptable. <br>


## Reference(s): <br>
- [UniClaw API Reference](references/api.md) <br>
- [UniClaw Skill Page](https://clawhub.ai/jvsteiner/skills/uniclaw) <br>
- [UniClaw API Service](https://api.uniclaw.app) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and command output text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js, npx, the tsx package, and a configured Unicity wallet.] <br>

## Skill Version(s): <br>
0.2.1 (source: evidence.release.version and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
