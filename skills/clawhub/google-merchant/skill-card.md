## Description:

Google Merchant Center API integration with managed OAuth for reading and managing products, inventories, data sources, promotions, account settings, conversions, and reports in Google Shopping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to administer Google Merchant Center through Maton, including Merchant API reads and approved changes to products, inventories, promotions, data sources, account settings, conversions, and reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable Merchant Center actions can change live products, inventory, promotions, data sources, account settings, or conversions.

Mitigation: Default to read and list calls; require explicit user approval with specific resource identifiers before any create, update, or delete operation.

Risk: Creating a connection grants the agent access through the user's authorized Google Merchant Center account.

Mitigation: Confirm the user's intent before creating a connection, select least-privilege scopes when available, and revoke unused connections promptly.

Risk: Trigger destinations and notification subscriptions can establish persistent forwarding of event or Merchant Center data to a URL.

Mitigation: Show the exact destination host, payload fields, and persistence behavior before creation or update; prefer Maton-controlled destinations and avoid third-party hosts unless specifically approved.

Risk: Using a raw Maton API key can expose a long-lived credential through environment variables, logs, command history, or pasted output.

Mitigation: Prefer OAuth through the Maton CLI, use raw HTTP only when the CLI cannot be installed, never print or persist the key, and rotate it if exposure is suspected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-merchant)
- [Maton Homepage](https://maton.ai)
- [Merchant API Overview](https://developers.google.com/merchant/api/overview)
- [Merchant API Reference](https://developers.google.com/merchant/api/reference/rest)
- [Products Guide](https://developers.google.com/merchant/api/guides/products/overview)
- [Data Sources Guide](https://developers.google.com/merchant/api/guides/data-sources/overview)
- [Reports Guide](https://developers.google.com/merchant/api/guides/reports/overview)
- [Product Data Specification](https://support.google.com/merchants/answer/7052112)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, markdown]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Maton CLI commands, raw HTTP examples, SDK snippets, and approval guidance for write-capable Merchant Center operations.]

## Skill Version(s):

1.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
