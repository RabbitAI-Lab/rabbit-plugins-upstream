## Description: <br>
Project Delivery Engine helps agents keep long-running projects continuous by preserving status, handoffs, TODOs, evidence, material indexes, collaboration boundaries, and review workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haoyun18881-beep](https://clawhub.ai/user/haoyun18881-beep) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, project teams, and agent operators use this skill to initialize, resume, checkpoint, hand off, review, and coordinate projects that span multiple sessions or agents. It is intended for tasks that depend on current project state, not ordinary one-off requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill persistently manages project handoff, status, TODO, evidence, and material-index files in a repository. <br>
Mitigation: Install it only for projects where persistent project-governance files are desired, and review proposed project-state changes during initialization and checkpoints. <br>
Risk: Controlled apply operations may create or update governance files and temporary .project-gov plans, locks, or backups. <br>
Mitigation: Use the documented propose-then-apply workflow and inspect proposed paths, actions, and summaries before applying changes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/haoyun18881-beep/skills/project-delivery-engine) <br>
- [Project State and Handoff Reference](artifact/references/project-state.md) <br>
- [Project Governance CLI Reference](artifact/references/project-gov-cli.md) <br>
- [Collaboration and Review Reference](artifact/references/collaboration.md) <br>
- [Quickstart and FAQ](artifact/references/quickstart-faq.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, structured project files, JSON CLI reports and plans, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces persistent project-governance files and project-local temporary plans, locks, and backups during controlled apply operations.] <br>

## Skill Version(s): <br>
0.3.5 (source: server release evidence and project-gov script constant) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
