## Description:

Creates UGC-style product testimonial scripts, shot plans, and short videos from product details and a presenter persona.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers and creators use this skill to draft persona-based product scripts and storyboards and produce UGC-style promotional videos with optional subtitles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, presenter references, prompts, and generated outputs may be handled by the selected media provider.

Mitigation: Use --dry-run first, avoid sensitive or private images, choose the provider and model deliberately, and keep API keys out of prompts and files.

Risk: UGC-style videos may be mistaken for genuine buyer testimonials.

Mitigation: Do not present generated personas or scenarios as real customer reviews; follow the target platform's AI-content disclosure rules.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/ugc-testimonial)
- [Video backend configuration](references/video-backends.md)
- [Provider CLI guide](references/provider-cli.md)
- [Brand-kit reference](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [Text, Storyboard configuration, Video files, Subtitle files]

**Output Format:** [Markdown, JSON, MP4, and SRT]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation requires an explicitly chosen model; subtitles may be embedded or supplied separately.]

## Skill Version(s):

1.0.16 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
