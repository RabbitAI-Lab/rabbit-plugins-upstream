## Description:

Shopee-店铺AMS helps agents operate Shopee Affiliate Marketing Solutions through LinkFox scripts for authorized-shop campaign, product, affiliate, commission, and performance APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and developers use this skill to inspect and manage Shopee AMS open campaigns, targeted campaigns, affiliate lists, commission settings, and performance reports for authorized Shopee shops.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Shopee AMS operations through LinkFox, including state-changing and bulk campaign actions.

Mitigation: Confirm destructive or bulk campaign changes manually before execution and review saved responses after high-impact operations.

Risk: API keys, phone numbers, shop IDs, tokens, saved JSON responses, payment details, and order details may be sensitive.

Mitigation: Treat those values as secrets, avoid sharing saved linkfox output directories, and clean local output directories when no longer needed.

Risk: Environment variables can alter LinkFox endpoint selection.

Mitigation: Use trusted LinkFox endpoint environment values only and avoid inheriting untrusted shell environments when running the scripts.

Risk: The security scan verdict is suspicious because credential, billing, payment, broad local logging, and high-impact campaign mutation behavior require review.

Mitigation: Install only after reviewing the security summary and guidance from the release evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-ams)
- [Shopee AMS official API index](https://open.shopee.com/documents/v2/v2.ams.get_open_campaign_added_product?module=127&type=1)
- [AMS parameter and field reference](artifact/references/api.md)
- [Authentication and billing onboarding reference](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with Python command examples and JSON API responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under linkfox/<date>/<session>/data; stdout prints the full response for small payloads and summaries for larger payloads.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
