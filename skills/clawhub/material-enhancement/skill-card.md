## Description:

材质质感增强与纹理重建。糊掉的图 + 高清商品图 -> 纹理清晰可信的图。当用户说「增强质感」「图糊了」「补纹理」「提清晰度」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and agents use this skill to improve blurred clothing material texture in product or on-model images while preserving composition, model appearance, background, silhouette, and color.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product or model images and prompts are sent to the configured cloud image-generation provider.

Mitigation: Use only providers acceptable for the image data, avoid private images unless approved for that provider, and review provider configuration before execution.

Risk: Paid image generation may incur provider credits or costs.

Mitigation: Use dry-run or doctor modes to confirm the selected provider and estimated cost before running generation.

Risk: Texture enhancement can unintentionally alter non-target image areas or shift garment color.

Mitigation: Use prompts that restrict changes to the garment material surface and compare the output against the source image before accepting it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with shell command examples and generated image file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses source and high-resolution product images as inputs, supports dry-run cost checks, and saves generated image outputs locally when executed.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
