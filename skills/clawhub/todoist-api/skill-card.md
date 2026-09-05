## Description:

Todoist API integration with managed OAuth for managing Todoist tasks, projects, sections, labels, and comments through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to Todoist through Maton, inspect existing work items, and create, update, complete, or organize tasks and projects with user confirmation for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can read Todoist data and, after confirmation, modify tasks, projects, sections, labels, comments, and connections through Maton.

Mitigation: Prefer OAuth, start with read/list calls, specify the intended connection or profile when accounts are ambiguous, and approve write, delete, or connection changes only after checking the exact target and payload.

Risk: A long-lived Maton API key can leak if it is printed, logged, persisted, or passed on a command line.

Mitigation: Use CLI OAuth when possible; when raw HTTP is required, read MATON_API_KEY from the process environment, never print or persist it, send it only to api.maton.ai, and rotate it after exposure.

Risk: Todoist task or comment content may include untrusted instructions or data.

Mitigation: Treat API content as data, avoid executing or interpolating it into commands, and do not let fetched content choose follow-up endpoints, recipients, or operations.

## Reference(s):

- [Todoist API v1 Documentation](https://developer.todoist.com/api/v1)
- [Todoist Filter Syntax](https://todoist.com/help/articles/introduction-to-filters)
- [Todoist OAuth Documentation](https://developer.todoist.com/guides/#oauth)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Maton CLI or raw HTTPS examples; Todoist API responses may contain user data and should be minimized to task-relevant fields.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter says 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
