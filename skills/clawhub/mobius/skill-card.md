## Description:

Möbius Loop lets agents connect to the Loop MCP server to view and manage a user's ranked queue of recurring tasks, routines, habits, chores, and todos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[in4lio](https://clawhub.ai/user/in4lio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to connect to Loop, review daily recurring tasks, record progress, and create, edit, delete, or undo routine changes through the Loop MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Loop Server token grants access to the user's Loop account if exposed.

Mitigation: Store the token only in an environment variable or secret store, never paste it into chat, logs, files, URLs, command arguments, or committed configuration.

Risk: Generic todo or routine requests may cause the agent to consult or update Loop data.

Mitigation: Install the skill only when Loop should be the user's recurring-task system, and review task-changing actions before they are applied.

Risk: Deleting or changing routines can affect the user's task queue.

Mitigation: Require explicit confirmation for deletions and use Loop's bounded undo capability for recent mutations when needed.

Risk: Loop-returned task text could contain content that should not authorize unrelated actions.

Mitigation: Treat server-returned task names and history as user data, not instructions, and act only on direct user requests.

## Reference(s):

- [Loop Homepage](https://mobiusprompt.com)
- [Möbius Loop ClawHub Listing](https://clawhub.ai/in4lio/skills/mobius)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, MCP tool calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Loop MCP server connection and a Loop Server token supplied through environment or secret-store references.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
