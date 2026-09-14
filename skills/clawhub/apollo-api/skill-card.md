## Description:

Apollo.io API integration with managed OAuth for searching and enriching people and companies, and for managing contacts, accounts, and sales data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, sales operations teams, and agents use this skill to work with Apollo.io data through Maton-managed authentication. It supports prospecting, lead enrichment, and sales-record management while defaulting to read and list actions unless the user confirms a write.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apollo access uses user-authorized credentials and may expose long-lived API keys if OAuth is not used.

Mitigation: Prefer OAuth, keep credentials in the operating system credential store, and avoid printing, exporting, or embedding API keys.

Risk: Write, sequence, or workflow actions can modify sales data or trigger downstream effects.

Mitigation: Default to read and list calls, then confirm the target resource, payload, and intended effect before any write action.

Risk: Hosted functions and triggers can continue running or forwarding data after setup.

Mitigation: Review and approve each function or trigger separately, use restrictive network policy where possible, and delete automation when it is no longer needed.

Risk: Apollo searches and enrichment can send business or personal data to a third-party service and return third-party personal data.

Mitigation: Send only task-required fields, avoid unnecessary bulk collection, and treat onward use of returned personal data as a user compliance decision.

## Reference(s):

- [Apollo API Overview](https://docs.apollo.io/reference)
- [Search People](https://docs.apollo.io/reference/people-api-search.md)
- [Enrich Person](https://docs.apollo.io/reference/people-enrichment.md)
- [Search Organizations](https://docs.apollo.io/reference/organization-search.md)
- [Search Contacts](https://docs.apollo.io/reference/search-for-contacts.md)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Apollo API calls through the Maton CLI or raw HTTP; write actions and new connections require user confirmation.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
