## Description: <br>
Query Yahoo Fantasy Baseball league data, including rosters, standings, matchups, free agents, draft results, transactions, injuries, and read-only daily roster optimization suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[khaney64](https://clawhub.ai/user/khaney64) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External fantasy baseball managers use this skill to inspect Yahoo league, team, player, matchup, transaction, injury, and draft data and receive read-only lineup optimization guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Yahoo OAuth credentials and tokens are stored on disk under ~/.openclaw/credentials/yahoo-fantasy/. <br>
Mitigation: Use the skill only in trusted environments, treat that directory as sensitive, and remove stale legacy .env credentials after migration. <br>
Risk: Commands can read league-wide data visible to the authenticated Yahoo account. <br>
Mitigation: Grant Yahoo API access only from accounts whose fantasy league data may be viewed by the agent. <br>
Risk: The --setup command installs Python dependencies before normal use. <br>
Mitigation: Run --setup only after reviewing the included requirements and accepting the dependency install. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/khaney64/skills/yahoo-fantasy-baseball) <br>
- [yahoo-fantasy-api](https://github.com/spilchen/yahoo_fantasy_api) <br>
- [Yahoo Developer Apps](https://developer.yahoo.com/apps/) <br>
- [MLB Stats API](https://statsapi.mlb.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance, Shell commands] <br>
**Output Format:** [CLI text output, JSON, or Discord-formatted code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only results and recommendations; requires Yahoo OAuth access, local token storage, network access, and explicit dependency installation via --setup.] <br>

## Skill Version(s): <br>
0.1.29 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
