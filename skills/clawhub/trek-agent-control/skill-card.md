## Description:

Trek Agent Control lets compatible agents use authenticated MCP or the Trek CLI to research trips and safely synchronize structured itinerary data with the Trek WeChat mini program.

This skill is ready for commercial/non-commercial use.

## Publisher:

[super21-bat](https://clawhub.ai/user/super21-bat)

### License/Terms of Use:

MIT-0

## Use Case:

External users and compatible agent runtimes use this skill to research trips and synchronize itinerary data, reservations, accommodations, costs, packing lists, todos, files, and collaboration proposals with the Trek WeChat mini program. It supports authenticated MCP access and a CLI fallback for configuration, diagnostics, writes, and readback verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad persistent Trek Agent Key for access to user travel data and writes.

Mitigation: Create one dedicated key per agent, store it in a runtime secret manager, avoid exposing it in files or logs, run diagnostics before writes, and revoke the key when access is no longer needed.

Risk: The skill can install mutable remote CLI code and synchronize globally into agent skill directories.

Mitigation: Install only when the Trek service and GitHub-published CLI source are trusted, verify the connection with doctor, and review global sync behavior before enabling write operations.

Risk: Write operations can affect bookings, costs, deletions, proposal decisions, or rescheduled itinerary data.

Mitigation: Preview high-impact changes, write in small batches, use readback verification, and require user confirmation for destructive, financial, membership, proposal-decision, or rescheduling actions.

## Reference(s):

- [Trek Agent Control Skill Page](https://clawhub.ai/super21-bat/skills/trek-agent-control)
- [Runtime Configuration](references/configuration.md)
- [Dynamic Tool and Field Guide](references/field-guide.md)
- [Research and Synchronization Workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May perform authenticated MCP calls or Trek CLI operations when configured with a user-provided Trek Agent Key.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
