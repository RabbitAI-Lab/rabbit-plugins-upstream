## Description:

This LinkFox skill analyzes product images and brand parameters to produce a structured brandGeneJson visual identity profile for downstream image-generation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to extract a reusable visual brand profile from product images, brand colors, fonts, platform, language, and sales-region inputs. The resulting brandGeneJson is intended to keep downstream product-image generation visually consistent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product image URLs, brand parameters, and prompts are sent to LinkFox services.

Mitigation: Use only approved media and non-sensitive prompt content, and install the skill only when sending those inputs to LinkFox services is acceptable.

Risk: The bundled text-generation support skill can handle API keys, phone login, and payment ordering beyond brand-gene extraction.

Mitigation: Treat LINKFOX_AGENT_API_KEY as a secret and use phone login or payment-order flows only when account onboarding or billing actions are intended.

Risk: Configurable LINKFOX_* endpoint variables can redirect calls away from expected services.

Mitigation: Verify all LINKFOX_* endpoint environment variables point to trusted LinkFox domains before execution.

Risk: Generated brandGeneJson is stored in the session data directory for downstream reuse.

Mitigation: Review stored JSON for sensitive brand or product details and manage workspace/session data according to the user's retention requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-aigc-imagegen-brand-gene-extract)
- [AI 生文 API Reference](artifact/skills/linkfox-aigc-textgen/references/api.md)
- [Authentication and Billing Onboarding](artifact/skills/linkfox-aigc-textgen/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and structured JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a length-one brandGeneJson array and writes the assembled result to the session data directory for reuse by downstream image-generation skills.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
