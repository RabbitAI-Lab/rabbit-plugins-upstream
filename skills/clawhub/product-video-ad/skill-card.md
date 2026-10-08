## Description:

Turns product selling points into a shot-by-shot ad storyboard, generates clips, and assembles a subtitled product video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers and creators use this skill to turn product benefits and reference images into short, multi-shot video ads with captions for promotional campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, captions, and brand settings may be sent to the selected generation provider.

Mitigation: Use a provider whose data handling you accept and run a dry-run before generation.

Risk: Unauthorized product assets or unchanged example brand and model details could appear in an ad.

Mitigation: Use only assets you are authorized to use and customize the example brand and model fields before reuse.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Video backend configuration](artifact/references/video-backends.md)
- [Provider CLI reference](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Video files, Subtitle files]

**Output Format:** [Storyboard text and JSON shot list; MP4 clips and assembled video; SRT captions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional subtitled MP4 and concat list; clip generation requires a configured video provider, and assembly requires ffmpeg.]

## Skill Version(s):

1.0.15 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
