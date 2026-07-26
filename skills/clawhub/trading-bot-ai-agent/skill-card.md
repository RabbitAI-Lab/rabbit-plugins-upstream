## Description: <br>
Build and evaluate an offline crypto grid-trading simulation without connecting an exchange, wallet, Telegram bot, or user account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[frederica123](https://clawhub.ai/user/frederica123) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to model hypothetical crypto grid levels, reserve estimates, fees, and path crossings while keeping the workflow offline and non-custodial. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may provide exchange keys, wallet secrets, Telegram tokens, seed phrases, or real account credentials. <br>
Mitigation: Do not request, repeat, store, or process secrets; advise revocation or rotation if sensitive material was exposed. <br>
Risk: Users may treat hypothetical grid results as trading advice or verified performance. <br>
Mitigation: Begin delivered results with a not-investment-advice disclaimer and state that outputs are simplified scenarios, not forecasts, backtests, or profit guarantees. <br>
Risk: Users may ask to restore live trading, withdrawal, wallet export, credential binding, or public server behavior. <br>
Mitigation: Refuse execution or custody requests and offer an offline simulation using non-sensitive scenario parameters. <br>


## Reference(s): <br>
- [Safety boundaries](references/safety-boundaries.md) <br>
- [ClawHub skill page](https://clawhub.ai/frederica123/skills/trading-bot-ai-agent) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown response with inline shell commands and JSON simulator output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Offline simulation only; results include a not-investment-advice disclaimer and must not be presented as forecasts or verified performance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
