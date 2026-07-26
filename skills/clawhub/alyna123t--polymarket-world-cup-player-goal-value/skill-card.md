## Description: <br>
Trade Polymarket player-goal YES markets (World Cup + league + match props) using role/minutes/penalty/value scoring and patient limit orders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alyna123t](https://clawhub.ai/user/alyna123t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External traders and agent operators use this skill to scan Polymarket-imported player-goal markets, estimate fair YES prices from Understat player data, and place dry-run, simulated, or live orders with configurable edge, liquidity, cooldown, and budget controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place live prediction-market trades and those trades can lose money. <br>
Mitigation: Start in dry-run or sim mode, keep the default low budget and position caps, and enable live trading only after reviewing the strategy and fill behavior. <br>
Risk: The skill requires a Simmer API key, which grants access to account and trading functions. <br>
Mitigation: Store the API key only in the intended environment variable, limit access to the runtime environment, and rotate the key if it may have been exposed. <br>
Risk: Live execution behavior differs by venue, and the security guidance flags execution ambiguity outside the preferred Polymarket path. <br>
Mitigation: Prefer live Polymarket mode when priced GTC limit orders are expected, and review or modify the code before using Kalshi/live or expanding beyond World Cup player-goal markets. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/alyna123t/polymarket-world-cup-player-goal-value) <br>
- [Publisher Profile](https://clawhub.ai/user/alyna123t) <br>
- [Understat League Data](https://understat.com/league/{league}/{season}) <br>
- [Simmer Markets API](https://api.simmer.markets) <br>
- [Reference Inspiration](https://x.com/Predicti0r/status/2061791808158400570) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown guidance with bash commands, plus text or JSON terminal output from the bundled scripts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce dry-run order previews, simulated account state, or live trade requests depending on command flags, venue, and credentials.] <br>

## Skill Version(s): <br>
0.1.6 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
