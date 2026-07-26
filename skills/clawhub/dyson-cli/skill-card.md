## Description: <br>
Control Dyson air purifiers, fans, and heaters over local MQTT for power, fan speed, oscillation, heat, and status tasks on the same WiFi network. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tmustier](https://clawhub.ai/user/tmustier) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users use this skill through an agent to control supported Dyson air purifiers, fans, and heaters from a local machine. It is intended for device setup, status checks, fan and oscillation adjustments, and supervised heat control on the same WiFi network as the device. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dyson account setup and device-control credentials are sensitive when stored locally. <br>
Mitigation: Run setup only on a trusted machine, protect ~/.dyson/config.json with restrictive permissions, and remove the file if you stop using the skill. <br>
Risk: Heater commands can affect a physical device. <br>
Mitigation: Use heat controls only when you can supervise the Dyson device. <br>
Risk: Commands require local network reachability and may fail when the agent is not on the same WiFi network as the device. <br>
Mitigation: Confirm the machine is on the same WiFi network and run dyson list --check before issuing control commands. <br>


## Reference(s): <br>
- [README.md](README.md) <br>
- [libdyson-neon](https://github.com/libdyson-wg/libdyson-neon) <br>
- [ClawHub Skill Page](https://clawhub.ai/tmustier/skills/dyson-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may control local physical devices and require Dyson account setup plus same-network access.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release and pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
