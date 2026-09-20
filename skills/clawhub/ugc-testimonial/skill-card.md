## Description:

UGC 口播种草视频。商品 + 人设 → 口播脚本与成片，达人自拍质感。当用户说「口播视频」「种草视频」「达人风格」「UGC」「真人推荐」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce operators and creative agents use this skill to turn product details and buyer personas into UGC-style testimonial scripts, storyboards, and generated short-form video assets. It is intended for disclosed AI-generated demonstrations, not undisclosed fake customer reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product data, and reference images may be sent to the selected generation provider.

Mitigation: Choose the provider intentionally, review provider data handling requirements, and avoid submitting sensitive images or confidential product material unless approved.

Risk: Remote reference image URLs can expose data to third-party hosts or retrieve untrusted content.

Mitigation: Prefer trusted local assets and avoid untrusted remote image URLs.

Risk: UGC-style output could be mistaken for a real customer testimonial.

Mitigation: Disclose AI-generated content where required and do not present generated scenes as real buyer reviews or authentic customer experiences.

Risk: A generation run may incur provider cost or use an unintended model.

Mitigation: Run with --dry-run first, verify the selected provider and model, and set the video model explicitly before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/ugc-testimonial)
- [Provider CLI reference](references/provider-cli.md)
- [Video backend configuration](references/video-backends.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [Brand kit reference](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash and JSON examples; generated runs can produce MP4 video files, SRT subtitles, concat lists, and JSON status envelopes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run previews, explicit provider/model selection, storyboard inputs, optional brand configuration, and ffmpeg-based concatenation/subtitle post-processing.]

## Skill Version(s):

1.0.8 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
