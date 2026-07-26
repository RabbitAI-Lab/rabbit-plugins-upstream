## Description: <br>
FIFA World Cup match predictor: dual-mode score model + Elo ratings. Win/draw/loss probabilities & score predictions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ravenquasar](https://clawhub.ai/user/ravenquasar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to inspect FIFA World Cup schedules, group standings, win/draw/loss probabilities, and predicted scores from a local command-line predictor. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional BALLDONTLIE API key is a sensitive credential. <br>
Mitigation: Store only the skill-specific API key in the documented OpenClaw configuration and rotate or remove it if it is no longer needed. <br>
Risk: The local schedule cache may become stale and affect prediction quality. <br>
Mitigation: Refresh or review the schedule cache before relying on predictions for current matches. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ravenquasar/worldcup-predictor) <br>
- [NetEase Sports World Cup schedule source](https://sports.163.com/caipiao/worldcup2026) <br>
- [BALLDONTLIE FIFA World Cup API](https://fifa.balldontlie.io) <br>
- [BALLDONTLIE FIFA World Cup API base URL](https://api.balldontlie.io/fifa/worldcup/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Terminal text with command examples and optional JSON configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include match predictions, schedules, standings, team lists, and local schedule-cache updates.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
