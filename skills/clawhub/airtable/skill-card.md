## Description:

Airtable API integration with managed OAuth for reading, creating, updating, deleting, and querying Airtable bases, tables, and records through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Airtable through a managed Maton connection, including listing bases, querying records, performing approved writes, and setting up approved hosted automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill mediates access to a user's Airtable account and may request scopes that expose business data.

Mitigation: Install only when Maton-mediated Airtable access is intended, review requested Airtable scopes carefully, and prefer read-only access when possible.

Risk: Write, delete, connection, function, or trigger actions can change data or create ongoing automation.

Mitigation: Confirm every write, delete, new connection, hosted function, and automation setup with the user before execution.

Risk: Trigger destinations can continuously forward Airtable-derived or connected-app data outside the expected environment.

Mitigation: Avoid third-party trigger destinations unless the user explicitly trusts the destination and understands what data will be forwarded continuously.

## Reference(s):

- [Airtable API Overview](https://airtable.com/developers/web/api/introduction)
- [Airtable List Records](https://airtable.com/developers/web/api/list-records)
- [Airtable Create Records](https://airtable.com/developers/web/api/create-records)
- [Airtable Update Records](https://airtable.com/developers/web/api/update-record)
- [Airtable Delete Records](https://airtable.com/developers/web/api/delete-record)
- [Airtable Formula Reference](https://support.airtable.com/docs/formula-field-reference)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with CLI commands, HTTP examples, JSON payloads, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses managed OAuth where available and requires explicit user confirmation before writes, connection creation, deletion, hosted functions, or trigger automation.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
