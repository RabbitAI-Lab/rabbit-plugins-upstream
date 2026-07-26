## Description: <br>
Project Manager helps agents manage internal project tasks with a JSON-based Kanban workflow, chat notifications for review or blocked work, and optional Apple Reminders sync. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fr0ziii](https://clawhub.ai/user/fr0ziii) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to list, create, move, and sync internal project tasks while enforcing workflow rules such as approval before review and limits on work in progress. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Task titles or descriptions may be synced to reminders or sent in chat notifications. <br>
Mitigation: Do not put secrets or sensitive details in tasks that may be synced or messaged. <br>
Risk: The skill edits a specified local project task file and can trigger external workflow side effects. <br>
Mitigation: Install only when this local project file, Apple Reminders sync, and David notification workflow are intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fr0ziii/skills/project-manager) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Natural language responses with JSON task updates and occasional shell commands or workflow calls.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May edit the local projects JSON file, sync tasks to Apple Reminders when requested, and notify David when tasks move to review or blocked.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
