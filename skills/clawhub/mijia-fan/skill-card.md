## Description: <br>
Controls Xiaomi Mijia fans through a Python CLI for power, speed, swing, status, and device-list actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[renjianboshi](https://clawhub.ai/user/renjianboshi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI-tool users use this skill to invoke a local CLI that controls a configured Xiaomi Mijia fan and reports basic status or device inventory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Xiaomi account-backed access to control a smart-home device. <br>
Mitigation: Install only where Xiaomi account/session access is acceptable and restrict use to the intended fan device ID. <br>
Risk: Device listing can expose household device inventory and device IDs in logs or chat transcripts. <br>
Mitigation: Run listing only during setup and avoid sharing command output that includes device names, models, or DIDs. <br>
Risk: The installer may reuse an existing .mijia_token from another local Mijia skill. <br>
Mitigation: Review and remove copied token files when session reuse is not intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/renjianboshi/skills/mijia-fan) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Plain text CLI output and Markdown command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, the mijiaAPI package, and MIJIA_FAN_DID for fan-specific commands; optional environment variables can override Mijia property identifiers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, SKILL.md frontmatter, and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
