## Description:

图像 helps agents generate images with Grok Imagine from user prompts, save the resulting file locally, and optionally send the image to Feishu.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content creators use this skill to automate image generation from prompts and hand off saved images to Feishu when that delivery step is intended.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can save generated image files and send them to Feishu without a clear confirmation boundary.

Mitigation: Require explicit user approval for the exact file path and recipient or channel before any send action.

Risk: The skill may be selected for generic automation tasks beyond image generation.

Mitigation: Use it only when the user is requesting image generation with Grok Imagine and an intended save or Feishu delivery workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/grok-image-generate)
- [Grok Imagine](https://grok.com/imagine)
- [SkillHub skill listing](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, files]

**Output Format:** [Markdown guidance with JavaScript and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow can result in a locally saved image file and an optional Feishu message send.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
