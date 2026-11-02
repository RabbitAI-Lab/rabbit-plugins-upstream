## Description:

Creates short product advertisements by turning selling points into a storyboard, generating video clips, and assembling them with captions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and marketing teams use this skill to turn product benefits into 15–30 second, multi-shot promotional videos for advertising and social commerce. They can review the storyboard before generation and assemble clips with captions and optional brand styling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Storyboard text and reference images, including any added face image, are sent to the selected provider and generation may incur charges.

Mitigation: Get approval for the storyboard and images before generation, choose the provider and model explicitly, and review the provider’s data-handling terms and expected charges.

Risk: An untrusted or unpinned CLI and an unsuitable output location can add avoidable execution or file-management risk.

Mitigation: Use a trusted pinned CLI version and save generated files in a dedicated output folder.

## Reference(s):

- [Product Video Ad on ClawHub](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Video backend configuration](artifact/references/video-backends.md)
- [Provider CLI guide](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Configuration, Shell commands, Video files, Subtitle files]

**Output Format:** [Storyboard and prompts in text or JSON; generated video clips and assembled MP4; SRT subtitles and a concat manifest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically produces a 15–30 second multi-shot ad; optional brand styling; no voiceover, music, or precise music synchronization.]

## Skill Version(s):

1.0.22 (source: SKILL.md frontmatter; server release 1.0.22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
