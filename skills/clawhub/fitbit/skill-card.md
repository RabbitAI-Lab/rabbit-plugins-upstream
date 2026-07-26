## Description: <br>
Query Fitbit health data including sleep, heart rate, activity, SpO2, and breathing rate. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mjrussell](https://clawhub.ai/user/mjrussell) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users can ask an agent to retrieve read-only Fitbit sleep, heart-rate, activity, SpO2, breathing-rate, profile, and device information through fitbit-cli. The skill is useful for answering personal fitness, sleep quality, step count, device sync, and related health-metric questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Fitbit health, profile, or device data may be exposed in the agent conversation. <br>
Mitigation: Ask only for metrics you are comfortable displaying and keep requested date ranges narrow. <br>
Risk: The skill depends on an external fitbit-cli binary to access Fitbit data. <br>
Mitigation: Use a trusted fitbit-cli installation and complete authentication intentionally with fitbit-cli --init-auth. <br>
Risk: Fitbit data may lag behind current activity if the wearable has not synced recently. <br>
Mitigation: Check device sync status before relying on recent metrics. <br>


## Reference(s): <br>
- [Fitbit homepage](https://www.fitbit.com) <br>
- [ClawHub skill page](https://clawhub.ai/mjrussell/skills/fitbit) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and plain-language summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses fitbit-cli for read-only retrieval; first-time setup requires fitbit-cli --init-auth.] <br>

## Skill Version(s): <br>
0.1.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
