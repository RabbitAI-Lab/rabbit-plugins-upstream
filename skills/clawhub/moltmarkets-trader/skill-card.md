## Description: <br>
Moltmarkets Trader helps agents screen MoltMarkets prediction markets, form probability estimates, detect edge, size positions, place bets, create markets, resolve markets, and track calibration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[spiceoogway](https://clawhub.ai/user/spiceoogway) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents and developers use this skill to screen MoltMarkets prediction markets, estimate probabilities, size positions, place bets, create markets, resolve markets, and review account positions. It supports authenticated trading workflows and short-term market idea research. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated scripts can make live bets, create markets, place seed bets, and resolve markets without built-in confirmations. <br>
Mitigation: Use a test or least-privilege API key and require human approval outside the skill before any bet, market creation, seed bet, or resolution. <br>
Risk: create-market-with-odds.sh can create a market and then immediately place a seed bet. <br>
Mitigation: Avoid create-market-with-odds.sh until its confirmation flow and argument handling are fixed. <br>


## Reference(s): <br>
- [MoltMarkets Trader on ClawHub](https://clawhub.ai/spiceoogway/skills/moltmarkets-trader) <br>
- [MoltMarkets API](https://api.zcombinator.io/molt) <br>
- [Forecasting Guide](references/forecasting-guide.md) <br>
- [Kelly Criterion for MoltMarkets](references/kelly-criterion.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, API calls] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local shell scripts and an authenticated MoltMarkets API key when executing account or market actions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
