## Description:

UGC 口播种草视频。商品 + 人设 → 口播脚本与成片，达人自拍质感。当用户说「口播视频」「种草视频」「达人风格」「UGC」「真人推荐」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Product marketers and content creators use the skill to turn a product and target persona into a spoken promotional script, storyboard, and UGC-style video variants. Generated promotional content should be disclosed and must not be presented as a genuine buyer testimonial.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: UGC-style promotional content could be mistaken for a real buyer's experience.

Mitigation: Clearly label AI-generated promotional content, do not present it as a genuine customer review, and check the target platform's disclosure rules.

Risk: Cloud video generation can incur provider costs and uses supplied images.

Mitigation: Choose the provider explicitly, review the images and expected costs, and run a dry run before generation.

Risk: Provider tooling may be obtained from untrusted sources.

Mitigation: Install provider tools only from sources you trust.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/ugc-testimonial)
- [Video backend configuration](artifact/references/video-backends.md)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Brand-kit reference for consistent subjects](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [Video, Text, JSON, Subtitle files]

**Output Format:** [Video clips or assembled MP4, spoken-script text, JSON storyboard, and optional SRT subtitles.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lip-sync is not supported; video assembly and subtitle capabilities depend on local FFmpeg support.]

## Skill Version(s):

1.0.22 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
