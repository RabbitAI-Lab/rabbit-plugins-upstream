## Description:

静态主图转主图视频。一张商品图 → 3–5 秒可上架的主图短视频。当用户说「主图视频」「图转视频」「让图动起来」「加个视频」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ecommerce operators use this skill to turn a single product hero image into a short 3-5 second listing video with controlled camera motion, material movement, and optional brand styling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to the selected cloud generation backend.

Mitigation: Confirm the selected backend and credential policy before use, and avoid sending confidential product assets to unapproved providers.

Risk: Video generation can consume paid credits or provider quota.

Mitigation: Use dry-run mode first and start with a short single-clip test before batch generation.

Risk: The sample brand configuration includes reusable model and visual defaults that may not fit a real storefront.

Mitigation: Edit brand.yaml before reuse, especially model description, demographic defaults, and platform-specific constraints.

Risk: Generated motion may distort product appearance or miss marketplace video requirements.

Mitigation: Review the source image first, use subtle motion prompts, and manually check the resulting video against platform rules before publishing.

## Reference(s):

- [Video Backend Configuration](references/video-backends.md)
- [Provider CLI Reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with CLI commands; generated outputs are MP4 video files and optional SRT captions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run previews before paid generation and requires an explicit video model for the selected backend.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
