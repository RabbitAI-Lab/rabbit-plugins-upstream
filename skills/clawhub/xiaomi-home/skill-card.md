## Description: <br>
Controls Xiaomi Home devices on the local network through miiocli, including status checks, power toggles, and MIOT property changes for smart plugs, humidifiers, rice cookers, and similar devices. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pegasus02](https://clawhub.ai/user/pegasus02) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and advanced smart-home users use this skill to translate natural-language requests into miiocli commands for discovering and controlling Xiaomi devices on a trusted local network. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package ships a private-looking Xiaomi device inventory and handles device-control secrets loosely. <br>
Mitigation: Remove private inventory files before use or publication, keep device tokens out of shared repositories, and rotate exposed device tokens where possible. <br>
Risk: Xiaomi account credentials and device tokens may be exposed through command-line arguments or debug logs. <br>
Mitigation: Prefer interactive credential entry or protected local secret storage, keep debug logging off, and avoid passing passwords directly on the command line. <br>
Risk: Commands can control physical devices such as heaters, cookers, cameras, routers, and plugs. <br>
Mitigation: Require explicit user confirmation before executing commands that affect physical devices, safety-sensitive appliances, cameras, or network equipment. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/pegasus02/skills/xiaomi-home) <br>
- [Device inventory template](references/devices.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and MIOT parameter examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include device IP, token, model, and MIOT siid/piid/value placeholders; users must supply local credentials and review commands before execution.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
