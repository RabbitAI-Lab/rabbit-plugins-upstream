## Description:

Microsoft To Do API integration with managed OAuth for managing task lists, tasks, checklist items, and linked resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to read and manage Microsoft To Do lists and tasks through Maton-authenticated Microsoft Graph calls. It supports task list, task, checklist item, and linked resource workflows while requiring confirmation for connection setup and data-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Microsoft To Do requests are routed through Maton and require trust in the gateway and installed release source.

Mitigation: Install only from the server-resolved ClawHub release, review the publisher profile, and use the skill only when routing requests through Maton is acceptable.

Risk: OAuth or API-key credentials may grant access to Microsoft To Do account data.

Mitigation: Prefer OAuth over API keys, do not inspect or persist credentials, review requested Microsoft permissions, and rotate any API key that was exposed.

Risk: Task, checklist item, linked resource, or list writes and deletions can alter or remove user data.

Mitigation: Default to read/list calls, verify resource identifiers and account context first, and confirm every create, update, or delete operation with the user before execution.

Risk: Multiple Maton accounts or Microsoft To Do connections can cause requests to affect the wrong account.

Mitigation: Specify the intended profile or connection when more than one account or connection exists.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/microsoft-to-do)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Microsoft To Do API Overview](https://learn.microsoft.com/en-us/graph/api/resources/todo-overview)
- [todoTaskList Resource](https://learn.microsoft.com/en-us/graph/api/resources/todotasklist)
- [todoTask Resource](https://learn.microsoft.com/en-us/graph/api/resources/todotask)
- [checklistItem Resource](https://learn.microsoft.com/en-us/graph/api/resources/checklistitem)
- [linkedResource Resource](https://learn.microsoft.com/en-us/graph/api/resources/linkedresource)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands, Microsoft Graph API paths, JSON request bodies, SDK snippets, and safety guidance for authenticated Microsoft To Do operations.]

## Skill Version(s):

1.2.0 (source: server release metadata; skill frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
