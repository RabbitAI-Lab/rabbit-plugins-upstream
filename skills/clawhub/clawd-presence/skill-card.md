## Description: <br>
Physical presence display for AI agents that shows a customizable A-Z monogram, status state, and current activity on a dedicated terminal or screen. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[voidcooks](https://clawhub.ai/user/voidcooks) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to give an AI agent an always-on local terminal presence that shows its current status and activity. It is useful when a human needs quick visual feedback without waiting for chat updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled Python scripts create and update local config.json and state.json files in the skill directory. <br>
Mitigation: Install and run the skill only in a workspace where local file updates by these scripts are acceptable. <br>
Risk: The --auto configuration mode inspects local Clawd or Clawdbot configuration files to detect an agent name. <br>
Mitigation: Use manual configuration with --letter and --name when you do not want the skill to inspect those local configuration files. <br>
Risk: Presence messages are displayed on a terminal or screen and stored locally in state.json. <br>
Mitigation: Keep status messages non-sensitive and avoid including secrets, private user data, or confidential task details. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local terminal display behavior and updates local config.json and state.json files through bundled Python scripts.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
