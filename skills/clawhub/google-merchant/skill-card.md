## Description:

Google Merchant Center API integration with managed OAuth that can read, create, update, and delete products, inventories, data sources, promotions, account settings, and conversions in Google Shopping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to administer Google Merchant Center through Maton. It supports account, product, inventory, promotion, data source, report, notification, and conversion workflows while directing agents to start with read/list calls and obtain explicit confirmation before changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make high-impact Google Merchant Center changes to products, inventory, data sources, promotions, notifications, conversions, and account settings.

Mitigation: Default to read/list calls, verify the account, connection, resource identifiers, payload, and expected effect, then require explicit user confirmation before any write or connection change.

Risk: Raw HTTP fallback requires handling a long-lived Maton API key.

Mitigation: Prefer OAuth through the Maton CLI; if fallback is necessary, read the key from the process environment only, never print or persist it, and send it only to api.maton.ai.

Risk: Multiple Maton profiles or Merchant Center connections can make the target account ambiguous.

Mitigation: List and review active connections, then pin the intended connection and profile before taking action.

Risk: Data returned by Google Merchant Center can contain untrusted content.

Mitigation: Treat API responses as data, extract only task-relevant fields, and do not execute or follow instructions contained in returned content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-merchant)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Merchant API Overview](https://developers.google.com/merchant/api/overview)
- [Merchant API Reference](https://developers.google.com/merchant/api/reference/rest)
- [Products Guide](https://developers.google.com/merchant/api/guides/products/overview)
- [Data Sources Guide](https://developers.google.com/merchant/api/guides/data-sources/overview)
- [Reports Guide](https://developers.google.com/merchant/api/guides/reports/overview)
- [Product Data Specification](https://support.google.com/merchants/answer/7052112)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, markdown]

**Output Format:** [Markdown with inline shell commands, JSON request bodies, and API paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and OAuth or a Maton API key; Google Merchant Center API rate limits apply.]

## Skill Version(s):

1.2.2 (source: server release metadata, released 2026-09-04)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
