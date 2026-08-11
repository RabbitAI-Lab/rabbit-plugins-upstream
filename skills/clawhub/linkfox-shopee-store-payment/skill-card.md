## Description:

Shopee（虾皮）店铺支付结算（与 linkfox-shopee-store-auth 同系列），经 /shopee/developerProxy 转发 Shopee Open API Payment 模块全部 18 个接口：get_escrow_detail、get_escrow_list、get_payout_detail、get_wallet_transaction_list、get_income_overview、generate_income_report 等。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee sellers, operators, and developers use this skill to query authorized store payment, escrow, payout, wallet transaction, income report, and installment data through LinkFox's Shopee payment API wrappers. It can also generate or retrieve income statements and reports for settlement review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill accesses sensitive Shopee payment, settlement, wallet, and payout data through LinkFox APIs.

Mitigation: Install and use it only for authorized Shopee stores, review LINKFOX_* API-key environment variables before execution, and limit access to users who need settlement data.

Risk: Payment and settlement responses are saved locally in plaintext JSON files.

Mitigation: Run the scripts from an appropriate workspace, restrict local file permissions, and remove saved response files when they are no longer needed.

Risk: The skill includes set_* installment operations that can change live payment settings.

Mitigation: Require explicit user confirmation before running set_item_installment_status or set_shop_installment_status, and verify the target shop or merchant identifier first.

Risk: The onboarding and billing flow may involve account setup, SMS verification, API keys, or credit purchases.

Mitigation: Use the onboarding flow only when intended, avoid bundled purchase or order actions unless credits are deliberately being bought, and stop on unclear 401, 402, quota, or balance errors.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-payment)
- [LinkFox publisher profile](https://clawhub.ai/user/linkfox-ai)
- [Shopee Payment API index](https://open.shopee.com/documents/v2/v2.payment.get_escrow_detail?module=97&type=1)
- [Payment module reference](references/api.md)
- [Onboarding and auth guidance](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts write full API responses under a local linkfox data directory and print either full JSON or a summary depending on response size.]

## Skill Version(s):

1.0.4 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
