## Description: <br>
Control smart home devices via Homebridge Config UI X REST API. Use to list, turn on/off, adjust brightness, color, or temperature of HomeKit-compatible accessories. Supports lights, switches, thermostats, fans, and other Homebridge-managed devices. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiasenl](https://clawhub.ai/user/jiasenl) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and smart-home operators use this skill to inspect and control Homebridge-managed accessories through Config UI X. It can list devices and rooms, read accessory status, and update characteristics such as power, brightness, color, fan speed, and thermostat targets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control real smart-home devices, including thermostats and powered accessories. <br>
Mitigation: Install only when agent control of Homebridge accessories is intended, and require extra confirmation for actions that affect safety, comfort, or energy use. <br>
Risk: The helper script reads Homebridge URL, username, and password from a local credential file. <br>
Mitigation: Store the credential file carefully, restrict local access, and verify the configured URL points to the user's own Homebridge instance before use. <br>


## Reference(s): <br>
- [Homebridge Config UI X](https://github.com/homebridge/homebridge-config-ui-x) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration examples, bash commands, and Python helper commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Homebridge API requests and JSON accessory data through the bundled helper script.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
