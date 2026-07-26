## Description: <br>
Interact with ClickUp project management platform via REST API. Use when working with tasks, spaces, lists, assignees, or any ClickUp workflow automation. Handles pagination, subtasks, and common query patterns. Use for task management, reporting, automation, or any ClickUp-related queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shubhs0707](https://clawhub.ai/user/shubhs0707) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to query, report on, and automate ClickUp tasks, spaces, lists, assignees, and workflow status through the ClickUp REST API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, assign, change status, or delete live ClickUp tasks. <br>
Mitigation: Require explicit user confirmation before any write operation and test changes in a non-production workspace when possible. <br>
Risk: The skill requires a ClickUp API token that may expose workspace data and write permissions. <br>
Mitigation: Use the least-privileged ClickUp API token available and limit the token to the workspace or lists needed for the task. <br>
Risk: Task queries can miss work items if subtasks or paginated results are omitted. <br>
Mitigation: Use subtasks=true and follow pagination until last_page is true for task inventory, audit, and reporting workflows. <br>


## Reference(s): <br>
- [ClickUp API Reference](artifact/references/api-guide.md) <br>
- [ClickUp Skill on ClawHub](https://clawhub.ai/shubhs0707/skills/clickup) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, curl examples, jq filters, and JSON responses from ClickUp API calls.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require CLICKUP_API_KEY and CLICKUP_TEAM_ID environment variables and can operate on live ClickUp workspace data.] <br>

## Skill Version(s): <br>
1.2.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
