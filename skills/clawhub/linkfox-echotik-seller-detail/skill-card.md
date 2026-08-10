## Description:

Fetches the full profile of a single TikTok Shop store by sellerId, including sales, GMV, followers, ratings, fulfillment, product, category, and promotion reach metrics from EchoTik.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and e-commerce analysts use this skill to inspect one known TikTok Shop store's performance profile and benchmark sales, GMV, store health, product, category, and promotion reach indicators.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the configured LinkFox API key and seller lookup data to LinkFox services.

Mitigation: Install and run it only when the user trusts LinkFox with those credentials and lookup details.

Risk: Authentication and billing troubleshooting can collect phone/SMS onboarding data and create payment orders.

Mitigation: Use onboarding and order flows only after explicit user intent, and review returned order or account details before proceeding.

Risk: Environment variables can redirect LinkFox base URLs.

Mitigation: Set LinkFox URL override variables only to trusted HTTPS LinkFox services.

Risk: The skill writes full API responses to local linkfox session and cache directories.

Mitigation: Review local output locations and handle stored seller profile data according to the user's data retention expectations.

Risk: The bundled feedback behavior may send user feedback text to LinkFox.

Mitigation: Report feedback only when it matches the documented feedback criteria and avoid including unnecessary sensitive content.

## Reference(s):

- [EchoTik-TikTok店铺详情 API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-seller-detail)

## Skill Output:

**Output Type(s):** [text, json, files, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses, local JSON files, and optional shell commands for authentication or billing setup]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires sellerId input; full API responses are written under local linkfox session/cache directories and may be summarized on stdout when large.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
