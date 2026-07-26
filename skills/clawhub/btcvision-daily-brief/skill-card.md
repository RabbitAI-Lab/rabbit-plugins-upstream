## Description: <br>
Auto-generates a daily Bitcoin market brief from BTC-vision.org with price, halving countdown, Fear & Greed, and AI prediction details for channel delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[welove111](https://clawhub.ai/user/welove111) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to assemble daily Bitcoin market summaries and optionally send them to Telegram, Discord, or Slack channels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automated channel delivery could publish a market brief to a public, shared, or sensitive destination. <br>
Mitigation: Configure Telegram, Discord, or Slack destinations deliberately and use preview or confirmation before posting to sensitive channels. <br>
Risk: Scheduled runs could publish a brief without an operator noticing the timing or audience. <br>
Mitigation: Treat the cron example as opt-in automation and review scheduled delivery settings before enabling it. <br>


## Reference(s): <br>
- [BTC-vision.org](https://btc-vision.org) <br>
- [BTC-vision MCP endpoint](https://btc-vision.org/.netlify/functions/mcp) <br>
- [ClawHub skill page](https://clawhub.ai/welove111/skills/btcvision-daily-brief) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, shell commands, guidance] <br>
**Output Format:** [Markdown brief with API request examples and optional channel-delivery guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses BTC-vision.org as the external data source; evidence indicates no API key requirement.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
