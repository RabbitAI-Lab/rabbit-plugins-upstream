## Description:

Creates e-commerce product-photo variants by changing the model, background, or both while preserving the garment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and creators use this skill to make product-photo variants for different models and scenes without intentionally changing the clothing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source photos, pose references, and model-face images are sent to third-party image providers.

Mitigation: Submit only images you have rights and consent to process, and review provider data-handling terms before upload.

Risk: Generated likenesses could imply an unconsented endorsement or mislead customers.

Mitigation: Avoid unconsented real-person likenesses and fake endorsements; review generated images before publication.

Risk: Audience variants based on age, ethnicity, or skin tone may raise advertising compliance concerns.

Mitigation: Check applicable local advertising rules before creating or publishing demographic variants.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/one-shot)
- [Provider and data-flow reference](references/provider-cli.md)
- [Image-model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and generated product images (JPEG, PNG, or WebP)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports multiple variants; inspect garment fidelity, hands, and lighting before use.]

## Skill Version(s):

1.0.13 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
