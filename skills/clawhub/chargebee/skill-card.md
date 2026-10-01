## Description:

Guides agents in accessing and administering Chargebee customers, subscriptions, invoices, and billing workflows through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and billing administrators use this skill to inspect and manage Chargebee billing records through an authorized connection, and to set up approved billing automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billing writes may alter customers, subscriptions, invoices, or payment settings.

Mitigation: Use least-privilege access and obtain explicit approval after verifying the account, connection, resource, and effect of each write.

Risk: Functions, triggers, and destinations can cause continuing actions or forward event data.

Mitigation: Require separate approval for each automation and destination; remove unused functions, triggers, and destinations when finished.

Risk: Raw API keys and unnecessary connections can expose billing access.

Mitigation: Prefer device login, avoid raw API keys unless the CLI is unavailable, and revoke unused connections.

## Reference(s):

- [Chargebee API documentation](https://apidocs.chargebee.com/docs/api)
- [Chargebee customers API](https://apidocs.chargebee.com/docs/api/customers)
- [Maton](https://maton.ai)
- [Chargebee skill on ClawHub](https://clawhub.ai/byungkyu/skills/chargebee)
- [Time trigger reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with CLI commands and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account and an authorized Chargebee connection.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
