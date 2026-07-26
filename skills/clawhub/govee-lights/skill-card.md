## Description: <br>
Control Govee smart lights to turn on or off, adjust brightness, set colors, and manage device states via the Govee API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[joeynyc](https://clawhub.ai/user/joeynyc) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Smart-home users and developers use this skill to list and control Govee lights by name from an agent workflow, including power, brightness, and RGB color changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Govee API key that can control devices on the connected account. <br>
Mitigation: Keep the API key private and revocable, and install only where agent access to Govee device control is intended. <br>
Risk: Partial name matching can select an unintended device when names overlap. <br>
Mitigation: List devices first and use exact or distinctive device names before sending control commands. <br>
Risk: The script depends on a third-party Python package. <br>
Mitigation: Install requests in a virtual environment or other managed Python environment. <br>


## Reference(s): <br>
- [Govee Developer Portal](https://developer.govee.com/) <br>
- [Troubleshooting](references/TROUBLESHOOTING.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/joeynyc/skills/govee-lights) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and command output text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided GOVEE_API_KEY and the Python requests dependency.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
