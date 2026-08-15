## Description:

Sorftime-商品详情 helps agents query Sorftime for Amazon product details and historical ASIN trends across 14 marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and e-commerce analysts use this skill to retrieve ASIN-level product details, price and sales trends, BSR history, profit signals, FBA fees, and marketplace availability from Sorftime.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid external LinkFox/Sorftime data source and may spend account credits.

Mitigation: Use it only when paid Sorftime data is intended, confirm before calls that spend credits, and prefer cached or product-info-only queries when appropriate.

Risk: Credential-bearing network calls can be affected by endpoint override environment variables.

Mitigation: Keep endpoint override variables unset or pinned to trusted LinkFox hosts before providing API keys.

Risk: Onboarding supports phone/SMS registration and order/payment flows.

Mitigation: Avoid those flows unless explicitly needed for authentication or billing, and have the user confirm before creating orders or payment QR codes.

Risk: Full API responses and related artifacts are saved under the local linkfox output directory.

Mitigation: Review and clean the local linkfox directory according to the workspace's data retention expectations.

Risk: The security scan reports silent feedback behavior.

Mitigation: Review feedback behavior before installation and disclose it where deployment policy requires user notice.

## Reference(s):

- [Sorftime Product Detail API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-sorftime-amazon-product-detail)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON files, guidance]

**Output Format:** [Markdown guidance with shell commands, tabular summaries, and saved JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses under a local linkfox session directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
