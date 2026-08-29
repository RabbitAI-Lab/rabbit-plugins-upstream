## Description:

鞋包配饰真人穿戴图。商品图 + 模特参考图 → 真人佩戴图，落位、透视与阴影自然。当用户说「鞋包上脚」「配饰上身」「墨镜戴上」「首饰佩戴图」「包包上身」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, merchandisers, and creative operators use this skill to generate on-model accessory product photos from product images and model reference images while preserving product identity, placement, perspective, and the reference scene.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, model reference images, prompts, and brand files may be sent to the selected image provider during generation.

Mitigation: Use dry-run and provider selection before execution, and avoid uploading sensitive, private, or unauthorized images.

Risk: Generated on-model accessory imagery could be misused to imply endorsement or consent from a person shown in a reference image.

Mitigation: Use authorized reference images only and follow the skill's stated boundary against fake portrait endorsement.

Risk: Sample brand configuration may contain demographic defaults that are inappropriate for a specific campaign.

Mitigation: Edit brand.yaml for the intended audience and brand requirements instead of copying sample defaults unchanged.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/wear-everything)
- [model-flags.md](references/model-flags.md)
- [provider-cli.md](references/provider-cli.md)
- [dLazy CLI](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands, prompt templates, configuration notes, and generated image file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image files are typically saved as JPEG outputs when the referenced image-generation commands are executed.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
