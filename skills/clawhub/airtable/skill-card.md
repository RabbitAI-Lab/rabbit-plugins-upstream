## Description:

Airtable API integration with managed OAuth for reading, creating, updating, deleting, and querying bases, tables, and records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Airtable bases, tables, and records through a Maton-managed OAuth connection. The skill defaults to read and list operations and requires explicit user confirmation for writes, connection creation, hosted functions, and persistent triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Airtable OAuth authorization can expose business data from the bases and scopes selected during connection setup.

Mitigation: Prefer read-only or narrow Airtable scopes and create new connections only after the user confirms the intended Airtable access.

Risk: Writes or deletes can change or remove Airtable records.

Mitigation: Confirm every write or delete with exact base, table, record IDs, and payloads before execution.

Risk: Hosted functions and triggers can create ongoing automation that moves sensitive business data without repeated prompts.

Mitigation: Treat each function deployment, invocation, trigger, and destination as a separately approved action, scope payloads narrowly, and prefer platform destinations.

Risk: Using raw HTTP with MATON_API_KEY exposes a long-lived credential to the runtime environment.

Mitigation: Use the CLI OAuth flow when available; if raw HTTP is required, never print, persist, log, or pass the key on a command line.

## Reference(s):

- [ClawHub Airtable Skill](https://clawhub.ai/byungkyu/skills/airtable)
- [Maton Homepage](https://maton.ai)
- [Airtable API Overview](https://airtable.com/developers/web/api/introduction)
- [Airtable List Records](https://airtable.com/developers/web/api/list-records)
- [Airtable Create Records](https://airtable.com/developers/web/api/create-records)
- [Airtable Update Records](https://airtable.com/developers/web/api/update-record)
- [Airtable Delete Records](https://airtable.com/developers/web/api/delete-record)
- [Airtable Formula Reference](https://support.airtable.com/docs/formula-field-reference)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a user-authorized Airtable connection; raw HTTP fallback requires careful Maton API key handling.]

## Skill Version(s):

1.2.3 (source: server release evidence; artifact metadata version 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
