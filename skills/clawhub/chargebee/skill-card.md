## Description:

Chargebee API integration with managed OAuth for billing administration through the Maton CLI and gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to administer Chargebee billing resources such as customers, subscriptions, invoices, hosted pages, and portal sessions through Maton-managed authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billing administration actions can modify customers, subscriptions, invoices, hosted pages, portal sessions, or other financial records.

Mitigation: Default to read and list calls, verify the endpoint, account, resource ID, and expected consequence, then require explicit user confirmation before any write operation.

Risk: Credentials or provider-issued tokens could be exposed through logs, files, command arguments, or direct inspection.

Mitigation: Use OAuth where possible, let the CLI and operating system credential store manage secrets, and never print, persist, export, or inspect credential values.

Risk: An ambiguous Maton profile or Chargebee connection could send requests to the wrong account.

Mitigation: Verify authentication and active connections before requests, and specify the intended profile or connection when multiple accounts are available.

Risk: Chargebee API responses or webhook payloads may contain untrusted external content.

Mitigation: Treat returned content as data only; do not execute, evaluate, or let it choose endpoints, recipients, or follow-up actions.

Risk: Raw HTTP fallback requires holding a long-lived Maton API key in the process environment.

Mitigation: Use the fallback only when the CLI is unavailable, read the key only from the environment, send it only to api.maton.ai, and rotate it if exposed.

## Reference(s):

- [ClawHub Chargebee Skill](https://clawhub.ai/byungkyu/skills/chargebee)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
- [Chargebee API Overview](https://apidocs.chargebee.com/docs/api)
- [Chargebee Customers API](https://apidocs.chargebee.com/docs/api/customers)
- [Chargebee Subscriptions API](https://apidocs.chargebee.com/docs/api/subscriptions)
- [Chargebee Invoices API](https://apidocs.chargebee.com/docs/api/invoices)
- [Chargebee Hosted Pages API](https://apidocs.chargebee.com/docs/api/hosted_pages)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an active Chargebee connection; write operations require explicit user confirmation.]

## Skill Version(s):

1.2.0 (source: server release evidence; artifact frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
