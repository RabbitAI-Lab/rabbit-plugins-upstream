## Description:

UGC 口播种草视频。商品 + 人设 → 口播脚本与成片，达人自拍质感。当用户说「口播视频」「种草视频」「达人风格」「UGC」「真人推荐」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers and ecommerce operators use this skill to turn product details and buyer personas into UGC-style testimonial scripts, storyboards, and generated video assets for campaign testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected prompts, product images, model references, and storyboard assets may be sent to the configured AI provider.

Mitigation: Use dry-run first, choose the provider intentionally, and avoid sending assets that should not leave the selected provider boundary.

Risk: UGC-style assets can be mistaken for real buyer testimonials or undisclosed reviews.

Mitigation: Do not claim generated content is a real buyer experience, and apply platform-required AI content labels before publishing.

Risk: Untrusted image URLs or unsuitable example brand defaults can affect privacy, consent, or campaign compliance.

Mitigation: Use trusted local assets or vetted URLs, review storyboard image paths before execution, and edit brand/persona defaults for the actual campaign.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/ugc-testimonial)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Video backend configuration](artifact/references/video-backends.md)
- [brand-kit model reference guidance](https://github.com/dlazyai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)
- [dLazy CLI](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON storyboard examples and shell commands; scripts may save MP4 clips, SRT captions, concat files, and final video files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses configured AI provider credentials and optional ffmpeg for concatenation and subtitles; dry-run mode previews provider calls.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
