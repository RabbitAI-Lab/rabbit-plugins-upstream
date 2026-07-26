## Description: <br>
Integrates Todoist task management with conversational commands for listing, adding, updating, completing, and organizing tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hail2skins](https://clawhub.ai/user/hail2skins) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
OpenClaw users and developers use this skill to manage Todoist tasks and projects through natural language requests or direct CLI commands. It is suited for personal task workflows where the agent may read, create, update, complete, or delete Todoist items with the user's API token. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change real Todoist account data, including completing, updating, or deleting tasks when the user's API token is available. <br>
Mitigation: Install only when Todoist account access is intended, keep TODOIST_API_KEY private, and require explicit confirmation before destructive or state-changing task actions. <br>
Risk: Date-sensitive filters such as today may produce unexpected results if the runtime timezone is not set correctly. <br>
Mitigation: Set TZ to the user's expected timezone when date filtering matters. <br>


## Reference(s): <br>
- [Todoist API reference](references/api.md) <br>
- [Todoist developer API documentation](https://developer.todoist.com/api/v1/) <br>
- [ClawHub skill page](https://clawhub.ai/hail2skins/skills/todoist-natural-language) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Natural language guidance and JSON output from the Todoist CLI script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TODOIST_API_KEY; TZ is optional for timezone-aware date filtering.] <br>

## Skill Version(s): <br>
1.0.8 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
