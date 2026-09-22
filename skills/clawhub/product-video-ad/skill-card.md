## Description:

商品短视频广告。卖点 -> 分镜脚本 -> 分段生成 -> 拼接加字幕成片。当用户说「做条广告」「短视频」「投流素材」「分镜脚本」「带货视频」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing operators, ecommerce teams, and agents use this skill to turn product selling points into storyboarded short-form product video ads with generated clips, captions, and stitched final media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced product or model images may be sent to the selected external generation provider.

Mitigation: Use the skill only with data suitable for the chosen provider, select the provider explicitly when destination matters, and avoid supplying sensitive product or personal imagery unless approved.

Risk: Video generation may incur provider costs or use an unintended backend if configuration is implicit.

Mitigation: Run with --dry-run before generation and set --provider and model configuration explicitly for cost and routing control.

Risk: The example brand configuration may not match every campaign or product.

Mitigation: Review and customize examples/brand.yaml before reuse so default model, brand, and visual constraints match the intended advertisement.

## Reference(s):

- [Skill page](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Provider CLI reference](references/provider-cli.md)
- [Video backend configuration](references/video-backends.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON storyboard examples and shell commands; execution can produce MP4 clips, SRT captions, concat manifests, and final MP4 video files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run planning, explicit provider/model selection, optional brand configuration, and local ffmpeg stitching/subtitle workflows.]

## Skill Version(s):

1.0.9 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
