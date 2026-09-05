## Description:

This skill gives agents managed OAuth access to Squarespace Commerce APIs for products, inventory, orders, customer profiles, and transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Commerce operators, developers, and agents use this skill to inspect and manage Squarespace store inventory, products, orders, customer profiles, and transactions through Maton-authenticated API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can connect an agent to a Squarespace store with scopes that may allow commerce data access or changes.

Mitigation: Review requested Squarespace scopes during OAuth, prefer read-only access when possible, and install only for stores the user intends Maton to access.

Risk: Product, inventory, order, or deletion operations can change store state or remove data.

Mitigation: Default to read and list calls, specify the target connection for changes, and require explicit user confirmation of the resource, payload, and intended effect before write or delete actions.

Risk: Raw HTTP fallback use requires handling a long-lived Maton API key in the process environment.

Mitigation: Prefer OAuth through the Maton CLI, avoid printing or persisting API keys, send keys only to api.maton.ai, and rotate any key that was exposed.

Risk: Squarespace responses can contain personal or commerce-sensitive data.

Mitigation: Extract only fields needed for the task and avoid logging, saving, or broadly displaying raw API responses unless the user explicitly asks for them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/squarespace)
- [Maton Homepage](https://maton.ai)
- [Squarespace Commerce APIs Overview](https://developers.squarespace.com/commerce-apis/overview)
- [Inventory API](https://developers.squarespace.com/commerce-apis/inventory-overview)
- [Orders API](https://developers.squarespace.com/commerce-apis/orders-overview)
- [Products API](https://developers.squarespace.com/commerce-apis/products-overview)
- [Profiles API](https://developers.squarespace.com/commerce-apis/profiles-overview)
- [Transactions API](https://developers.squarespace.com/commerce-apis/transactions-overview)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON request or response snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run Maton CLI commands and raw HTTP fallback examples when the environment requires them.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
