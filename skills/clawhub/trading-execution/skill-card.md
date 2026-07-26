## Description: <br>
Trading Execution helps agents provide market monitoring workflows, Upbit automated trading commands, asset allocation guidance, scheduled trading tasks, and trading safety reminders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cooperiano](https://clawhub.ai/user/cooperiano) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Traders, portfolio managers, and developers use this skill to draft market monitoring, Upbit breakout trading, asset allocation, rebalancing, and scheduled trading workflows for agent-assisted execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automated trading workflows can place real trades or cause financial loss if executed without review, limits, or appropriately scoped credentials. <br>
Mitigation: Require explicit confirmation for live trading, use scoped exchange keys, store keys securely, set daily loss limits, and test strategies before real execution. <br>
Risk: Scheduled trading tasks can run with stale assumptions, incorrect budgets, or unintended timing. <br>
Mitigation: Review cron schedules, strategy settings, and budget values before enabling automation, then monitor execution outcomes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/cooperiano/skills/trading-execution) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and cron entries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes trading safety reminders for confirmations, loss limits, secure key storage, and avoiding high-frequency leverage.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
