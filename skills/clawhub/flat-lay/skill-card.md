## Description:

服装平铺图一键上身试穿。服装平铺图 + 姿势参考图 → 模特上身商拍图，款式、颜色、织法、版型保持不变。当用户说「平铺图转模特图」「衣服上身」「虚拟试穿」「AI 试衣」「让模特穿上」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, catalog teams, and content creators use this skill to turn flat-lay garment images and pose references into on-model product images while preserving garment style, color, material, and fit details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and uploaded images may be sent to a cloud generation provider.

Mitigation: Use only garment, model, and reference images that the user is allowed to upload and reuse.

Risk: The bundled helper configuration includes tasks outside the flat-lay try-on purpose, including watermark removal and video/UGC generation.

Mitigation: Restrict use to the documented flat-lay workflow unless a reviewer intentionally accepts the separate risks of other helper tasks.

Risk: Generated on-model imagery can imply identity, likeness, or endorsement.

Mitigation: Use authorized model/reference likenesses and avoid presenting generated images as commercial endorsement by real people without permission.

## Reference(s):

- [ClawHub Skill Release](https://clawhub.ai/dlazyai/skills/flat-lay)
- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Parameter Reference](references/model-flags.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands; generated outputs are image files and optional JSON result envelopes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run cost estimation, batch generation, provider selection, and saving generated ecommerce images to local paths.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
