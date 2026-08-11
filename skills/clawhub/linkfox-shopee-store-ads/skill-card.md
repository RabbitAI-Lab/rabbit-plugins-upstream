## Description:

Helps agents work with Shopee store advertising by calling 23 Shopee Open API Ads endpoints through LinkFox, including ad balance, manual product ads, campaign performance, recommendations, and GMS campaign operations after AD authorization is confirmed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to query Shopee Ads account data and perform store advertising workflows such as balance checks, keyword recommendations, product ad creation or edits, and campaign performance analysis. It should be used only after the target store has LinkFox AD authorization and Shopee advertising capability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform Shopee Ads account operations, including create and edit requests that may affect campaign spend or ad behavior.

Mitigation: Review all create and edit ad request bodies, campaign identifiers, budgets, bids, and keyword changes before execution.

Risk: The skill handles LinkFox API keys and can guide phone/SMS onboarding and payment or order flows when authentication or billing is missing.

Mitigation: Prefer a pre-issued API key stored in a secure environment variable, enter SMS codes only when intentionally onboarding the account, and verify plan and payment details before creating orders.

Risk: The skill saves complete API responses locally, which may include sensitive Shopee store, campaign, account, or business performance data.

Mitigation: Periodically review and clean the local linkfox response files, and avoid sharing saved response directories without checking their contents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-ads)
- [Shopee Ads API index](https://open.shopee.com/documents/v2/v2.ads.get_total_balance?module=117&type=1)
- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses; full responses are saved as local JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses at or below 8 KB are printed in full after saving; larger responses are summarized unless --inline is used.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
