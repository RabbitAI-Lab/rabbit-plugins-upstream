## Description: <br>
Controls Xiaomi Home devices over a local LAN with miiocli, including status checks, power toggles, and MIOT property updates for smart plugs, humidifiers, and rice cookers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yiqiezhenxi](https://clawhub.ai/user/yiqiezhenxi) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and home-automation users use this skill to translate natural-language Xiaomi Home requests into local miiocli commands and setup guidance for known devices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change the state of real Xiaomi smart-home devices and appliances. <br>
Mitigation: Install and use it only when agent-controlled local device operation is acceptable, and review generated commands before execution. <br>
Risk: Xiaomi account credentials, device IPs, and reusable device tokens can expose device control if shared or committed. <br>
Mitigation: Treat credentials, IPs, and tokens as secrets; store real values only in private, access-controlled files and never paste them into shared chats. <br>
Risk: The skill references a token_extractor.py script that was not included in the inspected artifact. <br>
Mitigation: Review the extractor script before running it and verify that it handles credentials and tokens appropriately. <br>


## Reference(s): <br>
- [Xiaomi Home Skill on ClawHub](https://clawhub.ai/yiqiezhenxi/skills/xiaomi-home-skill) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires miiocli and user-supplied device IPs and tokens.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
