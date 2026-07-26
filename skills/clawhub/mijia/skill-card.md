## Description: <br>
Control Xiaomi Mijia smart home devices, including lamp power, brightness, color temperature, and lighting modes, through natural language mappings and command-line actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hqman](https://clawhub.ai/user/hqman) <br>

### License/Terms of Use: <br>
MIT License <br>


## Use Case: <br>
Developers and agent users use this skill to control configured Xiaomi Mijia smart home devices from an AI coding assistant. It is intended for device status checks and direct lamp actions such as power, brightness, color temperature, and mode changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [Mijia skill page](https://clawhub.ai/hqman/skills/mijia) <br>
- [mijia-api library](https://github.com/Do1e/mijia-api) <br>
- [uv package manager](https://github.com/astral-sh/uv) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and concise status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MIJIA_LAMP_DID to target the intended device and Xiaomi QR login before controlling devices; ClawHub security guidance recommends confirmation before power, brightness, mode, or smart-plug actions.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence and pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
