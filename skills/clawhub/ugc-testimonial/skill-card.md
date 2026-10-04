## Description:

Creates persona-led product testimonial scripts, storyboards, and UGC-style short videos with a casual selfie aesthetic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers and creators use product details and a target persona to draft testimonial-style scripts and storyboards, then generate short promotional videos for review and editing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied product or model images are sent to the selected generation provider.

Mitigation: Confirm the provider and obtain approval before sending sensitive images or prompts.

Risk: Video generation can incur provider charges.

Mitigation: Review the script and use a dry run before paid generation.

Risk: Synthetic testimonials can be mistaken for genuine customer experiences.

Mitigation: Do not attribute the video to real buyers; disclose AI generation as required by the publishing platform.

## Reference(s):

- [Generation provider guidance](references/provider-cli.md)
- [Video backend and subtitle guidance](references/video-backends.md)
- [Brand-kit model reference guidance](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [Text, Storyboards, Video files, Subtitle files]

**Output Format:** [Markdown scripts and storyboard JSON; generated MP4 clips with optional SRT subtitles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A voiceover must be added separately; generated faces and lip sync may be imperfect.]

## Skill Version(s):

1.0.14 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
