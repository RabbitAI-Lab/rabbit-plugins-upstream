## Description:

商品短视频广告。卖点 → 分镜脚本 → 分段生成 → 拼接加字幕成片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External advertisers, e-commerce operators, and creative production teams use this skill to turn product selling points into storyboarded short-form video ads with generated clips, captions, and assembled output files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and reference images may be sent to the selected generation provider.

Mitigation: Use dry-run first, choose the provider intentionally, and avoid private or regulated data in prompts or images.

Risk: Generated advertising assets may inherit unsuitable sample brand, model, or demographic settings.

Mitigation: Replace the sample brand and model settings with lawful, product-appropriate advertising guidance before generation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Provider CLI Reference](references/provider-cli.md)
- [Video Backend Configuration](references/video-backends.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with JSON/YAML examples, shell commands, and generated video, subtitle, and manifest files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce per-shot MP4 clips, captions.srt, concat.txt, final.mp4, and final-sub.mp4 when run with configured generation providers and ffmpeg.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
