## Description:

Helps agents query Shopee cross-border merchant information through LinkFox, including merchant details, merchant shops, warehouse lists, warehouse locations, warehouse-eligible shops, and prepaid accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and marketplace operators use this skill to inspect authorized Shopee cross-border merchant records, related shops, warehouse information, and prepaid account data. It is intended for workflows that already have LinkFox and Shopee authorization in place.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can handle LinkFox account onboarding, API-key setup, billing order creation, and payment QR display.

Mitigation: Use it only when those account and billing flows are expected, and review payment or credential prompts before acting on them.

Risk: Merchant API responses and QR images may be persisted in the working directory.

Mitigation: Run the skill in a workspace where saved LinkFox response files and QR images will not be synced, shared, or committed.

Risk: Endpoint environment variables can redirect LinkFox calls to alternate hosts.

Mitigation: Keep LinkFox endpoint environment variables unset or set only to trusted hosts before using the scripts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-merchant)
- [Shopee Merchant API: get_merchant_info](https://open.shopee.com/documents/v2/v2.merchant.get_merchant_info?module=93&type=1)
- [Shopee Merchant API: get_shop_list_by_merchant](https://open.shopee.com/documents/v2/v2.merchant.get_shop_list_by_merchant?module=93&type=1)
- [Shopee Merchant API: get_merchant_prepaid_account_list](https://open.shopee.com/documents/v2/v2.merchant.get_merchant_prepaid_account_list?module=93&type=1)
- [Shopee Merchant API: get_merchant_warehouse_list](https://open.shopee.com/documents/v2/v2.merchant.get_merchant_warehouse_list?module=93&type=1)
- [Shopee Merchant API: get_merchant_warehouse_location_list](https://open.shopee.com/documents/v2/v2.merchant.get_merchant_warehouse_location_list?module=93&type=1)
- [Shopee Merchant API: get_warehouse_eligible_shop_list](https://open.shopee.com/documents/v2/v2.merchant.get_warehouse_eligible_shop_list?module=93&type=1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON files]

**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts may print full JSON for smaller responses or a summary for larger responses while saving the complete response under the working directory.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
