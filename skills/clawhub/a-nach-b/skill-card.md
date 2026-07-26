## Description: <br>
Austrian public transport (VOR AnachB) for all of Austria, supporting real-time departures, station and stop search, route planning, and service disruption checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manmal](https://clawhub.ai/user/manmal) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to answer Austrian public transport questions, including finding stops, checking real-time departures, planning routes, and reviewing current service disruptions. <br>

### Deployment Geography for Use: <br>
Austria, with limited cross-border route coverage where the underlying service provides it. <br>

## Known Risks and Mitigations: <br>
Risk: Script arguments are interpolated into JSON request bodies before calling the transit API. <br>
Mitigation: Use ordinary station names, station IDs, and small numeric counts; update the scripts to construct JSON with a proper encoder such as jq. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/manmal/skills/a-nach-b) <br>
- [VOR AnachB HAFAS endpoint](https://vao.demo.hafas.de/gate) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Shell command invocations and JSON transit results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access to the VOR AnachB HAFAS endpoint and jq for response parsing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
