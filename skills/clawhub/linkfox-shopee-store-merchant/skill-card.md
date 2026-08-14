## Description:

Helps agents query authorized Shopee cross-border merchant information through LinkFox, including merchant profile, shops under a merchant, warehouse data, warehouse-eligible shops, and prepaid accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and ecommerce operators use this skill to retrieve authorized Shopee cross-border merchant, shop, warehouse, and prepaid-account information from the Merchant module. It is intended for workflows that already have LinkFox API credentials and an authorized Shopee merchant or shop identifier.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access LinkFox and Shopee merchant credentials and authorized merchant data.

Mitigation: Use it only with intended accounts, provide credentials through environment variables, and avoid sharing API keys or merchant identifiers in public transcripts.

Risk: Full merchant API responses may be stored locally and can contain merchant, shop, warehouse, account, or billing-related details.

Mitigation: Review saved linkfox session files before sharing workspaces and remove local response files when they are no longer needed.

Risk: The onboarding flow can handle phone or SMS login, generate API keys, list paid plans, and create payment orders.

Mitigation: Confirm login, API-key generation, plan selection, and payment or QR-code steps explicitly with the user before running onboarding commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-merchant)
- [Artifact API reference](artifact/references/api.md)
- [Onboarding and billing guidance](artifact/references/onboarding.md)
- [Shopee get_merchant_info documentation](https://open.shopee.com/documents/v2/v2.merchant.get_merchant_info?module=93&type=1)
- [Shopee get_shop_list_by_merchant documentation](https://open.shopee.com/documents/v2/v2.merchant.get_shop_list_by_merchant?module=93&type=1)
- [Shopee get_merchant_warehouse_list documentation](https://open.shopee.com/documents/v2/v2.merchant.get_merchant_warehouse_list?module=93&type=1)
- [Shopee get_merchant_warehouse_location_list documentation](https://open.shopee.com/documents/v2/v2.merchant.get_merchant_warehouse_location_list?module=93&type=1)
- [Shopee get_warehouse_eligible_shop_list documentation](https://open.shopee.com/documents/v2/v2.merchant.get_warehouse_eligible_shop_list?module=93&type=1)
- [Shopee get_merchant_prepaid_account_list documentation](https://open.shopee.com/documents/v2/v2.merchant.get_merchant_prepaid_account_list?module=93&type=1)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON responses and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Merchant API calls require LinkFox API credentials and a shopId or merchantId; the generic runner can save full JSON responses under a linkfox session data directory.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
