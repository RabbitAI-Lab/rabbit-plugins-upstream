## Description: <br>
Query ecobee thermostat data via Beestat API including temperature, humidity, air quality (CO2, VOC), sensors, and HVAC runtime. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mjrussell](https://clawhub.ai/user/mjrussell) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to inspect Beestat/ecobee thermostat status, sensor readings, indoor air quality, and HVAC runtime through the Beestat CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on the external beestat-cli package and uses a Beestat API key. <br>
Mitigation: Install and run it only when the package source is trusted, and store BEESTAT_API_KEY as a secret rather than sharing it in prompts or logs. <br>
Risk: Thermostat, sensor, air quality, occupancy, and HVAC runtime outputs can reveal private household patterns. <br>
Mitigation: Treat command outputs as private household data and avoid exposing them outside the intended user or automation context. <br>


## Reference(s): <br>
- [Beestat homepage](https://beestat.io) <br>
- [ClawHub Beestat skill page](https://clawhub.ai/mjrussell/skills/beestat) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the beestat CLI and BEESTAT_API_KEY; command output may include private household thermostat, sensor, air quality, occupancy, and HVAC usage data.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
