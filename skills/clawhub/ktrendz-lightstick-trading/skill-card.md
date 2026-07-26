## Description: <br>
Trade K-pop artist lightstick tokens using bonding curve prices, real-time signals, and news to buy or sell with a daily limit and fee structure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hans1329](https://clawhub.ai/user/hans1329) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to check K-Trendz lightstick token prices, review trading signals, and execute one-token buy or sell orders through the K-Trendz bot API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can execute live buy and sell transactions without a built-in confirmation step. <br>
Mitigation: Confirm the artist, estimated cost or refund, fees, and slippage before every buy or sell. <br>
Risk: The setup script can save a K-Trendz API key in ~/.config/ktrendz/config.json. <br>
Mitigation: Only use the skill with a trusted K-Trendz API key and remove the saved config file when credentials should no longer be available. <br>
Risk: Trading output can influence financial decisions while prices, fees, and slippage may change. <br>
Mitigation: Review price, news, trend signals, round-trip fees, daily limits, and slippage tolerance before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hans1329/skills/ktrendz-lightstick-trading) <br>
- [K-Trendz bot API](https://k-trendz.com/api/bot/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell command results and trading summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include token prices, buy costs, sell refunds, trend signals, transaction status, and transaction hashes.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
