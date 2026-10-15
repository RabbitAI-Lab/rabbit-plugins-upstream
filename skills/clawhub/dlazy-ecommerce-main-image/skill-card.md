## Description:

Creates e-commerce main-image candidates from approved product photos, including white-background, lifestyle, color-variant, and single-variable A/B options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use this skill to plan and generate product main-image candidates for marketplace listings and controlled A/B tests, while checking product accuracy and platform requirements before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts are sent to dLazy's hosted service.

Mitigation: Use only commercial product images approved for upload and share prompts appropriate for the service.

Risk: Authentication may save an API key locally.

Mitigation: Protect local credentials and revoke or rotate the key with dLazy if needed.

Risk: Generated images can alter product details or imply unsupported claims.

Mitigation: Compare each candidate with the approved SKU photos and verify platform requirements before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown guidance and command examples; image-generation results are returned as image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses approved reference images and recommends checking generated candidates against the actual SKU and target platform rules.]

## Skill Version(s):

1.0.20 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
