## Description: <br>
Query workout data from Hevy including workouts, routines, exercises, and history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mjrussell](https://clawhub.ai/user/mjrussell) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to answer user questions about Hevy workouts, routines, exercise templates, and exercise history, and to prepare or run supported Hevy CLI commands. It can also create or update Hevy account data when write commands are used. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses HEVY_API_KEY to give an agent authenticated access to a Hevy account. <br>
Mitigation: Install it only when that account access is intended, and keep the API key scoped and stored as an environment variable. <br>
Risk: The skill exposes commands that can create or update Hevy account data. <br>
Mitigation: Treat it as a read/write account-management tool and review create or update commands before they run. <br>
Risk: Custom exercise creation can create duplicate records when forced. <br>
Mitigation: Use the default duplicate check and avoid the --force option unless duplicate creation is intentional. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mjrussell/skills/hevy) <br>
- [Hevy API Documentation](https://api.hevyapp.com/docs/) <br>
- [Hevy Developer Settings](https://hevy.com/settings?developer) <br>
- [Hevy](https://hevy.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON output from the Hevy CLI] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the hevy CLI and HEVY_API_KEY for authenticated Hevy API access.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
