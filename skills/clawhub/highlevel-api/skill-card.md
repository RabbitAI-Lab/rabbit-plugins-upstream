## Description:

Guides agents in managing GoHighLevel contacts, pipelines, calendars, conversations, payments, and automations through a connected Maton account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and developers use this skill to find and manage GoHighLevel CRM records, appointments, conversations, payments, and connected automations with their authorized accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized operations can change CRM records, messages, appointments, or billing data.

Mitigation: Verify the connection, account, target resource, and intended effect; obtain explicit approval before each write.

Risk: Triggers and destinations can act repeatedly or forward event data continuously.

Mitigation: Confirm the destination, payload, and ongoing behavior separately before enabling them.

Risk: Long-lived API keys can be exposed if mishandled.

Mitigation: Prefer OAuth/CLI authentication and keep any API key out of logs, commands, and shared output.

## Reference(s):

- [GoHighLevel Marketplace API documentation](https://marketplace.gohighlevel.com/docs/)
- [GoHighLevel Private Integration Token guide](https://marketplace.gohighlevel.com/docs/integrations/custom-token)
- [Maton homepage](https://maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authorized GoHighLevel connection; confirm writes before execution.]

## Skill Version(s):

1.2.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
