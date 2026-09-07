## Description:

UGC 口播种草视频。商品 + 人设 → 口播脚本与成片，达人自拍质感。当用户说「口播视频」「种草视频」「达人风格」「UGC」「真人推荐」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and commerce teams use this skill to draft UGC-style testimonial scripts, storyboard product shots, and run video generation workflows for promotional material. It is intended for AI-generated demonstration-style content, not undisclosed fake customer reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Custom Ark endpoints can receive credentials or generation payloads if ARK_BASE_URL is set to an untrusted service.

Mitigation: Do not set ARK_BASE_URL unless the endpoint is fully trusted; prefer the documented default provider settings and dry-run mode before execution.

Risk: Crafted storyboard shot IDs may cause generated files to be written outside the intended output folder.

Mitigation: Keep storyboard shot IDs simple and review untrusted storyboard JSON before running video generation.

Risk: UGC-style promotional content can mislead viewers if presented as a real buyer's testimonial.

Mitigation: Do not claim generated content is a real customer review; apply platform-required AI-generated content labels before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/ugc-testimonial)
- [Provider CLI reference](references/provider-cli.md)
- [Video backend configuration](references/video-backends.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [Brand kit reference](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON storyboard examples and bash commands; runtime scripts can emit JSON status and media file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce generated video clips, merged MP4 files, SRT subtitles, concat manifests, and saved output paths when scripts are executed.]

## Skill Version(s):

1.0.4 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
