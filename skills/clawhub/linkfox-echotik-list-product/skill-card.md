## Description:

EchoTik-TikTok商品搜索 helps agents search and analyze TikTok Shop product data, including sales, GMV, pricing, ratings, commission rates, and influencer promotion metrics across supported marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and e-commerce researchers use this skill to find and compare TikTok Shop products by keyword, marketplace, sales volume, GMV, price, rating, commission, and influencer promotion signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox API credentials and supports SMS-based onboarding flows.

Mitigation: Use only trusted LinkFox credentials, avoid sharing SMS codes or API keys in transcripts, and rotate credentials if exposure is suspected.

Risk: The skill can initiate LinkFox-hosted billing and payment flows.

Mitigation: Review plan details, payment method, and QR-code or payment-link destination before presenting or scanning payment information.

Risk: Product results, account-related outputs, and cache files may remain in the local linkfox directory.

Mitigation: Clear the local linkfox output and cache directories when stored product results or account details should not persist.

Risk: The skill may automatically report feedback when behavior, results, or user sentiment indicate a quality issue or praise.

Mitigation: Review feedback content before submission when user comments or task context may contain sensitive information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-list-product)
- [API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [LinkFox skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses, saved JSON data files, and shell commands for API, authentication, billing, and onboarding workflows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a local linkfox session data directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
