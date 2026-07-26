## Description: <br>
Monitors live status of a Pod Point charger's connectors A and B, reporting current availability and changes without requiring authentication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zoranjurcevic](https://clawhub.ai/user/zoranjurcevic) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Drivers and operators use this skill to check live connector availability for a known Pod Point pod ID, or to watch until a connector becomes available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pod IDs are sent to Pod Point's public status endpoint. <br>
Mitigation: Use only pod IDs you are comfortable sharing with Pod Point. <br>
Risk: Watch mode repeatedly contacts the public endpoint until an availability event occurs or the timeout is reached. <br>
Mitigation: Use reasonable intervalSeconds and timeoutSeconds values when watching a charger. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zoranjurcevic/skills/podpoint) <br>
- [Publisher profile](https://clawhub.ai/user/zoranjurcevic) <br>


## Skill Output: <br>
**Output Type(s):** [text, json] <br>
**Output Format:** [JSON object or concise status response] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports connector A and B status, availability booleans, timeout state, and availability-change events when watching.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
