## Description:

Microsoft To Do API integration with managed OAuth for reading and managing task lists, tasks, checklist items, and linked resources through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect a Microsoft To Do account through Maton and create, read, update, or delete task lists, tasks, checklist items, and linked resources with user confirmation for new connections and writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read, create, update, and delete Microsoft To Do data through Maton.

Mitigation: Default to read and list calls, confirm the target resource and payload before writes, and revoke unused connections when no longer needed.

Risk: New Microsoft To Do account connections grant OAuth/API access through Maton.

Mitigation: Use OAuth where possible, require user approval before creating connections, select the least privilege scope available, and pin the intended connection when multiple accounts exist.

Risk: API keys or provider-issued tokens may be exposed if printed, logged, persisted, or passed on command lines.

Mitigation: Let the CLI and operating system credential store handle credentials, avoid inspecting stored secrets, and send Maton API keys only to api.maton.ai when raw HTTP access is unavoidable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/microsoft-to-do)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Microsoft To Do API Overview](https://learn.microsoft.com/en-us/graph/api/resources/todo-overview)
- [todoTaskList Resource](https://learn.microsoft.com/en-us/graph/api/resources/todotasklist)
- [todoTask Resource](https://learn.microsoft.com/en-us/graph/api/resources/todotask)
- [checklistItem Resource](https://learn.microsoft.com/en-us/graph/api/resources/checklistitem)
- [linkedResource Resource](https://learn.microsoft.com/en-us/graph/api/resources/linkedresource)
- [Related api-gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, API paths, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an active Microsoft To Do connection.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
