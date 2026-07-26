## Description: <br>
Query workout data from Hevy including workouts, routines, exercises, and history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[baderfahoum17](https://clawhub.ai/user/baderfahoum17) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use Hevy to query workout history, routines, exercise templates, and fitness progress from a Hevy account. With explicit approval, the skill can also create or update routines, folders, custom exercises, and workout records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make persistent changes to a Hevy account while its summary is mainly query-focused. <br>
Mitigation: Treat it as read/write and require explicit user confirmation before any create or update command is run. <br>
Risk: The HEVY_API_KEY grants access to workout data and account operations exposed by the Hevy API. <br>
Mitigation: Provide the API key only in a controlled environment and install only when that account access is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/baderfahoum17/skills/hevy) <br>
- [Hevy homepage](https://hevy.com) <br>
- [Hevy API documentation](https://api.hevyapp.com/docs/) <br>
- [Hevy developer settings](https://hevy.com/settings?developer) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, api calls] <br>
**Output Format:** [CLI text output, JSON responses when requested, and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires HEVY_API_KEY; some commands can make persistent changes to the connected Hevy account.] <br>

## Skill Version(s): <br>
0.2.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
