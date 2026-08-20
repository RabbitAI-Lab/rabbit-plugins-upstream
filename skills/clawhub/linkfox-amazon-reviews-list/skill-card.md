## Description:

Fetches Amazon product reviews by ASIN across 15 marketplaces and helps agents summarize ratings, sentiment, complaints, praise, verified-purchase reviews, Vine reviews, and product-improvement opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce analysts use this skill to retrieve, filter, and summarize customer reviews for one ASIN at a time across supported Amazon marketplaces. It supports review lookup, negative-review and positive-review analysis, verified-purchase filtering, media-review filtering, competitor review research, and product-improvement research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review queries and onboarding data may be sent to LinkFox services.

Mitigation: Install and use the skill only when users accept LinkFox processing, and obtain clear consent before submitting feedback or onboarding information.

Risk: The skill can guide account, billing, and paid order flows when credits are insufficient.

Mitigation: Require explicit user confirmation before listing paid plans, creating orders, or presenting payment QR codes.

Risk: Endpoint environment variables can redirect requests away from the default LinkFox services.

Mitigation: Verify LinkFox endpoint environment variables before use and restrict untrusted environment overrides.

Risk: Full raw review responses are saved locally.

Mitigation: Store outputs in an appropriate workspace and review saved JSON files before sharing them.

## Reference(s):

- [Amazon Product Reviews API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-reviews-list)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with review excerpts, JSON API responses saved to files, and occasional shell commands for authentication or billing setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full raw responses are saved to a local LinkFox session data directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
