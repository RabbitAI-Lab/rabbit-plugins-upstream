## Description:

Enhances blurred apparel product images by reconstructing material texture from a matching high-resolution product reference while preserving the person, composition, background, color, and garment silhouette.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce image production teams use this skill to post-process on-model clothing photos whose fabric details are blurred, using a same-product reference image to restore credible texture and fold detail. Agents use it to produce prompts, commands, and configuration guidance for cloud image-editing providers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, model images, prompts, and generation parameters may be uploaded to dLazy or another selected cloud image provider.

Mitigation: Use the skill only when that upload is acceptable, choose the provider deliberately, and keep API keys in normal provider configuration or environment variables.

Risk: Shared brand templates can apply demographic or visual defaults across many product images.

Mitigation: Review optional brand templates before applying them to batches or shared catalog workflows.

Risk: A mismatched product reference can transfer the wrong fabric texture to the source image.

Mitigation: Confirm the source image and high-resolution reference show the same product before execution.

Risk: Image editing can alter non-target regions such as the face, background, garment color, or silhouette.

Mitigation: Use prompts that lock non-garment regions and compare the output against the source before accepting the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [gpt-image-2 model flags](artifact/references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [Material enhancement example source image](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/material-enhancement/source-image.jpg)
- [Material enhancement high-resolution product reference](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/material-enhancement/hires-product.jpg)
- [Material enhancement example output](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/material-enhancement/example-output.jpg)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, files]

**Output Format:** [Markdown instructions with bash examples, provider configuration guidance, and generated image files when commands are executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses two input images in a fixed order: source image first, high-resolution same-product material reference second.]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
