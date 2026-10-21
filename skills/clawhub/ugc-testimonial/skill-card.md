## Description:

Creates UGC-style product testimonial scripts and storyboarded videos from product details and a chosen persona.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers and creators use this skill to draft persona-specific product pitches and generate short, UGC-style promotional clips with shot lists and subtitles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied reference images are sent to the selected external generation provider.

Mitigation: Review inputs and provider data handling before submitting private or sensitive material.

Risk: AI-generated testimonials could be mistaken for genuine customer experiences.

Mitigation: Present clips as dramatizations, never as real buyer reviews, and follow the target platform's AI-labeling rules.

Risk: Generation may incur charges or use footage without appropriate rights.

Mitigation: Run --dry-run first and only supply media you own or are licensed to edit.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Video backend configuration](references/video-backends.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Video files, Subtitles]

**Output Format:** [Conversational scripts and shot-list JSON; generated MP4 clips and SRT subtitles when run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a configured video provider and model; voiceover is added separately because lip sync is unreliable.]

## Skill Version(s):

1.0.21 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
