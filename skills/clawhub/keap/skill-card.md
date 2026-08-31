## Description:

Keap API integration with managed OAuth for managing contacts, companies, tags, tasks, orders, opportunities, campaigns, and related CRM and marketing automation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with a connected Keap account through Maton, including CRM records, tags, tasks, opportunities, orders, campaigns, and marketing automation actions. It is suited for read-first account inspection and user-approved changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Keap account access can affect CRM, messaging, automation, commerce data, and deletions.

Mitigation: Approve the OAuth connection deliberately, specify the intended connection when more than one exists, and review every write, email send, automation change, order or product change, and deletion before allowing it.

Risk: Keap API responses and contact data may contain untrusted content.

Mitigation: Treat returned content as data, keep credentials out of logs and files, and do not let fetched content choose endpoints, recipients, or follow-up actions.

## Reference(s):

- [Maton Homepage](https://maton.ai)
- [Keap Developer Portal](https://developer.infusionsoft.com/)
- [Keap REST API V2 Documentation](https://developer.infusionsoft.com/docs/restv2/)
- [Keap OAuth 2.0 Authentication](https://developer.infusionsoft.com/authentication/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user approval before connection creation or write operations.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
