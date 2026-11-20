## Description:

商品短视频广告。卖点 → 分镜脚本 → 分段生成 → 拼接加字幕成片。当用户说「做条广告」「短视频」「投流素材」「分镜脚本」「带货视频」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and marketing teams use this skill to turn product selling points into a short, multi-shot video advertisement with captions. It guides storyboard creation, clip generation, and video assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be sent to an external video provider; the skill's reference-image workflow does not clearly disclose this transfer.

Mitigation: Choose the provider knowingly and avoid confidential or identifiable assets unless you accept that provider receiving them.

Risk: The security scan fully inspected only 6 of 11 components, so it cannot establish that the remaining content is safe.

Mitigation: Review the partially analyzed and uninspected components before installing or running the skill.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Video backend configuration](references/video-backends.md)
- [Provider CLI reference](references/provider-cli.md)
- [Related main-image-video skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/main-image-video/skill.md)
- [Related UGC testimonial skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/ugc-testimonial/skill.md)

## Skill Output:

**Output Type(s):** [JSON, Video files, Subtitle files, Shell commands, Guidance]

**Output Format:** [Storyboard JSON, MP4 video clips and assembled video, SRT subtitles, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically targets 15–30 second advertisements; voiceover and music are not produced by this skill.]

## Skill Version(s):

1.0.31 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
