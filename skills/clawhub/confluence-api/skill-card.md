## Description:

Confluence API integration with managed OAuth for managing pages, spaces, blogposts, comments, and attachments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to work with Confluence Cloud content through a Maton-managed OAuth connection. It supports read and write workflows for pages, spaces, blogposts, comments, attachments, and related automation when the user explicitly approves the connection and operation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify or delete real Confluence business content through the user's authorized account.

Mitigation: Default to read and list calls, verify the target resource and payload, and require explicit user confirmation before any POST, PUT, PATCH, DELETE, connection creation, or hosted automation.

Risk: OAuth tokens, API keys, and Confluence response data can expose sensitive business information if printed, logged, or copied into destinations.

Mitigation: Use OAuth where possible, leave credentials in the platform or operating system credential store, avoid dumping raw responses, and extract only the fields needed for the task.

Risk: Persistent trigger destinations or local event handlers can create ongoing data forwarding or unattended actions.

Mitigation: Keep destinations on Maton-controlled or explicitly approved hosts, disclose what data flows and how often, require separate approval for persistent automation, and remove unused connections, functions, and triggers after use.

## Reference(s):

- [ClawHub Confluence skill page](https://clawhub.ai/byungkyu/skills/confluence-api)
- [Maton homepage](https://maton.ai)
- [Confluence REST API V2 Documentation](https://developer.atlassian.com/cloud/confluence/rest/v2/intro/)
- [Confluence REST API V2 Reference](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/)
- [Confluence Storage Format](https://confluence.atlassian.com/doc/confluence-storage-format-790796544.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly trigger reference](references/calendly/triggers.md)
- [GitHub trigger reference](references/github/triggers.md)
- [Google Mail trigger reference](references/google-mail/triggers.md)
- [HubSpot trigger reference](references/hubspot/triggers.md)
- [Linear trigger reference](references/linear/triggers.md)
- [Notion trigger reference](references/notion/triggers.md)
- [Slack trigger reference](references/slack/triggers.md)
- [Stripe trigger reference](references/stripe/triggers.md)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples, code snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Confluence API requests and Maton CLI commands; responses can contain user business data and should be minimized to fields needed for the task.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
