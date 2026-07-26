## Description: <br>
Helps agents plan, execute, and track Binance spot-market dollar-cost averaging purchases with scenario analysis, market or limit buys, balance and history checks, testnet support, and OpenClaw automation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fpsjago](https://clawhub.ai/user/fpsjago) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to plan recurring Binance spot purchases, run manual or scheduled DCA buys, inspect balances and trade history, and test strategies on Binance testnet before live trading. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Configured credentials can allow real recurring Binance spot buy orders. <br>
Mitigation: Use Binance testnet first, use a dedicated spot-only key with withdrawals disabled, start with small per-run amounts, and regularly review or disable scheduled jobs. <br>
Risk: Secrets stored in shell startup files or scheduled jobs can be exposed on shared systems. <br>
Mitigation: Prefer a secret manager or protected environment, restrict local file permissions, and avoid committing keys or environment files. <br>


## Reference(s): <br>
- [Binance](https://www.binance.com) <br>
- [Binance Spot Testnet](https://testnet.binance.vision/) <br>
- [Binance Support Announcements](https://www.binance.com/en/support/announcement) <br>
- [ClawHub Skill Page](https://clawhub.ai/fpsjago/skills/binance-dca) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline bash and JSON examples; shell script output is plain text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May make Binance API calls when the shell script is executed with API credentials.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata and artifact changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
