## Description:

Google Merchant Center API integration with managed OAuth for reading and administering products, inventories, data sources, promotions, account settings, conversions, and reports in Google Shopping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect through Maton and manage Google Merchant Center resources. It supports read/list workflows by default and write workflows only after the user confirms the account, resource identifiers, payload, and intended effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change products, inventories, data sources, promotions, account settings, conversions, and related shopping data.

Mitigation: Default to read/list calls, verify the current resource state, and require explicit user approval with exact account and resource identifiers before any POST, PUT, PATCH, or DELETE.

Risk: Credentials or API keys could be exposed if authentication is handled outside the Maton CLI flow.

Mitigation: Prefer OAuth, avoid printing or persisting secrets, pass raw HTTP credentials only through stdin when the CLI cannot be used, and revoke unused connections when finished.

Risk: A request could target the wrong Merchant Center account or Maton profile when multiple connections exist.

Mitigation: List active connections first and specify the intended connection and profile for account-sensitive or write operations.

Risk: Content returned from Google Merchant Center is external data and may contain misleading or adversarial text.

Mitigation: Treat API responses as data only; do not execute returned content or let it choose follow-up endpoints, recipients, or commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-merchant)
- [Maton Homepage](https://maton.ai)
- [Merchant API Overview](https://developers.google.com/merchant/api/overview)
- [Merchant API Reference](https://developers.google.com/merchant/api/reference/rest)
- [Products Guide](https://developers.google.com/merchant/api/guides/products/overview)
- [Data Sources Guide](https://developers.google.com/merchant/api/guides/data-sources/overview)
- [Reports Guide](https://developers.google.com/merchant/api/guides/reports/overview)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and Google Merchant Center authorization; writes require explicit user approval.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact frontmatter metadata version 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
