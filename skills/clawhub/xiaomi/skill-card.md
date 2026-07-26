## Description: <br>
Control Xiaomi Home devices over the local network using miiocli for status checks, power toggles, and MIOT property changes on smart plugs, humidifiers, rice cookers, and similar devices. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yiqiezhenxi](https://clawhub.ai/user/yiqiezhenxi) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and smart-home developers use this skill to translate natural-language Xiaomi device requests into miiocli commands for local LAN control and device status checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Xiaomi device-control tokens that can grant local access to smart-home devices. <br>
Mitigation: Treat tokens like passwords: do not commit, paste, or store them in shared markdown files, and keep device registries private. <br>
Risk: Generated commands can change physical device states, including power, heating, cooking, or humidifier settings. <br>
Mitigation: Require explicit user confirmation before executing commands that turn devices on or alter physical appliance behavior. <br>
Risk: The token extraction workflow may access Xiaomi Cloud account data. <br>
Mitigation: Review any token-extraction script before running it and only execute it in an environment trusted for account credentials. <br>


## Reference(s): <br>
- [ClawHub Xiaomi skill page](https://clawhub.ai/yiqiezhenxi/skills/xiaomi) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and device configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may include device IP addresses, Xiaomi tokens, and MIOT property identifiers supplied by the user.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
