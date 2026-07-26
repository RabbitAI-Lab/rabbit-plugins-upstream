## Description: <br>
Controls IKEA/TP-Link Kasa smart bulbs by setting power, brightness, and color. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and smart-home users can use this skill to have an agent control IKEA or TP-Link Kasa light bulbs, including on/off state, brightness, and color. Use it only when shell execution for local device control is acceptable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests shell execution for smart-bulb control without clearly limiting allowed commands. <br>
Mitigation: Review and approve exact commands before execution, and run only in an environment where shell access and local device control are acceptable. <br>
Risk: The skill can change local smart-bulb state on the user's network. <br>
Mitigation: Use it only with intended devices and verify device identifiers, IP addresses, brightness, and color settings before executing control commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/control-ikea-lightbulb) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON-like status or confirmation output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use local command-line tools to control smart bulbs; commands should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
