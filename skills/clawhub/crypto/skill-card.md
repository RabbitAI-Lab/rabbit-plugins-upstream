## Description: <br>
Cryptocurrency market data and price alert monitoring tool based on CCXT. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manifoldor](https://clawhub.ai/user/manifoldor) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query cryptocurrency market data, inspect order books and candles, monitor live prices, and manage local threshold or percentage-change alerts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Price queries contact the selected cryptocurrency exchange through CCXT. <br>
Mitigation: Review network and exchange API policies before running the CLI, and pass --exchange explicitly when a specific exchange is required. <br>
Risk: The documentation and script disagree about the default exchange. <br>
Mitigation: Specify --exchange in commands instead of relying on the default. <br>
Risk: Alert rules are stored locally in ~/.config/crypto/alerts.json. <br>
Mitigation: Review or remove the local alert file when sharing systems, and avoid storing sensitive information in alert values or copied examples. <br>
Risk: Reference examples mention private exchange API keys for advanced CCXT use. <br>
Mitigation: Do not put real exchange API keys into copied examples; normal market monitoring does not require private keys. <br>


## Reference(s): <br>
- [CCXT Documentation](https://docs.ccxt.com/) <br>
- [CCXT GitHub Repository](https://github.com/ccxt/ccxt) <br>
- [Supported Exchanges](references/exchanges.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/manifoldor/skills/crypto) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples; CLI output is terminal text and local JSON alert configuration.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Price queries contact the selected exchange through CCXT, and alert rules are stored at ~/.config/crypto/alerts.json.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
