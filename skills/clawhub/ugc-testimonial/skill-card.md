## Description:

Creates UGC-style product testimonial scripts, storyboards, and short videos with a handheld selfie aesthetic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and creators use this skill to draft product recommendation scripts, plan selfie-style shots, and generate short UGC-style promotional videos for review before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, reference faces, prompts, and captions are sent to the configured generation provider.

Mitigation: Use only assets you are comfortable sharing with that provider, and run a dry-run before generation.

Risk: Testimonial-style videos could be mistaken for genuine customer endorsements.

Mitigation: Do not impersonate real customers or present generated experiences as genuine reviews; check the target platform's AI-labeling rules before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/ugc-testimonial)
- [Provider configuration and data flow](artifact/references/provider-cli.md)
- [Video backends and subtitles](artifact/references/video-backends.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance, Video files, Subtitle files]

**Output Format:** [Markdown guidance, JSON storyboards, MP4 video, and SRT subtitles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation requires a configured provider; voiceover is added separately.]

## Skill Version(s):

1.0.15 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
