## Description: <br>
Binance DCA Test helps agents plan Binance dollar-cost averaging strategies and propose or run commands for manual, scheduled, and recurring Binance spot purchases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fpsjago](https://clawhub.ai/user/fpsjago) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to plan DCA strategies, check balances and trade history, project outcomes, and prepare Binance spot-buy commands or schedules. It should be used with testnet or manually confirmed live trades because it can steer an agent toward real crypto purchases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can steer an agent into live Binance crypto purchases and recurring trading without enough guardrails. <br>
Mitigation: Start on Binance testnet, require manual confirmation before live orders or schedules, and set explicit spending limits. <br>
Risk: Binance API credentials could authorize real account activity if over-scoped or mishandled. <br>
Mitigation: Use restricted spot-trading API keys with withdrawals disabled and provide credentials only through environment variables. <br>
Risk: The server security guidance notes that the dca.sh implementation is missing from the available artifact. <br>
Mitigation: Inspect the implementation before live use and verify order responses before confirming execution to a user. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fpsjago/skills/binance-dca-test) <br>
- [Binance testnet endpoint referenced by the skill](https://testnet.binance.vision) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and environment-variable configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Binance symbols, quote-currency amounts, order type, limit price, schedule examples, and testnet configuration.] <br>

## Skill Version(s): <br>
0.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
