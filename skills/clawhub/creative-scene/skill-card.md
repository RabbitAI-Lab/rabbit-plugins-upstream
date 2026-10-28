## Description:

从零创意生图，也可定向改模特、姿势、搭配。一句描述（可选参考图）→ 图。当用户说「创意生图」「生成一张」「改个姿势」「换模板」「随便来张图」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to generate original images from text prompts or modify selected aspects of a supplied reference image, such as a model, pose, or outfit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are processed by the chosen external provider and may incur charges.

Mitigation: Set the provider explicitly, use --dry-run to check routing and inputs, share only images and brand references authorized for that provider, and protect API keys.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/creative-scene)
- [Provider and CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [Generated image files (for example, JPG), with Markdown guidance and command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts may include optional reference images; users can select image dimensions, provider, batch count, and a local output path.]

## Skill Version(s):

1.0.25 (source: frontmatter; server release 1.0.25)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
