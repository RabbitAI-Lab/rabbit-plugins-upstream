## Description:

MPSTATS-Ozon商品详情 batch-fetches full MPSTATS product cards for up to 100 Ozon Russia SKUs, including price, rating, reviews, stock, sales, revenue, listing date, images, and fulfillment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and marketplace analysts use this skill to retrieve per-SKU Ozon Russia product metrics through MPSTATS for price, stock, sales, revenue, fulfillment, and competitor listing checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes account login, API-key generation, billing plan listing, and paid order creation flows in addition to Ozon data retrieval.

Mitigation: Run onboarding or billing commands only when the user intends to register, log in, generate a LinkFox API key, or create a payment order.

Risk: The skill sends API keys and Ozon SKU lookup requests to LinkFox-controlled service endpoints.

Mitigation: Install and use the skill only when the operator trusts LinkFox, and configure a dedicated least-privilege API key through LINKFOX_AGENT_API_KEY or LINKFOXAGENT_API_KEY.

Risk: Full response data, cache files, metadata, and payment QR images may be written locally under LinkFox directories that can fall back outside the current project.

Mitigation: Run from the intended workspace, verify LinkFox-related environment variables and output paths before use, and review or delete local LinkFox data and cache files when they are no longer needed.

Risk: Ozon detail lookups consume LinkFox credits, and repeated or modified calls may create additional cost.

Mitigation: Confirm expected credit use before batch calls, rely on the documented local cache when appropriate, and avoid automatic retries with changed parameters unless the user approves more cost.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-mpstats-ozon-product-detail)
- [MPSTATS Ozon product detail API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, JSON, files, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses and saved JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are saved under LinkFox session directories; large responses print summaries unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
