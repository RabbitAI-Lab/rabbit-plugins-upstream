## Description: <br>
Trade Polymarket player-goal YES markets using role, minutes, penalty, and value scoring with patient limit orders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bridgeaisocial](https://clawhub.ai/user/bridgeaisocial) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and trading-system operators use this skill to scan Polymarket-imported player-goal YES markets, estimate fair value from player statistics, and place or preview disciplined limit-order ladders with configurable risk controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place live prediction-market orders that may lose money. <br>
Mitigation: Start with dry-run or `--venue sim`, keep strict position and daily budget caps, and avoid `--live` unless intentionally accepting real-money trading risk. <br>
Risk: A Simmer API key is required and misuse could authorize unwanted activity. <br>
Mitigation: Use a limited Simmer API key, keep credentials out of the repository, and rotate or revoke keys after testing. <br>
Risk: The packaged client helper bypasses a Simmer entrypoint integrity check for local edits. <br>
Mitigation: Review the packaged source and security scan before installing, and do not use the helper for production execution without explicit approval. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bridgeaisocial/skills/polymarket-world-cup-player-goal-value) <br>
- [Reference inspiration](https://x.com/Predicti0r/status/2061791808158400570) <br>
- [ESPN FIFA World Cup scoreboard API](https://site.api.espn.com/apis/site/v2/sports/soccer/fifa.world/scoreboard) <br>
- [Polymarket Gamma events API](https://gamma-api.polymarket.com/events/keyset) <br>
- [Understat league player data](https://understat.com/league/{league}/{season}) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration settings, and runtime text output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Simmer API key and supports dry-run, sim, and live venue modes.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
