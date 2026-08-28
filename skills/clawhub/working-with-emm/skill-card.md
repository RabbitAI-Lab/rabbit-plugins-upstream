## Description:

Working with Emm AI helps agents use the Emm AI MCP connector to recall user preferences, save durable context, manage outputs and instructions, and run recurring task cycles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gregertw](https://clawhub.ai/user/gregertw)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to give MCP-capable agents durable personal memory, standing instructions, an output wiki, and controlled recurring work through Emm AI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has broad implicit triggers for personalization and recurring agent work involving sensitive personal data.

Mitigation: Review MCP permissions, sharing defaults, and instruction-write settings before deployment; use the documented shared-memory consent rule before searching remote memories.

Risk: The optional manual OAuth fallback can store OAuth tokens in a local mcporter credentials file.

Mitigation: Prefer platform-managed OAuth where available, and treat ~/.mcporter/credentials.json as sensitive if the manual fallback is used.

Risk: Connected actions and recurring cycles can affect external services, devices, messages, or wiki outputs.

Mitigation: Keep external actions user-authorized, draft messages before sending, and re-read editable outputs before updates to avoid stale writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gregertw/skills/working-with-emm)
- [Setup Guide](references/setup.md)
- [Memory Best Practices](references/memory-best-practices.md)
- [Emm AI Mission Control Reference Card](references/mission-control.md)
- [Tool Surface](references/tool-surface.md)
- [Shared Memories from Connections](references/shared-memories.md)
- [Remote Action Execution](references/remote-actions.md)
- [Task Builder](references/task-builder.md)
- [Custom Memory Categories](references/custom-categories.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and YAML configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Emm AI MCP connector and live MCP tool schemas.]

## Skill Version(s):

2.5.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
