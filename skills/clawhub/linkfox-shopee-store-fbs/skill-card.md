## Description:

This skill helps agents query Shopee Brazil FBS shop enrollment status, invoice errors, shop block status, and SKU block status through LinkFox's Shopee developer proxy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators and agent users use this skill to inspect authorized Shopee Brazil FBS shop and SKU status, including enrollment, invoice, and block-state checks. It is most relevant when the user already has LinkFox credentials and the companion Shopee store authorization skill installed.

### Deployment Geography for Use:

Global; functional scope is Shopee Brazil FBS shops.

## Known Risks and Mitigations:

Risk: The skill uses LinkFox API credentials and can contact LinkFox network services.

Mitigation: Use it only in a private workspace, keep API keys out of shared logs and repositories, and avoid custom LINKFOX_* endpoint overrides unless the endpoints are trusted.

Risk: The bundled onboarding flow can guide phone/SMS login and create payment orders for billing errors.

Mitigation: Review the onboarding and payment flow before use, and remove or disable it if the deployment only needs read-only Shopee FBS status queries.

Risk: API responses may be retained as local JSON files in a linkfox session data directory.

Mitigation: Treat saved response files as potentially sensitive store data and apply the workspace's normal access control and cleanup practices.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-fbs)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [FBS API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [Shopee query_br_shop_enrollment_status documentation](https://open.shopee.com/documents/v2/v2.fbs.query_br_shop_enrollment_status?module=126&type=1)
- [Shopee query_br_shop_invoice_error documentation](https://open.shopee.com/documents/v2/v2.fbs.query_br_shop_invoice_error?module=126&type=1)
- [Shopee query_br_shop_block_status documentation](https://open.shopee.com/documents/v2/v2.fbs.query_br_shop_block_status?module=126&type=1)
- [Shopee query_br_sku_block_status documentation](https://open.shopee.com/documents/v2/v2.fbs.query_br_sku_block_status?module=126&type=1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts may write full API responses to a local linkfox session data directory and print either full JSON or a summary depending on response size.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
