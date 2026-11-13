## Description:

商品短视频广告。卖点 → 分镜脚本 → 分段生成 → 拼接加字幕成片。当用户说「做条广告」「短视频」「投流素材」「分镜脚本」「带货视频」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce marketers and content creators use the skill to turn product selling points into a storyboard, then generate and assemble a short multi-shot video ad with captions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be sent to external video services without clear disclosure.

Mitigation: Check the selected provider and its data flow, and remove sensitive details or images before generation.

Risk: Scanner coverage was partial, so some behavior remains unassessed.

Mitigation: Review provider settings and the relevant skill behavior before use, especially when handling sensitive material.

## Reference(s):

- [Provider CLI and data-flow reference](references/provider-cli.md)
- [Video backend configuration](references/video-backends.md)
- [Main Image Video skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/main-image-video/skill.md)
- [UGC Testimonial skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/ugc-testimonial/skill.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Video files, Subtitle files]

**Output Format:** [Storyboard guidance and shot-list JSON, plus generated MP4 clips, SRT captions, and assembly files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typical ads run 15–30 seconds; video generation requires a configured provider, and local assembly or subtitle rendering depends on ffmpeg support.]

## Skill Version(s):

1.0.29 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
