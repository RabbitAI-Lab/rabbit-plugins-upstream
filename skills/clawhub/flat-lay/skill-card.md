## Description:

服装平铺图一键上身试穿。服装平铺图 + 姿势参考图 -> 模特上身商拍图，款式、颜色、织法、版型保持不变。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketers, and developers use this skill to turn garment flat-lay or existing apparel photos plus pose references into on-model catalog images while preserving garment color, texture, fit, and details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment, model, and reference images may be sent to the configured cloud provider.

Mitigation: Use only images and likenesses you own or are authorized to process, and install only when that provider data flow is acceptable.

Risk: Custom provider endpoints and provider-returned result URLs create network-handling exposure.

Mitigation: Use trusted provider endpoints, do not set ARK_BASE_URL unless the endpoint is fully trusted, and avoid privileged server or CI environments.

Risk: The bundled task catalog includes an unrelated remove-watermark task.

Mitigation: Use this release only for virtual apparel try-on workflows and avoid invoking unrelated watermark-removal behavior.

## Reference(s):

- [Provider CLI Reference](artifact/references/provider-cli.md)
- [gpt-image-2 Model Flags](artifact/references/model-flags.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/flat-lay)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with inline shell commands and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides image generation through dLazy or configured cloud providers; typical outputs are saved JPEG ecommerce product images.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
