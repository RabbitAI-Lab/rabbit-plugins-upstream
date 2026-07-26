## Description: <br>
Control a Homey home automation hub from an agent through CLI commands for device status, device control, zones, flows, and inventory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[krausefx](https://clawhub.ai/user/krausefx) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and smart-home operators use this skill to let an agent inspect Homey devices, read device state, adjust allowlisted capabilities, and trigger Homey flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package asks agents to run a CLI implementation that was not included in the submitted artifact. <br>
Mitigation: Inspect or obtain the missing CLI implementation before running npm install or bash run.sh. <br>
Risk: The skill uses persistent Homey credentials and can trigger flows or change device states. <br>
Mitigation: Protect .env and ~/.config/homey-cli credential files, and require explicit approval before triggering flows or changing device states. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/krausefx/skills/homey-cli) <br>
- [Homey developer app tools](https://tools.developer.homey.app/tools/app) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may read or change real smart-home state and require Homey OAuth credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
