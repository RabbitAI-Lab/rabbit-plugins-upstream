## Description: <br>
FireHydrant (firehydrant.com). Use this skill for ANY FireHydrant request: reading, creating, and updating data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and incident responders use this skill to let an agent inspect FireHydrant incidents, services, and environments and create incidents through an OOMOL-connected FireHydrant account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create FireHydrant incidents through the connected account. <br>
Mitigation: Confirm the exact write payload and expected effect with the user before running incident creation. <br>
Risk: Using the skill grants the agent access to FireHydrant data available through the connected OOMOL account. <br>
Mitigation: Install and use the skill only when that account access is intended for the task. <br>
Risk: First-time setup may require running a remote oo CLI installer. <br>
Mitigation: Run the installer only after verifying that the OOMOL install source is trusted. <br>


## Reference(s): <br>
- [ClawHub FireHydrant Skill](https://clawhub.ai/oomol/skills/oo-firehydrant) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [FireHydrant Homepage](https://firehydrant.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent actions may return JSON data from FireHydrant connector calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
