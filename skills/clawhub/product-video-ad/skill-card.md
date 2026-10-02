## Description:

Creates short product video ads by turning selling points into a storyboard, generating individual shots, assembling them, and adding subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to plan and generate multi-shot product ads for social media, with assembled video and timed captions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and selected reference images are sent to the configured media provider.

Mitigation: Avoid sensitive local images and review the storyboard image paths and shot IDs before generation.

Risk: Generation may incur provider charges or expose a long-lived API key.

Mitigation: Use dry-run to check inputs before generating and keep provider keys scoped and revocable.

Risk: Independently generated shots may show inconsistent product details.

Mitigation: Use the same product reference across shots and review the assembled video before publication.

## Reference(s):

- [Product Video Ad on ClawHub](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Video backend configuration](artifact/references/video-backends.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, JSON storyboard, Shell commands, Video files, Subtitle files]

**Output Format:** [Markdown guidance and JSON storyboard; generated MP4 clips and assembled video, with SRT captions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional subtitles; video assembly requires ffmpeg, and generation requires a configured media provider.]

## Skill Version(s):

1.0.13 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
