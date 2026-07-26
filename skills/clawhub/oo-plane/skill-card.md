## Description: <br>
Plane (plane.so). Use this skill for ANY Plane request - reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams use this skill to let an agent inspect and manage Plane projects, members, labels, states, and work items through an OOMOL-connected Plane account. It supports read operations, work item creation and updates, and explicitly approved deletion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, or delete Plane work items. <br>
Mitigation: Confirm the exact payload and expected effect with the user before write actions, and require explicit approval before delete_work_item. <br>
Risk: One-time CLI installation or account connection steps affect the user's local environment and OOMOL-connected Plane access. <br>
Mitigation: Run setup only after an authentication or connection failure, and perform installation or connection steps from a trusted environment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-plane) <br>
- [Plane Homepage](https://plane.so) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May trigger Plane read, write, or delete actions through the oo CLI when the user has configured OOMOL credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
