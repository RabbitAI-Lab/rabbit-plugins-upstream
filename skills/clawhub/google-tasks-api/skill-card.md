## Description:

Helps agents read and manage Google Tasks lists and tasks through a connected Maton account, with optional user-approved automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to list, create, update, and delete Google Tasks and task lists, or configure approved scheduled actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creating or changing tasks and task lists can alter or delete the user's data.

Mitigation: Start with read-only calls and obtain explicit approval for every write or new connection.

Risk: Hosted functions, triggers, and destinations can run ongoing actions or send personal data to other services.

Mitigation: Approve each automation separately, limit data shared, and keep destinations on trusted Maton hosts unless the user explicitly approves another host.

Risk: Raw API credentials or local event handlers can expose sensitive data or execute unintended actions.

Mitigation: Prefer the managed CLI, avoid handling raw credentials, and use watch --exec only when explicitly requested with a user-provided handler.

## Reference(s):

- [Google Tasks skill release](https://clawhub.ai/byungkyu/skills/google-tasks-api)
- [Maton](https://maton.ai)
- [Google Tasks API overview](https://developers.google.com/workspace/tasks)
- [Google Tasks API reference](https://developers.google.com/workspace/tasks/reference/rest/v1/tasks)
- [Maton documentation](https://docs.maton.ai)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Google Tasks access requires an authorized connection; writes and new automations require user approval.]

## Skill Version(s):

1.2.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
