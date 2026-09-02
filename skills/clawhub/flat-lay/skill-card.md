## Description:

服装平铺图一键上身试穿。服装平铺图 + 姿势参考图 → 模特上身商拍图，款式、颜色、织法、版型保持不变。当用户说「平铺图转模特图」「衣服上身」「虚拟试穿」「AI 试衣」「让模特穿上」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce teams use this skill to turn garment flat-lay or on-body reference images into on-model product photography while preserving garment color, texture, print, and fit. It also guides agents through input checks, prompt construction, provider selection, dry-run cost checks, generation, and output quality review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled generator exposes media tasks beyond flat-lay try-on, including watermark removal and promotional video or testimonial generation.

Mitigation: Review the scripts before installation and restrict agent use to the documented flat-lay workflow unless the broader media tasks are explicitly approved.

Risk: Input images and prompts may be uploaded to the selected cloud provider for generation.

Mitigation: Avoid sensitive faces, confidential product imagery, or restricted customer assets unless the chosen provider is approved for that data.

Risk: On-model generation can be misused to imply unauthorized endorsement or commercial likeness use.

Mitigation: Use only authorized model and reference imagery, and follow the skill's stated boundary against fake commercial endorsements.

## Reference(s):

- [Skill page](https://clawhub.ai/dlazyai/skills/flat-lay)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash command examples; generation runs can save JPEG image files or return JSON status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The flat-lay workflow defaults to 1024x1536 JPEG output with high quality; cloud generation may upload input images to the selected provider.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
