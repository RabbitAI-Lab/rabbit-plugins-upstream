## Description:

Chargebee helps agents administer Chargebee billing resources through Maton-managed OAuth and CLI/API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and billing operations teams use this skill to list, inspect, and administer Chargebee customers, subscriptions, invoices, hosted pages, and portal sessions through an agent. It is intended for controlled billing administration where account, connection, endpoint, payload, and financial impact are verified before changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact writes can change billing records, subscriptions, invoices, customers, hosted pages, or portal sessions.

Mitigation: Use least-privilege Chargebee access, retrieve and verify the target resource first, and require explicit user confirmation with endpoint, account, resource ID, payload, and consequence before any write.

Risk: The passthrough API can reach native Chargebee API paths.

Mitigation: Use documented endpoint paths, specify the intended connection, and review exact endpoints and payloads before approving changes.

Risk: Fallback API-key use can expose a long-lived Maton credential if printed, logged, persisted, or passed on a command line.

Mitigation: Prefer OAuth through the Maton CLI and operating-system credential storage; if raw HTTP is unavoidable, never print, log, persist, or command-line pass the key and send it only to api.maton.ai.

## Reference(s):

- [Chargebee ClawHub Skill](https://clawhub.ai/byungkyu/skills/chargebee)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Chargebee API Overview](https://apidocs.chargebee.com/docs/api)
- [Chargebee Customers API](https://apidocs.chargebee.com/docs/api/customers)
- [Chargebee Subscriptions API](https://apidocs.chargebee.com/docs/api/subscriptions)
- [Chargebee Invoices API](https://apidocs.chargebee.com/docs/api/invoices)
- [Chargebee Hosted Pages API](https://apidocs.chargebee.com/docs/api/hosted_pages)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown with inline shell, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing instructions for authenticated Chargebee API calls through Maton, including read-first workflow and explicit confirmation before writes.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact frontmatter version 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
