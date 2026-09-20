## Description:

Creates product short-video ad workflows from selling points through storyboard, per-shot video generation, stitching, and subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and commerce teams use this skill to plan and generate short product advertising videos with storyboards, shot clips, final stitched videos, and subtitles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product images, brand or model references, and generated outputs may be sent to a selected cloud provider and saved locally.

Mitigation: Use dry-run before paid or remote generation, choose the provider intentionally, and avoid submitting confidential or unauthorized assets.

Risk: API keys and cloud generation credits may be exposed or misused if credentials are shared broadly.

Mitigation: Use scoped and rotatable credentials, store them through the documented provider configuration, and rotate keys when access changes.

Risk: Generated advertising outputs may include assets, likenesses, or claims the user does not have rights to use.

Mitigation: Use only product images, brand references, video clips, and advertising claims the user has permission to use, and review outputs before publishing.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [Video Backend Configuration](references/video-backends.md)
- [main-image-video related skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/main-image-video/skill.md)
- [ugc-testimonial related skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/ugc-testimonial/skill.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON storyboard examples, YAML brand configuration, shell commands, SRT subtitles, and MP4 video outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces per-shot MP4 files, concat lists, captions.srt, final stitched videos, and optional subtitle-burned videos.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
