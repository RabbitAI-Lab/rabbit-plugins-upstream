## Description:

UGC 口播种草视频。商品 + 人设 → 口播脚本与成片，达人自拍质感。当用户说「口播视频」「种草视频」「达人风格」「UGC」「真人推荐」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and marketing teams use the skill to turn a product and audience persona into a spoken UGC-style script, storyboard, and promotional video. It is intended for clearly presented AI-generated demonstrations, not fabricated customer testimonials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images, including face references, are sent to the selected cloud provider for processing.

Mitigation: Use only images authorized for sharing and choose the provider explicitly before generation.

Risk: Generated output files can overwrite existing files.

Mitigation: Use a dedicated output folder and review a dry run before spending credits.

Risk: UGC-style generated scenes could be mistaken for real customer experiences.

Mitigation: Do not present generated scenes as genuine buyer testimonials; label AI-generated content as required by the target platform.

Risk: Separately installed external CLI tools may change or behave unexpectedly.

Mitigation: Review and pin external CLI installations separately.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Video backend reference](references/video-backends.md)
- [Brand kit skill reference](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Video files, Subtitle files, Shell commands, Configuration]

**Output Format:** [Chinese spoken scripts and storyboards, generated video files, optional SRT subtitles, and runnable shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation requires an explicitly selected model; lip synchronization is not provided.]

## Skill Version(s):

1.0.26 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
