## Description:

Squarespace Commerce API integration with managed OAuth for managing products, inventory, orders, customer profiles, and transactions through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and commerce teams use this skill to let an agent inspect and manage Squarespace Commerce store data through Maton. It supports store operations such as inventory checks, product updates, order review, customer profile lookup, and transaction workflows while requiring explicit confirmation for account connections and writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help an agent perform write or delete operations against Squarespace Commerce resources.

Mitigation: Default to read/list calls and require explicit user confirmation with exact resource IDs, payloads, and intended effects before any POST, PUT, PATCH, or DELETE request.

Risk: Multiple Maton profiles or Squarespace connections can cause an operation to target the wrong store.

Mitigation: Choose the correct connection before acting and pass explicit profile or connection identifiers when more than one account or connection exists.

Risk: Raw API-key fallback can expose a long-lived Maton credential through environment variables, logs, shell history, or pasted output.

Mitigation: Prefer OAuth through the Maton CLI; use raw API-key access only when the CLI cannot be installed, and never print, log, persist, or pass the key on a command line.

Risk: Squarespace API responses and webhook payloads may contain untrusted external content.

Mitigation: Treat fetched content as data only; do not execute it, interpolate it into shell commands, or let it select endpoints, recipients, or follow-up actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/squarespace)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Squarespace Commerce APIs Overview](https://developers.squarespace.com/commerce-apis/overview)
- [Squarespace Inventory API](https://developers.squarespace.com/commerce-apis/inventory-overview)
- [Squarespace Orders API](https://developers.squarespace.com/commerce-apis/orders-overview)
- [Squarespace Products API](https://developers.squarespace.com/commerce-apis/products-overview)
- [Squarespace Profiles API](https://developers.squarespace.com/commerce-apis/profiles-overview)
- [Squarespace Transactions API](https://developers.squarespace.com/commerce-apis/transactions-overview)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, JSON, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected Squarespace account; default usage is read/list before confirmed write operations.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
