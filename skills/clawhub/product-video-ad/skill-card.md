## Description:

商品短视频广告。卖点 → 分镜脚本 → 分段生成 → 拼接加字幕成片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and marketing teams use this skill to turn product selling points into a multi-shot short-video ad, with a storyboard, generated clips, captions, and a stitched video. They can review the prompts and reference images before generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images, including face references in a brand file, may be sent to a cloud provider for generation.

Mitigation: Choose the provider explicitly and use only prompts and images approved for cloud processing.

Risk: Video generation may incur charges, and a storyboard preview may omit request details.

Mitigation: Review a detailed request with --dry-run before generation and confirm the selected provider and model.

Risk: Untrusted storyboard files or reused output directories can lead to unwanted inputs or overwrite prior output.

Mitigation: Use trusted storyboard files and a fresh output directory.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Video backend configuration](references/video-backends.md)
- [Main Image Video skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/main-image-video/skill.md)
- [UGC Testimonial skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/ugc-testimonial/skill.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/product-video-ad)

## Skill Output:

**Output Type(s):** [Text, JSON, SRT subtitles, Video files, Shell commands]

**Output Format:** [Storyboard guidance, JSON shot boards, SRT subtitles, shell commands, and MP4 video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shot durations, prompts, and captions are organized per shot. Voiceover and music are not produced; precise music timing requires post-editing. Video stitching and subtitle packaging depend on local ffmpeg availability.]

## Skill Version(s):

1.0.26 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
