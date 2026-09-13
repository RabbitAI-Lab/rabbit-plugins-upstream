## Description:

Baserow API integration with managed API key authentication for managing database rows, fields, and tables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operational teams use this skill to query and manage Baserow database rows, fields, tables, files, and related automations through Maton-authenticated API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Baserow data through Maton as a gateway and can access rows, fields, tables, and files allowed by the connected account.

Mitigation: Install only when the publisher and Maton gateway are trusted, prefer OAuth, keep Baserow scopes narrow, and use the specific connection required for the task.

Risk: Write, delete, connection, hosted function, trigger, and destination actions can change data or create persistent automation.

Mitigation: Require explicit user approval for each such action, disclose the target resource and effect, and remove unneeded connections, functions, triggers, or destinations after use.

Risk: Raw HTTP fallback with a Maton API key can expose a long-lived credential if handled carelessly.

Mitigation: Use the CLI and OAuth where possible; if raw HTTP is necessary, read the key from the environment, send it only to api.maton.ai, and avoid logging raw responses or credentials.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/baserow-api)
- [Baserow API Documentation](https://baserow.io/api-docs)
- [Baserow Database API](https://baserow.io/user-docs/database-api)
- [Baserow Database Tokens](https://baserow.io/user-docs/personal-api-tokens)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, Python, JSON, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include API request paths, Maton CLI commands, approval prompts, and least-privilege handling guidance.]

## Skill Version(s):

1.2.7 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
