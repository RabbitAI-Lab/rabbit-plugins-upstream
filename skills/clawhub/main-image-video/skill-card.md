## Description:

静态主图转主图视频。一张商品图生成 3-5 秒可上架的主图短视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce operators use this skill to turn a single product main image into a short product video with controlled camera motion, material movement, and optional brand styling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, prompts, and provider credentials may be sent to the configured generation backend.

Mitigation: Use dry-run first, confirm the selected provider and request details, and only use provider credentials intended for this workflow.

Risk: Video generation can incur provider costs and may use the wrong model if the environment is misconfigured.

Mitigation: Set an explicit video model before generation and review the dry-run cost and request preview before running paid jobs.

Risk: The bundled shared generator supports broader image-generation tasks beyond main-image video creation.

Mitigation: Limit use to product-image-to-video tasks and avoid unrelated transformations such as watermark removal unless rights to the assets are clear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Backend call reference](references/provider-cli.md)
- [Video backend configuration](references/video-backends.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, files]

**Output Format:** [Markdown guidance with bash commands and generated MP4 video file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run request previews, explicit video model selection, provider credentials, optional brand configuration, and local MP4 outputs.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
