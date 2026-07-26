## Description: <br>
Controls Xiaomi Home devices over the local LAN with miiocli for status checks, power toggles, and MIOT property changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yiqiezhenxi](https://clawhub.ai/user/yiqiezhenxi) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and home automation users use this skill to translate Xiaomi Home requests into local miiocli commands for device status checks, power control, and MIOT property updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Xiaomi device tokens that grant local control of devices. <br>
Mitigation: Treat device tokens like passwords, keep them out of shared markdown and version control, and inspect any token extractor before running it. <br>
Risk: Generated commands can change real appliance power or operating state on the local network. <br>
Mitigation: Require explicit confirmation before power or appliance-state changes and scope commands to the intended device. <br>
Risk: The security verdict requires review because device-control scope and safety guidance are limited. <br>
Mitigation: Review the skill and command targets before deployment, and restrict use to trusted agents and users on the local network. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yiqiezhenxi/skills/home-xiaomi) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires miiocli and Xiaomi device IP/token values; may include commands that change device state.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
