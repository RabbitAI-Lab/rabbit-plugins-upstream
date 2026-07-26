## Description: <br>
Control IKEA/TP-Link Kasa smart bulbs on a local network by IP address, including power, brightness, color, and light-show actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[antgly](https://clawhub.ai/user/antgly) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation users can use this skill to have an agent generate or run commands that control a Kasa-compatible smart bulb on the same LAN. It is useful for local smart-home control when the bulb IP address is known and cloud credentials are not required. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send commands to a user-specified smart bulb on the local network. <br>
Mitigation: Verify the bulb IP address before running commands and use it only on trusted local networks. <br>
Risk: Light-show modes can rapidly change brightness or color. <br>
Mitigation: Use caution with flashing or light-show modes, especially around people sensitive to flashing lights. <br>
Risk: The skill depends on uv and python-kasa from the Python package ecosystem. <br>
Mitigation: Install dependencies from trusted package sources and keep the local Python environment under user control. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/antgly/skills/control-ikea-lightbulb) <br>
- [Publisher profile](https://clawhub.ai/user/antgly) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and Python script invocation examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires uv, Python 3.11+, python-kasa, and a reachable local bulb IP address.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
