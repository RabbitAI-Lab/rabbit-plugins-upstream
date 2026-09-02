## Description:

商品短视频广告。卖点 -> 分镜脚本 -> 分段生成 -> 拼接加字幕成片。当用户说「做条广告」「短视频」「投流素材」「分镜脚本」「带货视频」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and marketing teams use this skill to turn product selling points and reference images into short storyboarded product video ads with generated clips, captions, and local assembly outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Example brand settings may not match the user's campaign, audience, or compliance requirements.

Mitigation: Review and replace examples/brand.yaml before generation, including model description, brand tone, and platform compliance fields.

Risk: Prompts and reference images are sent to the configured generation provider.

Mitigation: Use only approved provider credentials and avoid sending sensitive, confidential, or unlicensed imagery.

Risk: Generated ad claims, prices, captions, or visuals may be inaccurate or unsuitable for publication.

Mitigation: Use dry-run first, review the storyboard with the user, and manually approve the final video before campaign use.

Risk: Local video assembly depends on ffmpeg capabilities, and subtitle burn-in may not be available in every installation.

Mitigation: Install ffmpeg where final assembly is required and rely on the generated SRT or soft subtitle fallback when libass support is unavailable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Provider CLI Reference](references/provider-cli.md)
- [Video Backend Configuration](references/video-backends.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [Related Skill: main-image-video](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/main-image-video/skill.md)
- [Related Skill: ugc-testimonial](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/ugc-testimonial/skill.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON storyboard examples and shell command blocks; runtime scripts produce MP4 clips, SRT captions, concat lists, and final MP4 files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run planning, provider selection, brand configuration, per-shot regeneration, ffmpeg concatenation, and subtitle fallback.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
