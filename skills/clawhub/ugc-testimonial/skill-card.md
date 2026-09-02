## Description:

Generates UGC-style testimonial scripts, storyboards, and short product-video outputs from product details and audience personas, with a casual creator-selfie look.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and ecommerce operators use this skill to draft persona-led testimonial scripts, create shot plans, and generate UGC-style product videos for campaign testing. The skill is also useful for preparing variants for A/B tests while avoiding claims that AI output is a real buyer review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images may be sent to the configured media-generation provider.

Mitigation: Use --dry-run first, keep API keys scoped and revocable, and avoid private images or sensitive brand material unless the configured provider is acceptable for the use case.

Risk: UGC-style generated content can mislead viewers if presented as a real buyer's authentic experience.

Mitigation: Do not claim generated output is a real customer review; apply AI-generated content disclosures required by the target platform.

Risk: Video output depends on an explicitly configured model and local media tooling for stitching or subtitles.

Mitigation: Set an available video model before generation, run a dry run, and verify ffmpeg support when merged video or subtitle output is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/ugc-testimonial)
- [Provider CLI reference](references/provider-cli.md)
- [Video backend configuration](references/video-backends.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [Brand kit reference](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON storyboard examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may produce video clips, a final MP4, subtitle files, and concat files when executed with a configured media-generation provider.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
