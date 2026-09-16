## Description:

从零创意生图，也可定向改模特、姿势、搭配；一句描述或可选参考图即可生成或修改图片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and commerce teams use this skill to draft prompts and commands for generating creative product or model scenes from text, or for targeted edits such as changing the model, pose, or outfit from a reference image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the Ark backend with a custom provider endpoint can send the Ark API key, prompts, and reference images to an environment-configured URL.

Mitigation: Use only trusted provider environment variables, avoid setting ARK_BASE_URL unless you control the destination, and run a dry run first to inspect the planned request.

Risk: Reference images and prompts may be sent to the selected cloud provider during generation.

Mitigation: Do not pass sensitive private images unless sharing them with the selected provider is acceptable.

## Reference(s):

- [Skill page](https://clawhub.ai/dlazyai/skills/creative-scene)
- [banana-pro parameter reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash command examples and generated image file paths or URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-only image generation, optional reference images, dry-run previews, provider selection, image size/aspect controls, and batch generation.]

## Skill Version(s):

1.0.9 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
