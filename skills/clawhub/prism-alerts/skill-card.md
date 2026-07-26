## Description: <br>
Real-time Pump.fun token alerts for Solana traders, trading bots, Discord, Telegram, and AI agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nextfrontierbuilds](https://clawhub.ai/user/nextfrontierbuilds) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and trading-bot builders use this skill to query PRISM Pump.fun and Solana token data and produce bonding, graduation, and watch alerts for shell, Telegram, or Discord workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Alert queries are sent to the external PRISM endpoint. <br>
Mitigation: Install only if sending alert queries to PRISM is acceptable for the intended workflow, and configure PRISM_URL deliberately. <br>
Risk: Telegram or Discord bot tokens could be exposed if stored in committed files or logs. <br>
Mitigation: Keep bot tokens in environment variables or a secret manager and avoid printing them in logs. <br>
Risk: Automated trading or public posting could amplify incorrect or stale token alerts. <br>
Mitigation: Require independent confirmation, rate limits, and cooldowns before connecting alerts to trades or public channels. <br>


## Reference(s): <br>
- [ClawHub Prism Alerts listing](https://clawhub.ai/nextfrontierbuilds/skills/prism-alerts) <br>
- [PRISM API base endpoint](https://strykr-prism.up.railway.app) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON configuration examples; script output is plain text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May query the PRISM API and poll every 30 seconds in watch mode.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
