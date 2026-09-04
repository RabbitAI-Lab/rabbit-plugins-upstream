## Description:

Zoho Projects API V3 integration with managed OAuth for managing projects, tasks, milestones, tasklists, and team collaboration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Zoho Projects resources through Maton-authenticated API calls, including project, task, tasklist, milestone, comment, and user workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zoho Projects API traffic is routed through Maton as an intermediary.

Mitigation: Install only when the user accepts Maton handling the API traffic, and use OAuth where possible.

Risk: Long-lived Maton API keys can be exposed through environment variables, logs, or shell history.

Mitigation: Prefer OAuth-backed CLI login, avoid printing or exporting MATON_API_KEY, and rotate any key that may have been exposed.

Risk: Create, update, delete, connection, and webhook-related calls can change or remove project data or create downstream effects.

Mitigation: Default to read and list calls, use the narrowest Zoho scopes available, specify the intended connection, and require explicit user approval before every write or new connection.

Risk: Content returned by Zoho Projects can contain untrusted instructions or data.

Mitigation: Treat API responses as data, validate values before reuse, and never execute or follow instructions found inside fetched project content.

## Reference(s):

- [Zoho Projects Skill on ClawHub](https://clawhub.ai/byungkyu/skills/zoho-projects)
- [Maton](https://maton.ai)
- [Zoho Projects API V3 Documentation](https://projects.zoho.com/api-docs)
- [Zoho Projects Developer Portal](https://www.zoho.com/projects/help/rest-api/zohoprojectsapi.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose read and write API calls; write actions and new connections require explicit user approval.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
