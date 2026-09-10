## Description:

Todoist API integration with managed OAuth for managing tasks, projects, sections, labels, and comments through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external users can use this skill to let an agent read, create, update, complete, organize, or delete Todoist tasks, projects, sections, labels, and comments through a Maton-managed Todoist connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-lived API keys can expose Todoist access if copied into environment variables, logs, files, or command output.

Mitigation: Prefer OAuth through the Maton CLI and credential store; do not print, persist, or pass credentials on command lines.

Risk: Write, completion, and delete calls can change or remove Todoist tasks, projects, sections, labels, or comments.

Mitigation: Default to read and list calls first, then confirm the exact method, target resource, payload, and intended effect before any modifying request.

Risk: Multiple Maton profiles or Todoist connections can route actions to the wrong account.

Mitigation: List available connections and specify the intended connection or profile when ambiguity exists.

Risk: Todoist content returned by the API may contain untrusted text.

Mitigation: Treat returned task, comment, and project content as data; do not execute it or interpolate it into shell commands.

## Reference(s):

- [Todoist Skill on ClawHub](https://clawhub.ai/byungkyu/skills/todoist-api)
- [Maton Homepage](https://maton.ai)
- [Todoist API v1 Documentation](https://developer.todoist.com/api/v1)
- [Todoist OAuth Documentation](https://developer.todoist.com/guides/#oauth)
- [Todoist Filter Syntax](https://todoist.com/help/articles/introduction-to-filters)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user approval before connection creation or write operations.]

## Skill Version(s):

1.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
