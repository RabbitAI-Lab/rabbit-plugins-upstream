## Description: <br>
The Hunter: Professional Binance Trading Skill. Features AI market analysis, auto-risk calculation, and 125x leverage support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tetravad](https://clawhub.ai/user/tetravad) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to analyze Binance markets, review trading signals, and prepare Binance spot or futures account commands. It is intended for users who deliberately want agent assistance with Binance trading workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill provides broad live Binance trading and leveraged-account instructions without enough safety scoping for real-money use. <br>
Mitigation: Use Binance testnet first, keep balances limited, and require explicit confirmation before every order, cancellation, leverage change, or other account-modifying command. <br>
Risk: Binance API credentials used with this skill can enable sensitive account operations if they are over-permissioned or exposed. <br>
Mitigation: Create separate restricted API keys, disable withdrawals, restrict keys by IP where possible, and protect the credential file. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tetravad/skills/binance-hunter) <br>
- [Binance API Documentation](https://binance-docs.github.io/apidocs/) <br>
- [Binance Testnet](https://testnet.binance.vision/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with bash, JSON, and Python examples; the analysis script returns JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, python3, Binance API credentials for account operations, and Python dependencies ccxt, pandas, and ta for analysis.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
