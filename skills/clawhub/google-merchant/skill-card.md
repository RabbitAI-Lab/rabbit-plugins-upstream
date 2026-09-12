## Description:

Google Merchant Center API integration with managed OAuth for reading and administering products, inventories, data sources, promotions, account settings, reports, and conversions in Google Shopping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent work with Google Merchant Center data through Maton-managed authentication. It supports catalog, inventory, promotion, data source, account, report, and conversion workflows, with write-capable operations requiring explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration can perform write-capable Merchant Center administration through Maton-mediated access.

Mitigation: Use OAuth where possible, grant the narrowest available scopes, default to read/list calls, and require explicit approval with specific resource identifiers before write or delete operations.

Risk: API keys or returned provider credentials could be exposed if printed, logged, stored, or passed through broad process environments.

Mitigation: Prefer the Maton CLI credential store, avoid printing or persisting credentials, send API keys only to api.maton.ai, and rotate any key that was exposed.

Risk: Ambiguous account or connection selection can apply a change to the wrong Merchant Center account.

Mitigation: Specify connection IDs and profile names when multiple accounts exist, retrieve the target resource first, and confirm the intended effect before executing changes.

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

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline shell commands, API paths, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Google Merchant Center connection; outputs may include Google Merchant Center resource data returned by API calls.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
