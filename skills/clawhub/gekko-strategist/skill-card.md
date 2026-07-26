## Description: <br>
AI-powered DeFi strategy development agent that designs, backtests, adapts, and evaluates yield farming strategies based on market conditions, risk profiles, and capital allocation goals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gekkoai001](https://clawhub.ai/user/gekkoai001) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and DeFi users use this skill to request strategy recommendations, backtests, adaptations, and comparisons for yield farming on Base. It supports planning and evaluation; it does not execute transactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Strategy details provided by the user may be sent to a remote service. <br>
Mitigation: Do not include wallet private keys, seed phrases, exchange credentials, or unnecessary sensitive financial data. <br>
Risk: DeFi strategy recommendations and backtests may be incorrect, stale, or unsuitable for the user's risk profile. <br>
Mitigation: Independently verify recommendations and backtest results before acting on them; execution still requires explicit wallet signing outside this skill. <br>


## Reference(s): <br>
- [Gekko Strategist ClawHub page](https://clawhub.ai/gekkoai001/skills/gekko-strategist) <br>
- [Gekko Strategist API endpoint](https://gekkoterminal.ai/api/a2a?agent=strategist) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with JSON API request examples and strategy or performance summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports market condition, risk tolerance, time horizon, capital, strategy objects, and backtest date ranges as API parameters.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
