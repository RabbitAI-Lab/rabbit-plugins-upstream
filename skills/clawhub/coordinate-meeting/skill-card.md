## Description: <br>
Schedules a group meeting by creating a MeetLark poll, sharing it with participants, checking votes, and recommending the best time. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mkelk](https://clawhub.ai/user/mkelk) <br>

### License/Terms of Use: <br>


## Use Case: <br>
People and their agents use this skill to coordinate a meeting by proposing time slots, collecting participant votes through MeetLark, and closing the poll after a time is chosen. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Meeting purpose, proposed times, verification email information, and participant-related details are shared with MeetLark. <br>
Mitigation: Use the skill only when the user is comfortable using meetlark.ai for scheduling and avoid adding unnecessary sensitive details. <br>
Risk: The admin token can be used to check results and close the poll. <br>
Mitigation: Keep the admin token private and share only the participation link with intended voters. <br>


## Reference(s): <br>
- [Coordinate a Meeting on ClawHub](https://clawhub.ai/mkelk/skills/coordinate-meeting) <br>
- [MeetLark](https://meetlark.ai) <br>
- [MeetLark OpenAPI spec](https://meetlark.ai/api/v1/openapi.json) <br>
- [MeetLark interactive docs](https://meetlark.ai/docs) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with poll links, participant messages, status summaries, and recommended meeting times] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May involve MeetLark API calls; the admin token should remain private and the participation link should be shared only with intended voters.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
