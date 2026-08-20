## Description:

Analyzes a provided product list and groups products by visual similarity of their main images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace sellers and agents use this skill after product search or recommendation to cluster visually similar product images, identify near-duplicates, and surface cross-brand lookalikes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product data and user instructions are sent to LinkFox for multimodal analysis.

Mitigation: Use only with product data approved for LinkFox processing, and avoid environments where LINKFOX endpoint variables can be set by untrusted parties.

Risk: Full analysis responses are persisted locally and may include product, image, and similarity result data.

Mitigation: Run the skill in an appropriate workspace and manage the generated linkfox output files according to the user's retention requirements.

Risk: The skill can guide account login, API-key generation, billing, order, and payment flows.

Mitigation: Provide phone numbers, SMS codes, plan choices, or payment methods only when intentionally completing LinkFox onboarding or billing actions.

Risk: Dynamic credit consumption may be large for product-image similarity analysis.

Mitigation: Warn the user about possible credit costs before execution and avoid automatic retries or parameter changes that would trigger extra paid calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-multimodal-product-similarity)
- [LinkFox publisher profile](https://clawhub.ai/user/linkfox-ai)
- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [JSON results persisted locally with concise text or Markdown summaries for larger responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an existing products array from a preceding tool, uses a configurable similarity threshold, and may guide LinkFox API-key or billing setup when authentication or balance errors occur.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
