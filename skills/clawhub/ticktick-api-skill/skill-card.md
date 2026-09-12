## Description:

TickTick API integration with managed OAuth for managing tasks, projects, and task lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to connect to a user's TickTick account through Maton, then list, create, update, complete, and delete TickTick projects and tasks. It is suited to task-management workflows where the user can approve account connections and data-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act on a connected TickTick account and perform create, update, complete, and delete operations.

Mitigation: Default to read and list calls, verify identifiers and account context first, and require explicit user confirmation before every POST, PUT, PATCH, or DELETE request.

Risk: Long-lived API keys or provider-issued tokens can leak through logs, shell history, process listings, or persisted files.

Mitigation: Prefer OAuth through the Maton CLI, keep credentials in the operating system credential store, never print or persist secrets, and use raw HTTP with MATON_API_KEY only when the CLI cannot be installed.

Risk: The raw Maton API passthrough can reach endpoints beyond the examples when the connected account permits them.

Mitigation: Use the narrowest TickTick scopes available, pin the intended connection when multiple accounts exist, and treat the documented endpoints as the intended operating surface.

Risk: TickTick responses can contain personal task and project data.

Mitigation: Extract only the fields needed for the task and avoid dumping full response bodies into logs, files, or user-visible output unless specifically requested.

Risk: Deleting a connection or TickTick resource can be irreversible and may break existing automation.

Mitigation: List and match the exact resource or connection identifier with the user before deletion, and avoid bypassing interactive prompts unless the user has already confirmed the specific target.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/ticktick-api-skill)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [TickTick Developer Portal](https://developer.ticktick.com/)
- [TickTick Help Center](https://help.ticktick.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include API request paths, payload examples, connection-selection guidance, and data-minimization guidance.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
