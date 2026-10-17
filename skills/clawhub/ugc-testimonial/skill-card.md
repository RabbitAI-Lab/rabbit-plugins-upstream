## Description:

Creates UGC-style product testimonial scripts, storyboards, and short videos from product details and a presenter persona.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to draft presenter-style product pitches and assemble short UGC-style promotional videos from a storyboard and reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images, including faces or product assets, may be sent to a selected cloud provider.

Mitigation: Use --dry-run first, explicitly select the provider for sensitive work, and obtain permission before sending reference images.

Risk: Synthetic presenter videos can be mistaken for genuine buyer testimonials.

Mitigation: Disclose AI generation as required by the distribution platform; do not claim a generated presenter is a real customer or fabricate reviews.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/ugc-testimonial)
- [Video backend configuration](references/video-backends.md)
- [Provider CLI reference](references/provider-cli.md)
- [Brand-kit reference](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Video files, Subtitle files]

**Output Format:** [Presenter script and storyboard guidance in text or Markdown; MP4 clips and optional SRT subtitles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can combine clips into a final video; voiceover requires separate editing, and lip sync is not provided.]

## Skill Version(s):

1.0.19 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
