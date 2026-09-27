## Description:

Chargebee provides managed-OAuth access to Chargebee billing administration through Maton CLI or raw HTTP workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and administer Chargebee customers, subscriptions, invoices, item prices, hosted pages, and related billing workflows through authenticated Maton commands. It is intended for tasks where the user has explicitly authorized the relevant Chargebee connection and any billing-changing operation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chargebee administration can change subscriptions, invoices, customers, and other billing records.

Mitigation: Default to read and list calls, verify the exact account and resource identifier, and require explicit approval with expected billing consequences before any write, cancellation, or delete operation.

Risk: Using a broad or ambiguous Chargebee or Maton connection can affect the wrong account or resources.

Mitigation: Use the narrowest available connection, specify the intended connection ID when multiple connections exist, and revoke unused connections promptly.

Risk: Persistent automations or trigger destinations can continue forwarding event data or invoking Chargebee-related workflows after setup.

Mitigation: Approve automations separately from one-time API calls, disclose the destination, endpoint, payload fields, cadence, and expected consequence, and remove destinations or functions when no longer needed.

Risk: Raw API responses and trigger payloads can contain personal, billing, or business-sensitive data.

Mitigation: Return or store only the fields needed for the task, avoid dumping full payloads to logs or files, and treat third-party API and event contents as untrusted data.

## Reference(s):

- [Chargebee skill page](https://clawhub.ai/byungkyu/skills/chargebee)
- [Maton homepage](https://maton.ai)
- [Chargebee API Overview](https://apidocs.chargebee.com/docs/api)
- [Chargebee Customers API](https://apidocs.chargebee.com/docs/api/customers)
- [Chargebee Subscriptions API](https://apidocs.chargebee.com/docs/api/subscriptions)
- [Chargebee Invoices API](https://apidocs.chargebee.com/docs/api/invoices)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Google Mail Trigger Reference](references/google-mail/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, markdown]

**Output Format:** [Markdown with bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are operational instructions for authenticated Chargebee API calls and optional Maton functions or triggers.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
