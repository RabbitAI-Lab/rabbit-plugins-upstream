## Description:

Generates Amazon product-detail imagery, including a main image, secondary images, and A+ content, through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and creative teams use the skill to plan and generate Amazon listing images and A+ brand-content visuals from product information and reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected product images are processed by dLazy, and the API key is stored in local CLI configuration.

Mitigation: Send only content approved for cloud processing, protect or rotate the API key, and review generation costs.

Risk: Generated product imagery may not meet the seller's accuracy or marketplace requirements without review.

Mitigation: Review each proposed image for product accuracy and applicable Amazon requirements before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [CLI homepage listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Text, Markdown, Shell commands]

**Output Format:** [Generated product-image assets and image URLs, with Markdown planning/checklists and CLI commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A staged set of Amazon listing and A+ image assets, reviewed individually before continuing.]

## Skill Version(s):

1.3.34 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
