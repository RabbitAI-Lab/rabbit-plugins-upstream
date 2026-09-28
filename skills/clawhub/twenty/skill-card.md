## Description:

Twenty CRM provides managed-authentication access for managing companies, people, opportunities, notes, tasks, workflows, and workspace members in Twenty CRM.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to read and manage Twenty CRM records through Maton-managed authentication, with explicit confirmation for writes, new connections, hosted functions, and trigger-based automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and change Twenty CRM data through an authenticated Maton connection.

Mitigation: Prefer OAuth and least-privilege scopes, default to read and list operations, and obtain explicit user confirmation before any write, deletion, or new connection.

Risk: Hosted functions and triggers can automate future actions or forward event data after initial setup.

Mitigation: Use only user-authored or user-reviewed handlers, require separate approval for each deploy, invocation, trigger, destination, and network-policy change, and prefer DENY_ALL outbound networking.

Risk: Long-lived API keys can be exposed through environment variables or copied into unsafe contexts.

Mitigation: Use OAuth and the operating system credential store when possible, reserve raw HTTP or MATON_API_KEY usage for environments where the CLI cannot be installed, and avoid logging full CRM responses.

## Reference(s):

- [Twenty API Documentation](https://docs.twenty.com/developers/extend/api)
- [Twenty GitHub](https://github.com/twentyhq/twenty)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Google Mail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration]

**Output Format:** [Markdown with inline bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include authenticated CRM API request patterns and automation setup guidance; responses can contain CRM personal or business data.]

## Skill Version(s):

1.2.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
