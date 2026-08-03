## Description: <br>
Routes crypto trade signal, market analysis, price data, news sentiment, Telegram publishing, x402 wallet, signal performance, and automated crypto signals operations requests to the appropriate agent in the crypto-signals-plugin team. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vizionik25](https://clawhub.ai/user/vizionik25) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to route 24/7 crypto signals workflows across market data, news analysis, x402 wallet payments, signal generation, Telegram publishing, and health checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill routes workflows that can use long-lived wallet secrets and scheduled x402 spending. <br>
Mitigation: Use only a low-balance wallet, strict spend caps, locked-down environment file permissions, and inspect referenced scripts before enabling automated actions. <br>
Risk: The skill routes automated Telegram publishing that may affect a public or production channel. <br>
Mitigation: Use a dedicated Telegram bot and channel until behavior is reviewed, tested, and approved for the intended audience. <br>
Risk: The skill is designed for scheduled 24/7 operation with limited per-action user control. <br>
Mitigation: Keep a clear way to disable cron, scheduler, or systemd jobs, and monitor state and log files for errors, spend caps, and pause conditions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vizionik25/skills/crypto-signals-router) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with routing tables, shell commands, cron entries, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces routing guidance for named agents and scheduled crypto signals operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
