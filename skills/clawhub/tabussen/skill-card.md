## Description: <br>
Tabussen helps agents plan public transport trips in Västerbotten and Umeå using the ResRobot API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[simskii](https://clawhub.ai/user/simskii) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents can look up stops, resolve locations, and plan bus, train, and walking journeys in Västerbotten and Umeå, including depart-now, future departure, and arrive-by queries. <br>

### Deployment Geography for Use: <br>
Sweden, focused on Västerbotten and Umeå <br>

## Known Risks and Mitigations: <br>
Risk: Transit searches and location queries are sent to the ResRobot public transport API. <br>
Mitigation: Use the skill only when sending those searches to ResRobot is acceptable for the user and task. <br>
Risk: The helper scripts require a ResRobot/Trafiklab API key. <br>
Mitigation: Use a dedicated API key, provide it through RESROBOT_API_KEY, and keep it out of shared logs. <br>
Risk: The skill depends on local command-line tools and network access. <br>
Mitigation: Confirm curl and jq are installed and that outbound access to ResRobot is available before relying on the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/simskii/skills/tabussen) <br>
- [Trafiklab developer portal](https://developer.trafiklab.se) <br>
- [ResRobot API endpoint](https://api.resrobot.se/v2.1/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell command invocations and plain-text journey results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires RESROBOT_API_KEY, curl, jq, and network access to ResRobot.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
