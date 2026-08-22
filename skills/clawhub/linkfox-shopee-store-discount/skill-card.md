## Description:

Manages Shopee store discount promotions through LinkFox wrappers for the Shopee Open API Discount module, including creating, listing, updating, ending, deleting, and SIP discount operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, e-commerce operators, and developers use this skill to create and manage discount campaigns for authorized Shopee stores, including item-level discounts and SIP discounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can update, end, or delete live Shopee discount promotions.

Mitigation: Require explicit user confirmation before any update, end, or delete action, and review the target shop, discount ID, and request body before execution.

Risk: The skill handles LinkFox API keys, phone/SMS onboarding, and billing or payment flows.

Mitigation: Use environment variables for API keys, share SMS codes only when intentionally creating or recovering a LinkFox account, and confirm payment choices before ordering.

Risk: Full API responses and stdout logs may contain sensitive store or campaign data.

Mitigation: Treat saved JSON response files and logs as sensitive business data, limit sharing, and remove local copies when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-discount)
- [Shopee Discount API documentation](https://open.shopee.com/documents/v2/v2.discount.add_discount?module=99&type=1)
- [Discount API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to files or printed to stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are written under linkfox/<date>/<session>/data; large responses are summarized unless --inline is used.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
