## Description:

服装平铺图一键上身试穿。服装平铺图 + 姿势参考图 -> 模特上身商拍图，款式、颜色、织法、版型保持不变。当用户说「平铺图转模特图」「衣服上身」「虚拟试穿」「AI 试衣」「让模特穿上」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams, marketers, and agents use this skill to turn garment flat-lay or product photos plus pose references into on-model catalog images while preserving garment details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment photos, model or reference photos, prompts, and generated outputs may be processed by dLazy or another configured cloud provider.

Mitigation: Use dry-run before paid execution, avoid sensitive personal images unless provider handling is acceptable, and keep provider credentials and PATH/DLAZY_BIN configuration under user control.

Risk: Generated try-on images may change garment color, texture, print placement, anatomy, or background details.

Mitigation: Use high-quality inputs and the documented prompt strategies, generate batches for selection, and review outputs for garment fidelity before commercial use.

Risk: Using a person's likeness as a reference can imply unauthorized endorsement or identity use.

Mitigation: Use authorized model/reference images and avoid outputs that suggest commercial endorsement by a real person without permission.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Model Flags](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands; generation scripts can return JSON and saved image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run request and cost previews; default generated images are JPEG files at 1024x1536 for the flat-lay task.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
