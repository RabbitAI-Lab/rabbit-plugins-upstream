## Description:

UGC 口播种草视频。商品 + 人设 → 口播脚本与成片，达人自拍质感。当用户说「口播视频」「种草视频」「达人风格」「UGC」「真人推荐」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and creators use this skill to turn a product and audience persona into a short UGC-style spoken script, storyboard, and promotional video. The generated scenes are demonstrations and should not be represented as genuine customer reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Identifiable faces or confidential images may be sent to the selected cloud provider for processing.

Mitigation: Use only images you have permission to process. Avoid confidential or identifiable images unless you have consent and have reviewed the selected provider's data handling.

Risk: The security scan reports 54.5% coverage and five partially inspected files, so some behavior remains unassessed.

Mitigation: Review the source files, especially those only partially inspected, before installing or running the skill.

Risk: Generated UGC scenes could be mistaken for genuine buyer testimonials if presented without context.

Mitigation: Label AI-generated content as required by the platform, avoid claiming a generated scene is a real customer's experience, and verify product claims before publication.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Video backend configuration](references/video-backends.md)
- [Brand kit model reference](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/ugc-testimonial)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Video, Shell commands, Configuration instructions]

**Output Format:** [Spoken scripts and prompts in text or Markdown, storyboards in JSON, generated video files, and optional SRT subtitles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Short clips can be combined into a finished video; subtitle files or concat instructions may be provided when local video tools are unavailable.]

## Skill Version(s):

1.0.29 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
