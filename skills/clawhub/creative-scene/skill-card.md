## Description:

从零创意生图，也可定向改模特、姿势、搭配。一句描述（可选参考图）生成图片，适用于创意生图、姿势调整、模板替换和搭配修改请求。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, ecommerce teams, and developers use this skill to turn scene descriptions into generated images or to edit a reference image by changing the model, pose, or outfit while preserving the rest of the composition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and optional reference images may be sent to dLazy or another configured image-generation provider.

Mitigation: Use the skill only with content that is appropriate to share with the selected provider, and avoid submitting sensitive images or confidential prompt content.

Risk: Broad image-generation requests, larger image sizes, or batch runs can create unexpected provider costs.

Mitigation: Use dry-run and lower-cost exploration settings before final generation, then increase image size or batch only when needed.

Risk: Model, skin, body, pose, or outfit editing templates can be misused on real people or to misrepresent identity.

Mitigation: Use these templates only with consent and avoid creating deceptive, non-consensual, or identity-misrepresenting imagery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/creative-scene)
- [Provider CLI reference](references/provider-cli.md)
- [banana-pro model flags](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with prompt templates, shell commands, and saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May send prompts and optional reference images to the configured image-generation provider and save returned images locally.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
