## Description:

Shopee-店铺广告 helps agents query Shopee Ads balances, recommendations, performance reports, and create or edit product and GMS advertising campaigns for authorized Shopee shops through LinkFox.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee sellers, operators, and developers use this skill to inspect authorized shop advertising accounts, retrieve CPC and campaign performance data, get recommendations, and manage paid product or GMS campaigns. Users should review any create, edit, onboarding, or payment action before it runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access LinkFox and Shopee Ads using an API key and read advertising account data.

Mitigation: Install and run it only for shops where the user intends to grant advertising-account access, and remove shell-profile API keys when they are no longer needed.

Risk: Create and edit operations can change paid Shopee advertising campaigns.

Mitigation: Review every campaign creation, edit, order, and payment action before execution, including target shop, campaign body, budget, and identifiers.

Risk: Onboarding and billing flows may involve phone numbers, SMS codes, payment plans, payment URLs, or QR images.

Mitigation: Use those flows only when explicitly setting up or recharging a LinkFox account, and do not provide SMS codes or create payment orders unless that is the intended action.

Risk: Saved response JSON may contain advertising account, campaign, performance, or billing-related data.

Mitigation: Run the skill from a trusted workspace and delete saved response JSON, QR images, and other local artifacts when they are no longer needed.

Risk: Custom gateway URL overrides can redirect API traffic to an endpoint other than the default LinkFox gateway.

Mitigation: Avoid gateway environment overrides unless the endpoint is trusted and expected for the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-ads)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [Shopee Ads get_total_balance official reference](https://open.shopee.com/documents/v2/v2.ads.get_total_balance?module=117&type=1)
- [API reference](references/api.md)
- [Onboarding and billing guidance](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save full API responses as JSON files under a linkfox session directory; large responses may be summarized unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
