## Description:

Generates UGC-style product testimonial scripts, storyboards, and short videos from a product and presenter persona.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to draft persona-based product pitches and assemble short, selfie-style promotional videos with product shots and captions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to an external generation provider.

Mitigation: Use --dry-run first, avoid sensitive local files and internal URLs as image inputs, and select a provider whose data handling is acceptable.

Risk: Generation may incur charges or expose API credentials.

Mitigation: Preview calls with --dry-run and use scoped, revocable API keys.

Risk: A synthetic testimonial could be mistaken for a real customer endorsement.

Mitigation: Do not claim a real buyer's experience; disclose AI-generated content when the publishing platform requires it.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Video backend configuration](references/video-backends.md)
- [Brand-kit reference for consistent presenter identity](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Video files]

**Output Format:** [Spoken script and storyboard JSON, with generated MP4 clips and optional SRT subtitles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation requires a configured provider and model; final assembly and subtitle embedding require ffmpeg. Narration is added separately because lip-sync is not supported.]

## Skill Version(s):

1.0.12 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
