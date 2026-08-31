## Description:

Squarespace Commerce API integration with managed OAuth for managing products, inventory, orders, customer profiles, and transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and store operators use this skill to manage Squarespace Commerce resources through the Maton CLI with OAuth-backed account access. It supports read/list workflows by default and requires user confirmation before connection creation or writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The raw API passthrough can call any Squarespace API path allowed by the connected account.

Mitigation: Use the narrowest OAuth scopes available, specify the intended connection when multiple accounts exist, and review write or delete requests before execution.

Risk: The skill can access Squarespace commerce data and modify store resources after authorization.

Mitigation: Install only when Maton access to the Squarespace account is intended, default to read/list calls, and confirm connection creation and mutations with the user.

Risk: Using the raw HTTP fallback requires handling a long-lived Maton API key.

Mitigation: Prefer OAuth through the Maton CLI; if the fallback is required, do not print, persist, or pass the key on the command line.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/squarespace)
- [Maton homepage](https://maton.ai)
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

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands target Squarespace through Maton and should be reviewed before write or delete operations.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
