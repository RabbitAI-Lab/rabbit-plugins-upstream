## Description:

从零创意生图，也可定向改模特、姿势、搭配。一句描述（可选参考图）→ 图。当用户说「创意生图」「生成一张」「改个姿势」「换模板」「随便来张图」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can describe a scene to generate an image from scratch, or provide a reference image and a prompt to request a targeted change to a subject, pose, or outfit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be sent to external image providers; the security review also reports that some files or references were only partially analyzed.

Mitigation: Avoid sending sensitive prompts or images unless you are comfortable with the provider processing, and review the provider's data-handling information before use.

## Reference(s):

- [model-flags.md](references/model-flags.md)
- [provider-cli.md](references/provider-cli.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [detect-task skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/detect-task/skill.md)

## Skill Output:

**Output Type(s):** [Images, Text, Shell commands, Guidance]

**Output Format:** [Generated image files with Markdown prompt templates and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts may include optional reference images and image-generation settings such as aspect ratio, size, and batch count.]

## Skill Version(s):

1.0.31 (source: frontmatter; server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
