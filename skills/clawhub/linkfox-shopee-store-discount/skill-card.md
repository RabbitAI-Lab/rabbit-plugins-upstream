## Description:

Helps agents manage Shopee store Discount promotions through LinkFox scripts for the Shopee Open Platform Discount APIs, including creating, listing, updating, ending, and deleting discounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to manage authorized Shopee store discount campaigns and inspect campaign results. It is intended for store-level promotion workflows that already have LinkFox and Shopee authorization in place.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, end, and delete live Shopee store discount promotions.

Mitigation: Require explicit user confirmation before every create, update, end, or delete operation, and verify shop IDs, merchant IDs, discount IDs, and request bodies before execution.

Risk: The skill handles LinkFox account onboarding, billing actions, and API keys.

Mitigation: Use it only with trusted LinkFox accounts, keep API keys in secure environment variables, and do not paste or expose keys in shared logs or prompts.

Risk: Service URL overrides can redirect operational requests away from the expected LinkFox gateway.

Mitigation: Avoid gateway or service URL environment overrides unless they have been reviewed and approved for the deployment environment.

Risk: Saved and printed responses may contain sensitive store, campaign, billing, or account data.

Mitigation: Protect the linkfox output directory, limit access to response files, and remove stored responses when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-discount)
- [Shopee Discount API reference](https://open.shopee.com/documents/v2/v2.discount.add_discount?module=99&type=1)
- [Discount module API overview](references/api.md)
- [Onboarding and billing guidance](references/onboarding.md)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save complete JSON responses under a linkfox output directory and may print either full JSON or a summary depending on response size.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
