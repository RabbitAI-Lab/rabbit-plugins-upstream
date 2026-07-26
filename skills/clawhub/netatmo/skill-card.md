## Description: <br>
Control Netatmo thermostat and weather station data for heating changes, thermostat modes, temperature history, and indoor/outdoor sensor readings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[florianbeer](https://clawhub.ai/user/florianbeer) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to ask an agent for Netatmo CLI guidance that checks thermostat status, weather station readings, temperature history, and heating mode or setpoint changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can propose thermostat temperature or mode changes that affect a physical heating system. <br>
Mitigation: Require explicit user confirmation before running setpoint or mode-change commands. <br>
Risk: Netatmo credentials and OAuth tokens are stored in local configuration files. <br>
Mitigation: Protect `~/.config/netatmo/credentials.json` and `~/.config/netatmo/tokens.json` with appropriate local file permissions and avoid exposing their contents in agent output. <br>
Risk: Sensor readings can reveal private home or office conditions such as occupancy-related CO2, noise, humidity, and temperature patterns. <br>
Mitigation: Share sensor output only with trusted users and avoid publishing raw readings unless disclosure is intended. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and optional JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Thermostat setpoint and mode changes should be confirmed before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
