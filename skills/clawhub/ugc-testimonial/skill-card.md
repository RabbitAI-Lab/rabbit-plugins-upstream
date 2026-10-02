## Description:

Creates UGC-style product testimonial scripts and shot plans, with guidance for generating a selfie-style promotional video from a product and presenter persona.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce marketers and creators use this skill to draft short product pitches and shot-by-shot plans, then generate UGC-style promotional clips with subtitles and optional voiceover editing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product images, and face or reference images may be sent to a selected generation provider.

Mitigation: Use non-sensitive media, review inputs before submission, and run a dry-run first.

Risk: Testimonial-style content may be mistaken for a real customer's experience or omit required AI disclosures.

Mitigation: Do not present generated testimonials as genuine buyer reviews; check the target platform's AI-content and advertising rules before publication.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/ugc-testimonial)
- [Video backend configuration](artifact/references/video-backends.md)
- [Provider CLI reference](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown scripts and shot plans with storyboard JSON and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Configured generation providers can produce video clips and subtitle files; lip synchronization is not supported.]

## Skill Version(s):

1.0.13 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
