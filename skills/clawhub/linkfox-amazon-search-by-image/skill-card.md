## Description:

Enables Amazon image-based product search across eight marketplaces to find visually similar listings from a public image URL, with optional Keepa-enriched product data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, sourcing teams, and product researchers use this skill to compare a supplied product image against visually similar Amazon listings across supported marketplaces. It returns product identifiers, images, pricing, ratings, reviews, brand details, and optional Keepa data for competitive analysis and sourcing decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images can be uploaded to a public URL before search.

Mitigation: Use only non-sensitive images and obtain explicit user approval before uploading a local file.

Risk: The skill can guide account setup, SMS login, API key creation, plan selection, and payment order creation.

Mitigation: Require explicit user approval before any login, account, billing, or payment action, and show returned order or payment details for review.

Risk: Amazon searches and Keepa enrichment consume LinkFox credits and may incur higher dynamic costs.

Mitigation: Disclose credit use before paid calls, avoid repeated automatic retries, and ask before expanding searches or enabling Keepa enrichment.

Risk: Full API responses are stored locally and may include product-search data, account context, or other task details.

Mitigation: Keep saved responses in the working session only when needed and remove or protect them if they contain sensitive business data.

Risk: Feedback content may be sent to a separate LinkFox endpoint.

Mitigation: Ask before submitting feedback and avoid sending private user or business information.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-search-by-image)
- [API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [LinkFox skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance, API calls]

**Output Format:** [Markdown tables and summaries, JSON response files, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a LinkFox API key and a publicly accessible image URL; local images may be uploaded to obtain a temporary public URL; full API responses are saved locally while large responses are summarized.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
