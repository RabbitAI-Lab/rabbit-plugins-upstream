## Description:

Helps ecommerce teams create and evaluate product main-image candidates from approved product photos, including white-background images, lifestyle scenes, color variants, and single-variable A/B tests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and creative teams use this skill to draft product-image generation commands and check candidates against product facts and marketplace rules before testing or publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts are sent to dLazy's cloud service.

Mitigation: Upload only approved assets; avoid confidential or regulated images unless your organization permits this workflow.

Risk: Generation consumes paid credits, especially across many product variants.

Mitigation: Run dry-run and cost checks before bulk SKU generation.

Risk: An API key is needed to access the hosted service.

Mitigation: Store or supply the key only in an approved manner and rotate it if exposed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image URLs]

**Output Format:** [Markdown guidance and CLI commands; generated image links in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are hosted by dLazy; review product accuracy and channel requirements before publication.]

## Skill Version(s):

1.0.23 (source: server-resolved ClawHub release; supplied SKILL.md frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
