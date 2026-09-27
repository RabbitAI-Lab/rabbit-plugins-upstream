## Description:

从零创意生图，也可定向改模特、姿势、搭配。一句描述（可选参考图）→ 图。当用户说「创意生图」「生成一张」「改个姿势」「换模板」「随便来张图」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce content teams use this skill to generate creative scene images from text prompts and optional reference images. It supports product and brand-style image ideation, plus targeted edits such as model, pose, and outfit changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and optional reference images may be sent to cloud image-generation providers.

Mitigation: Use only approved providers for private, regulated, or sensitive images and avoid uploading sensitive reference photos unless that provider is authorized for the data.

Risk: Generated product or lifestyle imagery can be mistaken for real photography or actual product use.

Mitigation: Review generated assets before publication and avoid using the skill to fabricate product evidence or misleading usage claims.

Risk: CLI setup may require provider credentials or local configuration.

Mitigation: Use pinned or trusted CLI installation commands and rotate or revoke provider keys according to the selected provider's credential policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/creative-scene)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [Provider CLI reference](references/provider-cli.md)
- [banana-pro model flags](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [Example output image](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/creative-scene/example-output.jpg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with prompt templates, command examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides cloud image-generation calls that can save generated image files through the selected provider CLI.]

## Skill Version(s):

1.0.13 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
