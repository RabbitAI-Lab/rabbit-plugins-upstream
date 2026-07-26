## Description: <br>
Control Sensibo smart AC devices through the Sensibo REST API for power, temperature, mode, sensor checks, and climate schedule management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[omere2](https://clawhub.ai/user/omere2) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers can use this skill to let an agent control Sensibo-connected AC units, query room temperature and humidity, and manage schedules, timers, and Climate React automations through the Sensibo REST API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Sensibo API key that can control connected AC devices. <br>
Mitigation: Store the API key like a password, avoid sharing files that contain it, and rotate the key if it is exposed. <br>
Risk: Schedule, timer, and Climate React automation changes can affect device behavior after the current interaction. <br>
Mitigation: Review any schedule, timer, or automation change explicitly before allowing the agent to apply it. <br>
Risk: Incorrect room, device, mode, or temperature choices can change comfort, energy use, or AC operation. <br>
Mitigation: Confirm the target room, device ID, mode, and temperature before sending control commands. <br>


## Reference(s): <br>
- [ClawHub Sensibo skill page](https://clawhub.ai/omere2/skills/sensibo) <br>
- [Sensibo API key page](https://home.sensibo.com/me/api) <br>
- [Sensibo API v2 base URL](https://home.sensibo.com/api/v2) <br>
- [Sensibo API v1 schedules base URL](https://home.sensibo.com/api/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses user-supplied Sensibo API keys and device IDs; responses should be checked for successful API status.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
