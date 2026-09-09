## Description:

从零创意生图，也可定向改模特、姿势、搭配；一句描述或可选参考图即可生成图片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce creative teams use this skill to create product-style scene images from short descriptions or reference images. It also helps draft prompts and shell commands for changing a model, pose, outfit, scene, framing, or mood.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images may be sent to cloud image providers.

Mitigation: Use the skill only when that data sharing is acceptable, and avoid sending sensitive or unconsented images.

Risk: The Ark provider can use an environment-configured endpoint for requests that include an API key and user images.

Mitigation: Leave ARK_BASE_URL unset unless it is a trusted HTTPS endpoint you control.

Risk: Identity-preserving edits can involve real people's photos.

Mitigation: Use real-person photos only with consent and authorization, and follow the skill boundary against generating specific real-person portraits.

## Reference(s):

- [Creative Scene skill page](https://clawhub.ai/dlazyai/skills/creative-scene)
- [Provider CLI reference](references/provider-cli.md)
- [banana-pro model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [Example output image](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/creative-scene/example-output.jpg)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline bash commands, plus generated image file paths or JSON envelopes when commands are executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use text prompts, optional reference images, aspect ratio, image size, batch count, provider selection, and save path.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
