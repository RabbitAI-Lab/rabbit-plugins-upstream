## Description: <br>
This skill lets an agent read, list, and merge Ortto people records through the OOMOL oo connector after checking each action schema. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and operators use this skill to retrieve Ortto contacts, list customer data, and create or update people through an OOMOL-connected Ortto account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Read operations may expose Ortto customer or contact data. <br>
Mitigation: Install and use the skill only for authorized Ortto work, and request only the fields and records needed for the task. <br>
Risk: The merge_people action can create or update Ortto contacts. <br>
Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running write actions. <br>
Risk: First-time CLI installation and account connection steps affect the local environment and account access. <br>
Mitigation: Run setup steps only after a matching command failure, and use the documented OOMOL CLI and connection URLs. <br>


## Reference(s): <br>
- [ClawHub Ortto skill page](https://clawhub.ai/oomol/skills/oo-ortto) <br>
- [Ortto homepage](https://ortto.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL app connections](https://console.oomol.com/app-connections?provider=ortto) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call Ortto read and write actions through oo connector; write actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
