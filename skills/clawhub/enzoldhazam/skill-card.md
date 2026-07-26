## Description: <br>
Control NGBS iCON Smart Home thermostats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daniel-laszlo](https://clawhub.ai/user/daniel-laszlo) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users use this skill to check room temperatures, inspect thermostat status, and control target temperatures for registered NGBS iCON Smart Home devices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill controls physical thermostat settings and can change a room's target temperature. <br>
Mitigation: Confirm the room and requested temperature with the user before running set commands. <br>
Risk: The skill requires account credentials for enzoldhazam.hu. <br>
Mitigation: Prefer macOS Keychain login, avoid shell history or CI logs for credentials, and use environment variables only when necessary. <br>
Risk: Installation examples include moving a binary into a system path. <br>
Mitigation: Use a user-local install path instead of sudo when practical and install only when the publisher is trusted. <br>


## Reference(s): <br>
- [enzoldhazam.hu](https://www.enzoldhazam.hu) <br>
- [ClawHub skill page](https://clawhub.ai/daniel-laszlo/skills/enzoldhazam) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute thermostat status, get, set, login, and logout commands through the enzoldhazam CLI when available.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
