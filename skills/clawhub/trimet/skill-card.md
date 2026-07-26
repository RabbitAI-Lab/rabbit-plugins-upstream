## Description: <br>
Get Portland transit information including arrivals, trip planning, and alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mjrussell](https://clawhub.ai/user/mjrussell) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to answer Portland transit questions, including real-time arrivals, trip planning, next departures, and service alerts for TriMet buses and MAX lines. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires the trimet-cli package and a TRIMET_APP_ID credential. <br>
Mitigation: Confirm trimet-cli is the intended package before installing it and keep TRIMET_APP_ID private. <br>
Risk: Trip-planning requests may include exact addresses or other sensitive locations. <br>
Mitigation: Avoid using exact sensitive addresses unless they are necessary for the requested transit plan. <br>


## Reference(s): <br>
- [TriMet](https://trimet.org) <br>
- [TriMet Developer Resources](https://developer.trimet.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include TriMet CLI commands and JSON-output options for arrivals, trips, next departures, and alerts.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
