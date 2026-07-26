## Description: <br>
Control your Tesla via MyTeslaMate API. Supports multi-vehicle accounts, climate control, and charging schedules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ovaris](https://clawhub.ai/user/ovaris) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and Tesla owners with authorized MyTeslaMate access use this skill to inspect vehicle state and run vehicle-control commands such as wake, climate, charging limit, and charging schedule changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands can change the state of a real vehicle, including climate, charging, schedule, and wake actions. <br>
Mitigation: Use only with a vehicle you own or are authorized to control, and confirm each state-changing action before execution. <br>
Risk: The skill depends on sensitive TESLA_MATE_TOKEN and TESLA_VIN values in the agent environment. <br>
Mitigation: Store the token and VIN only in the intended runtime environment, avoid sharing them in prompts or logs, and rotate the token if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ovaris/skills/tesla-commands) <br>
- [MyTeslaMate fleet page](https://app.myteslamate.com/fleet) <br>
- [MyTeslaMate vehicles API](https://api.myteslamate.com/api/1/vehicles) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON responses from the Tesla control script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided TESLA_MATE_TOKEN and a vehicle VIN from the environment or command line.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
