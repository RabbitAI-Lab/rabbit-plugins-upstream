## Description: <br>
Manage Operately from the CLI for goals, OKRs, projects, tasks, milestones, spaces, Docs & Files, discussions, check-ins, reviews, assignments, people, permissions, and workspace operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[markoa](https://clawhub.ai/user/markoa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, operators, and developers use this skill to operate an Operately workspace through the official CLI, including project, goal, task, space, documentation, collaboration, assignment, and company administration workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent through authenticated operations in an Operately workspace, including administrative and destructive actions. <br>
Mitigation: Use secure token injection, confirm the active profile and base URL before changes, and require explicit user approval before deleting resources or changing permissions. <br>
Risk: Password flags and interactive login flows can expose credentials or block headless automation. <br>
Mitigation: Prefer API-token login with OPERATELY_API_TOKEN or a saved profile, and use interactive auth only when a human can complete prompts, email-code entry, or browser confirmation. <br>


## Reference(s): <br>
- [Operately CLI ClawHub Release](https://clawhub.ai/markoa/skills/operately-cli) <br>
- [Operately Skills Repository](https://github.com/operately/skills) <br>
- [Assignments and Reviews](references/assignments-and-reviews.md) <br>
- [Auth Flows](references/auth-flows.md) <br>
- [Collaboration Patterns](references/collaboration-patterns.md) <br>
- [Docs & Files](references/docs-and-files.md) <br>
- [Goal Workflows](references/goal-workflows.md) <br>
- [Project Workflows](references/project-workflows.md) <br>
- [Space Workflows](references/space-workflows.md) <br>
- [Task Workflows](references/task-workflows.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference Operately CLI JSON responses and local file paths for uploads or markdown content.] <br>

## Skill Version(s): <br>
1.4.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
