## Description:

Lists the in-store products for a TikTok Shop seller by sellerId and returns product-level sales, GMV, price, rating, review, commission, listing, channel, and category metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Cross-border e-commerce sellers, marketers, and analysts use this skill to inspect a known TikTok Shop seller's current product catalog and compare product performance by sales, GMV, price, rating, reviews, commission, channel, and category.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill calls LinkFox/EchoTik services with an API key.

Mitigation: Obtain and manage API keys directly through the provider, scope them to the intended workflow, and avoid sharing saved outputs that may expose business analytics.

Risk: The bundled onboarding flow can support phone/SMS login and payment-order steps.

Mitigation: Confirm account recovery and any paid action with the user before creating orders or transmitting phone-based login details.

Risk: Full seller product results are persisted locally in the workspace.

Mitigation: Run the skill only in a workspace where saved seller analytics and cache files are acceptable, and remove local result files when they are no longer needed.

## Reference(s):

- [EchoTik Seller Product API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration]

**Output Format:** [Markdown summaries and tables, JSON API responses, saved JSON files, and shell commands for API access or account setup]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are saved under a local linkfox data directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
