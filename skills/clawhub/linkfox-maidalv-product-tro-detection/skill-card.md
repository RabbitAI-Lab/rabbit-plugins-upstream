## Description:

Checks product images and optional product context for TRO and trademark, patent, or copyright infringement risk, then returns risk levels, matching IP items, TRO plaintiff details, numeric scores, and an AI-generated legal assessment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers, compliance reviewers, and agent users use this skill to evaluate product images and listing context for TRO and IP infringement risk before listing or sourcing products. It is intended for one-shot risk screening and does not replace legal review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, descriptions, and generated legal-risk reports may contain sensitive business or legal data.

Mitigation: Confirm with the user before uploading local or proprietary images, and review the saved response files before sharing or retaining them.

Risk: The skill includes account onboarding, API-key setup, and payment ordering flows.

Mitigation: Prefer the official LinkFox site for signup and payment, require explicit user confirmation before billing actions, and avoid storing API keys in shell profiles on shared machines.

Risk: Full API responses are persistently logged, and the skill can report feedback to an external API.

Mitigation: Review or disable logging and feedback reporting when the workspace may contain sensitive commercial, legal, or product data.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-maidalv-product-tro-detection)
- [API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with JSON API responses and saved JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a main product image URL or Base64 data URI, may consume paid credits, caches identical calls for 24 hours, and writes full API responses to a local linkfox workspace directory.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
