## Description:

Guides agents in accessing and managing Zoho Books accounting records through Maton's authenticated integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents help users review and manage invoices, contacts, bills, expenses, and other records in their authorized Zoho Books account. Users can also request approved, scoped accounting automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to sensitive accounting records may exceed the task's needs.

Mitigation: Authorize only necessary accounts and prefer read-only scopes when available.

Risk: Writes, deletions, and sends can alter financial records or reach external recipients.

Mitigation: Confirm each action with the user, including exact record IDs and intended effects.

Risk: Functions and trigger destinations can create ongoing automation or data forwarding.

Mitigation: Review the function, event scope, destination, and shared data; obtain separate explicit approval for persistent forwarding.

Risk: Raw API keys can expose long-lived access to connected data.

Mitigation: Use managed login where possible and avoid raw API keys unless necessary.

## Reference(s):

- [Zoho Books API v3 documentation](https://www.zoho.com/books/api/v3/introduction/)
- [Maton documentation](https://docs.maton.ai)
- [Maton homepage](https://maton.ai)
- [Zoho Books skill on ClawHub](https://clawhub.ai/byungkyu/skills/zoho-books)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance and results depend on the authorized Zoho Books connection.]

## Skill Version(s):

1.2.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
