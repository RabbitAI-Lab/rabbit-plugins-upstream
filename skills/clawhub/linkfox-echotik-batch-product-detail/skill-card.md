## Description:

Fetches detailed TikTok Shop product analytics for known product IDs or TikTok Shop URLs, including multi-period sales, GMV, live-stream, video, influencer, pricing, rating, commission, and product-status metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and e-commerce analysts use this skill to compare known TikTok Shop products side by side using sales, GMV, pricing, rating, review, commission, live-stream, video, and influencer metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends TikTok product IDs or URLs and session metadata to LinkFox and stores full response files locally.

Mitigation: Use it only when sharing those product identifiers with LinkFox is acceptable, and review or delete saved linkfox response files when they contain sensitive business data.

Risk: The skill consumes paid credits and may guide users through phone or SMS login, API-key creation, and payment order flows.

Mitigation: Confirm cost expectations before repeated calls, treat API keys as secrets, and use official LinkFox endpoints for account and billing actions.

Risk: Configurable LINKFOX_* API URL variables can redirect requests away from official LinkFox services.

Mitigation: Avoid custom LINKFOX_* API URL variables unless the destination is fully trusted.

## Reference(s):

- [EchoTik batch product detail API reference](artifact/references/api.md)
- [LinkFox authentication and billing onboarding](artifact/references/onboarding.md)
- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-batch-product-detail)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, JSON API responses, saved JSON files, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can save full LinkFox API responses under a local linkfox session directory, print small JSON responses inline, and summarize larger responses.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
