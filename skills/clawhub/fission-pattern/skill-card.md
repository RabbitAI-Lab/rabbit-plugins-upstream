## Description:

一张商品图裂变成整套素材。商品图 + 卖点 → 多角度多场景成套图，够铺满一屏。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers, creative operators, and agents use this skill to turn one product image plus selling points into a consistent set of product shots for listing images and detail pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to dLazy or another configured image provider.

Mitigation: Use the skill only when those provider data flows are acceptable for the product images and prompts being processed.

Risk: Brand configuration defaults may include demographic descriptors for generated people or models.

Mitigation: Review and customize brand.yaml before scaled use so model descriptors match the intended brand, consent, and compliance posture.

Risk: Generated image sets can drift from the original product or repeat unwanted text from the input image.

Mitigation: Use detailed product-fidelity prompts, remove source-image marketing text before generation, and inspect each image before publication.

## Reference(s):

- [Model Flags Reference](references/model-flags.md)
- [Provider CLI Reference](references/provider-cli.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/fission-pattern)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces prompt structure, provider invocation guidance, and ecommerce image-set outputs from a reference product image.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
