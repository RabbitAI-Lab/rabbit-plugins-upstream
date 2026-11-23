## Description:

UGC 口播种草视频。商品 + 人设 → 口播脚本与成片，达人自拍质感。当用户说「口播视频」「种草视频」「达人风格」「UGC」「真人推荐」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and commerce teams use this skill to draft short product testimonial scripts, storyboards, and UGC-style promotional videos across different personas. Generated scenes should not be presented as genuine customer experiences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face-reference images may be sent to the selected generation provider.

Mitigation: Confirm which provider receives the images and obtain permission before sharing them.

Risk: Several components were only partly scanned, so their behavior is not fully established.

Mitigation: Review the required environment and network access, and pin unpinned dependencies before use.

Risk: UGC-style generated content could be mistaken for a genuine customer testimonial.

Mitigation: Do not present generated scenes as real buyer experiences, and disclose AI generation where the platform requires it.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Video backend reference](references/video-backends.md)
- [Brand kit reference](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/ugc-testimonial)

## Skill Output:

**Output Type(s):** [Text, Video files, JSON, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance and JSON storyboards; generated video files with optional SRT subtitles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses product prompts and optional face-reference images; storyboard shots can include captions and durations.]

## Skill Version(s):

1.0.32 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
