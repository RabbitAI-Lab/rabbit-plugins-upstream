## Description:

UGC 口播种草视频。商品 + 人设 → 口播脚本与成片，达人自拍质感。当用户说「口播视频」「种草视频」「达人风格」「UGC」「真人推荐」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and ecommerce teams use this skill to draft UGC-style testimonial scripts, storyboard short product videos, and generate video clips with captions for commercial product promotion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images may be sent to the configured generation provider and may incur provider billing.

Mitigation: Run the documented dry-run mode first, verify the selected provider and estimated cost, and confirm that the referenced media is appropriate to send to that provider.

Risk: UGC-style video can mislead viewers if presented as a real buyer testimonial.

Mitigation: Use the skill's disclosure guidance: do not claim generated scenes are real customer experiences, avoid fake review artifacts, and follow the target platform's AI-generated-content labeling rules.

Risk: Video model behavior may produce weak lip sync, inconsistent faces, or stiff expressions.

Mitigation: Use short talking-head clips, lock the face through the brand reference workflow, prefer voiceover instead of synchronized speech, and review outputs before publication.

Risk: Generated commands may require credentials, local files, ffmpeg, and third-party provider tools to be present.

Mitigation: Review commands before execution, use documented authentication flows, install ffmpeg only when needed for assembly or subtitles, and keep API keys in the supported local configuration or environment variables.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/ugc-testimonial)
- [Backend provider CLI reference](references/provider-cli.md)
- [Video backend configuration](references/video-backends.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON storyboards, shell commands, and generated video, subtitle, and configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run review, configurable model providers, local output files, storyboard clips, final MP4 assembly, and SRT subtitles.]

## Skill Version(s):

1.0.10 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
