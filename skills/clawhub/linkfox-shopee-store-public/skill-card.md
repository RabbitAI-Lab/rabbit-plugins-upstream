## Description:

Shopee Public module helper for calling six Shopee Open API public endpoints through LinkFox, including partner shop and merchant lookup, OAuth token exchange and refresh, resend-code token retrieval, and Shopee IP range lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and e-commerce operators use this skill to query Shopee Public API data and complete lower-level partner or OAuth operations when the regular authorization skill is not the right entry point. It is intended for LinkFox-backed Shopee workflows that need scripted public endpoint calls and response summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys, Shopee OAuth and token responses, and phone-number based onboarding.

Mitigation: Use approved credentials only, avoid unnecessary production secrets, and rotate any credential that may have been exposed through logs or saved responses.

Risk: Full API responses may be saved locally under the workspace or home LinkFox directory.

Mitigation: Review saved JSON files after use and delete sensitive response files when retention is not required.

Risk: Billing onboarding can include optional payment-order flows.

Mitigation: Confirm the selected plan, payment method, and order details with the user before creating or sharing payment orders.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-public)
- [Shopee Public API Index](https://open.shopee.com/documents/v2/v2.public.get_shops_by_partner?module=104&type=1)
- [API Reference](references/api.md)
- [Onboarding Reference](references/onboarding.md)
- [get_access_token Reference](references/apis/get-access-token.md)
- [get_merchants_by_partner Reference](references/apis/get-merchants-by-partner.md)
- [get_shopee_ip_ranges Reference](references/apis/get-shopee-ip-ranges.md)
- [get_shops_by_partner Reference](references/apis/get-shops-by-partner.md)
- [get_token_by_resend_code Reference](references/apis/get-token-by-resend-code.md)
- [refresh_access_token Reference](references/apis/refresh-access-token.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses or saved JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are summarized when large; full responses may be saved locally for later inspection.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
