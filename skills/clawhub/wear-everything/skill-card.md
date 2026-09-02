## Description:

Generates on-model commercial product images by placing shoes, bags, jewelry, eyewear, hats, scarves, and similar accessories from product photos onto a model reference image with natural placement, perspective, and shadows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, ecommerce operators, and creative production teams use this skill to turn accessory product images and model references into on-model product photography. It supports prompt construction, backend invocation, saved image outputs, and quality checks for placement, scale, reflections, and background preservation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product and model reference images may be uploaded to the selected image-generation provider.

Mitigation: Use only images the user has rights and consent to process, review the selected provider's data handling terms, and avoid sensitive or unauthorized likenesses.

Risk: API keys or local CLI authentication are required to run generation backends.

Mitigation: Store credentials in the documented local config or environment variables, restrict access to the machine or project, and rotate or revoke keys when no longer needed.

Risk: Generated accessory images can imply a person wore or endorsed a product.

Mitigation: Use consented model references and do not present generated outputs as real endorsements or documentary photos.

Risk: A fixed sample model demographic can create brand or fairness mismatches if reused without review.

Mitigation: Customize brand.yaml and model guidance for the intended brand, audience, and fairness requirements before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/wear-everything)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, image files]

**Output Format:** [Markdown guidance with inline bash commands, optional JSON execution status, and saved image assets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The default workflow uses gpt-image-2 with up to five reference images, configurable provider credentials, dry-run cost estimates, batch generation, and local file saving.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
