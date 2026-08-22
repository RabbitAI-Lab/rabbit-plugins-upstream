## Description:

Provides agent guidance and scripts for managing Shopee Shop Flash Sale campaigns, including time-slot lookup and creating, updating, listing, adding items to, and deleting flash-sale campaigns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to manage authorized Shopee Shop Flash Sale activity through LinkFox-provided scripts and reference guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires LinkFox API-key access.

Mitigation: Install only if the publisher is trusted and keep API keys scoped, private, and revocable.

Risk: The skill can create, update, and delete Shopee flash-sale data.

Mitigation: Review shop identifiers, campaign identifiers, item lists, prices, and time slots before running write or delete operations.

Risk: The evidence notes account, billing, payment-order, and inconsistent cost-disclosure concerns.

Mitigation: Confirm expected costs and plan terms with the publisher before using billing or onboarding commands.

Risk: Custom LinkFox endpoint environment variables can redirect requests.

Mitigation: Avoid custom endpoint settings unless the destination is known and trusted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-shop-flash-sale)
- [Shopee Shop Flash Sale API Reference](https://open.shopee.com/documents/v2/v2.shop_flash_sale.get_time_slot_id?module=123&type=1)
- [Shop Flash Sale API Overview](references/api.md)
- [LinkFox Onboarding and Account Guidance](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Files, Configuration]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes complete API responses to dated JSON files and may print summaries for responses over 8 KB.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
