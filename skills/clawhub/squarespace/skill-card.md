## Description:

Squarespace Commerce API integration with managed OAuth for managing products, inventory, orders, customer profiles, and transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Squarespace Commerce operations through Maton-mediated OAuth, including inventory, products, orders, customer profiles, and transactions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad authenticated Squarespace API passthrough that can read or modify sensitive store data beyond the documented endpoint list.

Mitigation: Use the narrowest OAuth scopes available, prefer read-only calls, verify the selected connection before writes or deletes, and require explicit user confirmation for data-changing operations.

Risk: Raw API-key fallback can expose a long-lived Maton credential if used unnecessarily.

Mitigation: Prefer OAuth through the Maton CLI and avoid the raw API-key fallback unless the CLI is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/squarespace)
- [Maton homepage](https://maton.ai)
- [Squarespace Commerce APIs Overview](https://developers.squarespace.com/commerce-apis/overview)
- [Squarespace Inventory API](https://developers.squarespace.com/commerce-apis/inventory-overview)
- [Squarespace Orders API](https://developers.squarespace.com/commerce-apis/orders-overview)
- [Squarespace Products API](https://developers.squarespace.com/commerce-apis/products-overview)
- [Squarespace Profiles API](https://developers.squarespace.com/commerce-apis/profiles-overview)
- [Squarespace Transactions API](https://developers.squarespace.com/commerce-apis/transactions-overview)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing operational guidance and command examples for authenticated Squarespace API calls.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
