## Description:

帮助电商营销团队将商品卖点转为分镜脚本，逐镜生成并拼接带字幕的短视频广告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商营销人员和内容创作者用它将商品卖点编排为多镜头广告，生成视频片段、拼接成片并添加字幕。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product images, and generated assets may be sent to the selected cloud provider or dLazy CLI.

Mitigation: Choose an explicit trusted provider and model; do not submit confidential assets or third-party assets without rights.

Risk: Generation may incur costs or produce inconsistent product depictions across shots.

Mitigation: Review the storyboard and run a dry-run first; use a consistent product reference and inspect the finished video.

Risk: Example brand demographics or ad claims may not fit the intended audience or product.

Mitigation: Customize example brand settings and check captions and claims before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Video backends and subtitles](artifact/references/video-backends.md)
- [Provider setup and data flow](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration guidance]

**Output Format:** [Storyboard text and JSON with generation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Execution can produce per-shot MP4 clips, an assembled video, SRT subtitles, and a concatenation list.]

## Skill Version(s):

1.0.21 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
