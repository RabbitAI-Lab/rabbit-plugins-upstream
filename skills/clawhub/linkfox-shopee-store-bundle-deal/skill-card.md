## Description:

Shopee（虾皮）套装优惠 Bundle Deal（与 linkfox-shopee-store-auth 同系列），经 /shopee/developerProxy 转发 Shopee Open API Bundle Deal 模块全部 10 个接口：add_bundle_deal、get_bundle_deal_list、add_bundle_deal_item、update_bundle_deal、end_bundle_deal 等。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and developers use this skill to manage Shopee store Bundle Deal promotions through LinkFox, including creating, listing, updating, ending, and deleting bundle deals and bundle-deal items. It depends on an authorized Shopee store selection from the companion authentication skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make real changes to Shopee bundle promotions, including creating, updating, ending, and deleting deals or items.

Mitigation: Require an explicit preview and confirmation of shopId, bundle_deal_id, affected items, and intended action before running write or destructive endpoints.

Risk: The artifact contains conflicting cost statements, while the security guidance says the credit-cost contradiction needs publisher review.

Mitigation: Confirm the current LinkFox credit or billing behavior with the publisher before repeated calls or onboarding/payment flows.

Risk: Full API responses are saved to local linkfox session data files and may contain store or promotion details.

Mitigation: Treat local response logs as sensitive operational data and delete them when they are no longer needed.

Risk: Environment URL overrides can redirect calls away from the default LinkFox gateway.

Mitigation: Use gateway override environment variables only in organization-controlled environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-bundle-deal)
- [Shopee Bundle Deal API Reference](https://open.shopee.com/documents/v2/v2.bundle_deal.add_bundle_deal?module=110&type=1)
- [Bundle Deal API Overview](references/api.md)
- [Onboarding and Billing Recovery](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses saved as local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Small responses are printed in full; larger responses are summarized while full JSON is written under a local linkfox session data directory.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
