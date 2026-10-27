## Description:

鞋包配饰真人穿戴图。商品图 + 模特参考图 → 真人佩戴图，落位、透视与阴影自然。当用户说「鞋包上脚」「配饰上身」「墨镜戴上」「首饰佩戴图」「包包上身」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers and product-content teams use this skill to create on-model product images by combining accessory photos with authorized model or scene reference photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded product or reference photos may contain identifiable people or confidential information.

Mitigation: Upload only photos you are authorized to share, and review the selected provider’s handling of confidential or identifiable images.

Risk: Provider selection and image-generation requests may route to an unintended service or incur unexpected costs.

Mitigation: Choose the intended provider explicitly and run --dry-run to review routing and estimated costs before generation.

Risk: Stored API credentials or existing output files may be exposed or overwritten.

Mitigation: Protect stored API keys and choose a fresh output filename to avoid overwriting files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/wear-everything)
- [Provider CLI guidance](artifact/references/provider-cli.md)
- [Model flags reference](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Image files]

**Output Format:** [JPEG images by default; provider-supported image formats can be selected.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Photorealistic accessory try-on images; output size, quality, and batch count are configurable.]

## Skill Version(s):

1.0.25 (source: SKILL.md frontmatter; server release 1.0.25)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
