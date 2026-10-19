## Description:

Creates UGC-style product testimonial scripts, shot plans, and short videos with a casual selfie aesthetic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and creators use this skill to draft product-focused spoken scripts and storyboards, then generate short UGC-style video clips for advertising.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, reference images, prompts, and captions may be sent to a cloud generation provider.

Mitigation: Choose the provider deliberately, preview with dry-run, and avoid sending private or regulated images.

Risk: UGC-style testimonials can imply real personal experience or make unsupported product claims.

Mitigation: Substantiate claims, do not present generated scenes as genuine buyer reviews, and label AI-generated or dramatized material where required.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/ugc-testimonial)
- [Video backend configuration](references/video-backends.md)
- [Provider CLI reference](references/provider-cli.md)
- [Brand kit reference](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Video files]

**Output Format:** [Spoken script, JSON storyboard, MP4 clips and optional SRT subtitles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Assembled video and embedded subtitles require ffmpeg; voiceover is added separately.]

## Skill Version(s):

1.0.20 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
