## Description:

商品短视频广告。卖点 → 分镜脚本 → 分段生成 → 拼接加字幕成片。当用户说「做条广告」「短视频」「投流素材」「分镜脚本」「带货视频」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use the skill to turn product selling points into a short, multi-shot video ad, with captions and a stitched video. It guides users through storyboard review and preview before generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious because it found external data transfers and gaps in analysis; prompts or images may be sent to video-generation services without a privacy warning.

Mitigation: Before use, verify what data is sent to external providers and whether sharing the prompts and images is acceptable. Treat the partial scan as a reason to review before installing, not as proof that the skill is safe.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Video backend reference](references/video-backends.md)
- [Related: Main Image Video skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/main-image-video/skill.md)
- [Related: UGC Testimonial skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/ugc-testimonial/skill.md)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/product-video-ad)

## Skill Output:

**Output Type(s):** [Guidance, JSON, Shell commands, Configuration instructions, Video files, Subtitle files]

**Output Format:** [Storyboard JSON, Markdown guidance, shell commands, SRT subtitles, and MP4 video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce segmented clips and a stitched 15–30 second ad; subtitles are optional.]

## Skill Version(s):

1.0.28 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
