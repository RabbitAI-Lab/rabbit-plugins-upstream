## Description:

静态主图转主图视频。一张商品图 → 3–5 秒可上架的主图短视频。当用户说「主图视频」「图转视频」「让图动起来」「加个视频」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商内容创作者和开发者可用一张商品主图生成 3–5 秒的短视频，并通过提示词控制运镜与商品材质动态。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic backend selection can choose an image provider and return a still image with an MP4 filename.

Mitigation: Select the provider and video model explicitly, then inspect the dry-run output before submitting a paid request.

Risk: Images, prompts, and optional brand reference photos are sent to the selected cloud provider.

Mitigation: Use only assets approved for processing by that provider.

Risk: An external CLI may change between releases.

Mitigation: Review and pin the CLI version used for generation.

## Reference(s):

- [Video backend configuration](references/video-backends.md)
- [Provider and CLI reference](references/provider-cli.md)
- [dLazy CLI reference](https://github.com/dlazy-ai/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/main-image-video)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [MP4 video files with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically a 3–5 second clip generated from one product image; model and provider options vary.]

## Skill Version(s):

1.0.25 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
