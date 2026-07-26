## Description: <br>
AI trading bot untuk BTC, ETH, dan SOL. <br>

This skill is for demonstration purposes and not for production usage. <br>

## Publisher: <br>
[yusufid2](https://clawhub.ai/user/yusufid2) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users can use this skill to request crypto prices, rule-based signals, paper-trade actions, portfolio status, and simple trade history for BTC, ETH, and SOL. It should be treated as a paper-trading demo, not financial advice or a live trading system. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security evidence marks the package suspicious because identity metadata is inconsistent and an unrelated shell-based chat wrapper can execute commands unsafely if run directly. <br>
Mitigation: Review the package carefully before installing, avoid the extra index. chat wrapper unless it is fixed to avoid shell interpolation, and scan the package before deployment. <br>
Risk: The tool performs paper-trading actions and can repeatedly call Binance APIs when run.sh is left running. <br>
Mitigation: Treat outputs as simulation only, not financial advice or live trading instructions, and run the loop only when repeated local paper-trade updates and Binance API calls are intentional. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yusufid2/my-skill) <br>
- [Publisher profile](https://clawhub.ai/user/yusufid2) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration] <br>
**Output Format:** [Console text with JSON-like command results and local JSON state files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local JSON files for prices, trade state, and trade history.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
