## Description:

Helps sellers create and review ecommerce product-image candidates from approved product photos, including controlled A/B variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and marketing teams use this skill to prepare ecommerce main-image candidates for approved products, check product accuracy and platform rules, and compare variants that differ by one variable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts are sent to dLazy's hosted service.

Mitigation: Upload only approved images and prompts that you are permitted to share.

Risk: The service requires a dLazy API key that grants account access.

Mitigation: Protect the key and rotate or revoke it when access should be removed; use the pinned npx command to avoid a global CLI installation.

Risk: Generated images may misrepresent product details or violate a sales channel's image rules.

Mitigation: Compare each candidate against the approved product photos and current channel requirements before publication.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Images]

**Output Format:** [Markdown guidance and commands; generated image URLs returned in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides baseline, scene, color-SKU and single-variable A/B image candidates for human review.]

## Skill Version(s):

1.0.17 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
