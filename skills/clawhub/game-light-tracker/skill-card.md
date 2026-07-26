## Description: <br>
Tracks live NFL, NBA, NHL, or MLB games and helps an agent sync Hue light colors through Home Assistant based on which team is leading. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xadamsu](https://clawhub.ai/user/0xadamsu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to set up sports-game score monitoring that changes Hue lights through Home Assistant when the leading team changes. It is intended for personal smart-home game tracking across NFL, NBA, NHL, and MLB games. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release depends on PowerShell scripts that were not included in the artifact. <br>
Mitigation: Review or provide the actual game-tracker.ps1 and keeper.ps1 scripts before running the skill. <br>
Risk: The workflow uses a Home Assistant API token and controls a configured light entity. <br>
Mitigation: Use the least-privilege token available and confirm the exact Home Assistant light entity before starting tracking. <br>
Risk: The keeper workflow may launch hidden background PowerShell processes and the stop command can broadly force-stop matching PowerShell processes. <br>
Mitigation: Avoid hidden background launch unless explicitly desired and stop only the specific tracker process IDs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/0xadamsu/skills/game-light-tracker) <br>
- [ESPN NFL teams](https://www.espn.com/nfl/teams) <br>
- [ESPN NBA teams](https://www.espn.com/nba/teams) <br>
- [ESPN NHL teams](https://www.espn.com/nhl/teams) <br>
- [ESPN MLB teams](https://www.espn.com/mlb/teams) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with PowerShell command blocks and setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference Home Assistant configuration, light entity IDs, team abbreviations, RGB colors, and local PowerShell scripts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
