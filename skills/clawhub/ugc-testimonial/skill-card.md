## Description:

Creates a UGC-style product testimonial script, shot plan, and video with a casual selfie aesthetic from product and persona details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers and creators use this skill to draft persona-based product pitches and shot plans, then generate short UGC-style promotional clips for review before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product assets, and model or reference images may be sent to the selected generation provider.

Mitigation: Choose the provider deliberately, run the documented dry-run first, and obtain consent before uploading personal images or sensitive assets.

Risk: A testimonial-style ad could be mistaken for a real buyer review or undisclosed AI-generated endorsement.

Mitigation: Do not present generated personas as real buyers; review product claims and follow the target platform's AI-content disclosure rules before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/ugc-testimonial)
- [Provider CLI reference](references/provider-cli.md)
- [Video backend configuration](references/video-backends.md)
- [Brand kit reference](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [Text, JSON storyboard, Shell commands, Video files, Subtitle files]

**Output Format:** [Markdown guidance and script; JSON shot plan; generated MP4 clips and optional SRT subtitles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A video model must be selected; assembling clips and burning subtitles requires ffmpeg. Voiceover is added separately because lip-sync is unreliable.]

## Skill Version(s):

1.0.17 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
