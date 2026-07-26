## Description: <br>
Autonomous AI trading agent for Simul8or, a live market simulator. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[day-trading-simulator](https://clawhub.ai/user/day-trading-simulator) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to configure an autonomous agent that watches market data, keeps local price history, manages a Simul8or watchlist, and places simulator trades through the Simul8or API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can set up persistent autonomous simulator trading every 5 minutes and persist across restarts. <br>
Mitigation: Enable it only intentionally, review the cron and PM2 startup settings, define trade limits, and confirm how to stop the schedule before use. <br>
Risk: The skill stores local market state and price history files in the user's home directory. <br>
Mitigation: Review and periodically clean up ~/market-state.json, ~/price-history.jsonl, and ~/commands.json according to the user's retention needs. <br>
Risk: The skill uses a Simul8or API key to place simulator trades on the user's account. <br>
Mitigation: Use a dedicated simulator-only API key, store it only in the intended OpenClaw configuration, and revoke it when the skill is no longer used. <br>
Risk: The security evidence marks the release suspicious because it provides limited user control and cleanup guidance for autonomous account actions. <br>
Mitigation: Verify the npm package source before installing, review generated commands before execution, and document the removal steps for cron, PM2 startup persistence, local files, and the API key. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/day-trading-simulator/skills/simul8or-trader) <br>
- [Simul8or](https://simul8or.com) <br>
- [Simul8or Setup Guide](https://simul8or.com/OpenClawLanding.php) <br>
- [Simul8or Leaderboard](https://simul8or.com/OpenClawTrading.php) <br>
- [Yahoo Finance Crypto Markets](https://finance.yahoo.com/markets/crypto/all/) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown with bash, JSON, and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May configure a recurring OpenClaw cron run, write local state files in the user's home directory, and call Simul8or API endpoints when enabled.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
