## Description: <br>
Send automatic Bitcoin price alerts when BTC moves ±3% or crosses key levels, using BTC-vision.org data for Telegram, Discord, or Slack notifications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[welove111](https://clawhub.ai/user/welove111) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to monitor Bitcoin price movement, sentiment changes, and user-defined BTC price thresholds for automated alerting workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill calls an external BTC-vision endpoint for price and sentiment data. <br>
Mitigation: Install only if BTC price or sentiment alerts powered by btc-vision.org are desired. <br>
Risk: The suggested hourly cron schedule can create recurring external requests and notifications. <br>
Mitigation: Review and adjust the cron schedule before enabling recurring alert checks. <br>
Risk: The sample alert template includes donation text and links. <br>
Mitigation: Edit the alert template before use if donation text or links should not appear in notifications. <br>


## Reference(s): <br>
- [Btcvision Alert on ClawHub](https://clawhub.ai/welove111/skills/btcvision-alert) <br>
- [BTC-vision.org](https://btc-vision.org) <br>
- [welove111 ClawHub profile](https://clawhub.ai/user/welove111) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with API request examples, alert template text, alert-condition logic, and cron guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces notification guidance for BTC price and sentiment alerts; it does not include executable local code.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
