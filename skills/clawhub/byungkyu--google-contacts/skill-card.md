## Description:

Google Contacts API integration with managed OAuth for managing contacts, contact groups, and address book search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Users and agents use this skill to access the Google People API through Maton-managed OAuth, primarily to list and search contacts and contact groups. With explicit confirmation, it can also create, update, or delete Google Contacts resources and configure related Maton-hosted automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth or API-key use can grant access to personal or business contact data.

Mitigation: Use Maton OAuth where possible, confirm the active account and connection, choose the least privileged scopes available, and avoid exposing MATON_API_KEY except in environments where the CLI cannot be installed.

Risk: Contact writes and deletions can alter or remove address book records.

Mitigation: Default to read and list operations, and require explicit approval with the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE operation.

Risk: Functions, triggers, trigger destinations, and local --exec handlers can create persistent or unattended automation.

Mitigation: Treat each automation step as separately high impact; approve the account, host, data fields, persistence, and cleanup plan before creating or running it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-contacts)
- [Maton](https://maton.ai)
- [Google People API Overview](https://developers.google.com/people/api/rest)
- [People Resource](https://developers.google.com/people/api/rest/v1/people)
- [Contact Groups Resource](https://developers.google.com/people/api/rest/v1/contactGroups)
- [Person Fields Reference](https://developers.google.com/people/api/rest/v1/people#Person)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose authenticated API calls and Maton configuration steps; write operations and automation setup require explicit user approval.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
