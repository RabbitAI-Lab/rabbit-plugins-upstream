## Description:

Helps dropshipping sellers assess profit, resolve supplier and order problems, improve product listings, and check Shopify stores before launch.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dsers](https://clawhub.ai/user/dsers)

### License/Terms of Use:

MIT-0

## Use Case:

Dropshipping sellers use the skill to evaluate product margins and pricing, respond to supplier or order issues, prepare accurate listings, and review stores before launch. It can work from information supplied by the user or, when connected, use DSers data and save changes to the user's DSers account after approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes to products, prices, or orders can affect the user's account or store.

Mitigation: Show the exact proposed changes and get the user's agreement before applying them; review products, prices, and orders before approval.

Risk: Supplier evidence may contain customer information that is not needed for the task.

Mitigation: Redact unnecessary customer information before sharing supplier evidence.

Risk: Payment testing can involve live charges or automatic fulfillment.

Mitigation: Prefer payment test mode, pause automatic fulfillment during testing, and keep export backups.

## Reference(s):

- [DSers](https://www.dsers.com)
- [DSers MCP server](https://ai.dsers.com/mcp)
- [Profit and pricing guide](references/profit.md)
- [Supplier and order guide](references/suppliers.md)
- [Product listing guide](references/listing.md)
- [Pre-launch store check](references/launch.md)
- [Connecting DSers](references/connect-dsers.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, CSV]

**Output Format:** [Markdown responses and optional Shopify CSV content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use user-provided information or connected DSers data; changes to accounts or stores require explicit user approval.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
