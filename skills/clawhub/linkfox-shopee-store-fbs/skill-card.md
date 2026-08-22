## Description:

Shopee-店铺FBS helps agents query Shopee Brazil FBS enrollment, invoice error, shop block, and SKU block status through LinkFox's Shopee developer proxy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee operators and agent users use this skill to check Brazil FBS enrollment, invoice-error, shop-block, and SKU-block status for authorized Shopee stores. It is also useful when an agent needs onboarding guidance for LinkFox API-key, billing, or dependency issues before calling the FBS APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Shopee shop identifiers and LinkFox API keys to LinkFox-hosted endpoints.

Mitigation: Use only trusted endpoint settings, avoid overriding LinkFox endpoint environment variables unless required, and rotate credentials if exposure is suspected.

Risk: Onboarding can involve SMS login, API-key generation, billing-plan selection, and payment ordering.

Mitigation: Prefer obtaining and setting the API key directly through LinkFox, and use onboarding or payment commands only after confirming the user intends those account actions.

Risk: Full API responses and payment QR outputs may be written to local linkfox session directories.

Mitigation: Review saved files for sensitive shop, token, payment, or account data and delete them when they are no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-fbs)
- [Shopee FBS Enrollment Status API](https://open.shopee.com/documents/v2/v2.fbs.query_br_shop_enrollment_status?module=126&type=1)
- [Shopee FBS Shop Block Status API](https://open.shopee.com/documents/v2/v2.fbs.query_br_shop_block_status?module=126&type=1)
- [Shopee FBS Shop Invoice Error API](https://open.shopee.com/documents/v2/v2.fbs.query_br_shop_invoice_error?module=126&type=1)
- [Shopee FBS SKU Block Status API](https://open.shopee.com/documents/v2/v2.fbs.query_br_sku_block_status?module=126&type=1)
- [Local API Reference](artifact/references/api.md)
- [Local Onboarding Reference](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, JSON, files, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell commands, and JSON API responses saved to local files with stdout summaries for large responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a LinkFox API key and an authorized Shopee shopId or merchantId; full API responses are persisted under a linkfox session directory.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
