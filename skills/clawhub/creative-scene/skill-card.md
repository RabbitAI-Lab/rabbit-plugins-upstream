## Description:

从零创意生图，也可定向改模特、姿势、搭配，一句描述或可选参考图即可生成图片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, commerce teams, and developers use this skill to create or modify commercial scene images from text prompts and optional reference images. It supports new scene generation plus targeted changes to model appearance, pose, outfits, and brand styling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be sent to the selected external image provider.

Mitigation: Use non-sensitive prompts and images, review the provider data flow, and avoid untrusted image URLs.

Risk: Generation can incur provider or dLazy credits.

Mitigation: Use --dry-run for preview and cost estimation before running paid generation.

Risk: Generated commercial images may be mistaken for real product photography or user experience evidence.

Mitigation: Review outputs before publication and do not use generated images to falsify product photos or usage claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/creative-scene)
- [Provider CLI reference](references/provider-cli.md)
- [banana-pro parameter reference](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands, optional JSON CLI envelopes, and saved image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call external image providers, save generated image files locally, and report estimated credits for dry runs.]

## Skill Version(s):

1.0.11 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
