## Description:

Transforms plain product images into photorealistic lifestyle scenes while preserving the product and matching shadows, reflections, and lighting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and developers use this skill to generate product-background replacement prompts and commands for commercial product imagery. It supports text-described scenes and uploaded background references while emphasizing product fidelity and physically plausible placement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be uploaded to dLazy or whichever image-generation provider is configured.

Mitigation: Use the skill only with product images and prompts approved for the selected provider and authentication context.

Risk: A generated scene may imply product properties or use cases that the real product does not support.

Mitigation: Keep prompt constraints that preserve the product, avoid misleading environments, and review outputs before publication.

Risk: The bundled brand example contains placeholder model and brand defaults.

Mitigation: Replace example brand.yaml values before using the file for a real campaign.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy provider information](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-change-background)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save JPEG image outputs locally; provider JSON responses may include saved paths and hosted asset URLs.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
