## Description:

Enhances blurred garment material in product images by using a high-resolution product reference to rebuild believable texture while preserving composition, person, background, color, and silhouette.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams, designers, and agent operators use this skill to post-process garment images by applying real fabric detail from a matching high-resolution product photo while preserving the original pose, background, silhouette, and color.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to cloud generation providers.

Mitigation: Use the skill only for images and prompts that are acceptable to share with the selected provider, and review the provider's data handling requirements before use.

Risk: The helper workflow can fetch image inputs from arbitrary URLs, which can expose internal or untrusted network locations if misused.

Mitigation: Use trusted local image files or trusted public image URLs, and avoid private-network, internal, or user-supplied URLs that have not been reviewed.

Risk: Provider credentials and custom endpoint settings can route requests to unintended destinations.

Mitigation: Use narrowly scoped, rotatable API keys and avoid untrusted ARK_BASE_URL values or other unreviewed provider endpoint overrides.

Risk: The generated image may change non-target details or apply the wrong texture if the reference image does not match the product.

Mitigation: Use a high-resolution reference image for the same product, lock non-target regions in the prompt, and compare output against the source before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands; generated image outputs are saved as JPEG files when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an original product image plus a matching high-resolution product reference; the documented workflow uses high quality image generation and may run batch variants for selection.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
