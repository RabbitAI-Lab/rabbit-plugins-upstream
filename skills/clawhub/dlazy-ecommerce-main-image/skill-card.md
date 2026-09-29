## Description:

Guides agents in creating accurate ecommerce product-image candidates and single-variable A/B variants from approved product photos using dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and creative teams use this skill to prepare product-image candidates for listings and controlled A/B tests while checking product accuracy and channel rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos are uploaded to dLazy's hosted service.

Mitigation: Use only approved commercial images; do not upload sensitive unreleased product photos without permission.

Risk: The dLazy CLI uses an API key to access the service.

Mitigation: Rotate or revoke the key when access should be removed.

Risk: Generated images may misrepresent the product or fail channel requirements.

Mitigation: Check each candidate against the real SKU, supported claims, and current platform image rules before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown guidance with shell commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers white-background, visual-difference, lifestyle, color-SKU, and single-variable A/B image candidates.]

## Skill Version(s):

1.0.13 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
