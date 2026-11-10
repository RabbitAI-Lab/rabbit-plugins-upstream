## Description:

商品短视频广告。卖点 → 分镜脚本 → 分段生成 → 拼接加字幕成片。当用户说「做条广告」「短视频」「投流素材」「分镜脚本」「带货视频」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce marketers and agents use this skill to turn product selling points into a short, multi-shot video ad, with a storyboard, generated clips, captions, and a stitched final video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan is incomplete, with five files only partially inspected, including scripts.

Mitigation: Consider the suspicious verdict and review the skill before installing or using it; the scan cannot establish that unreviewed content is safe.

Risk: Prompts and reference images may be sent to external video or image providers during generation.

Mitigation: Clarify the required network access and provider data handling before use, and avoid sending confidential or personal material unless you are comfortable with that processing.

## Reference(s):

- [Product Video Ad on ClawHub](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Provider CLI reference](references/provider-cli.md)
- [Video backend reference](references/video-backends.md)
- [Main Image Video skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/main-image-video/skill.md)
- [UGC Testimonial skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/ugc-testimonial/skill.md)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Shell commands, Files]

**Output Format:** [Markdown storyboards and guidance, JSON shot lists, SRT subtitles, shell commands, and generated MP4 clips or videos]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Storyboard prompts, shot durations, captions, and optional brand guidance; generated clips are combined into a finished video when the required tools are available.]

## Skill Version(s):

1.0.27 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
