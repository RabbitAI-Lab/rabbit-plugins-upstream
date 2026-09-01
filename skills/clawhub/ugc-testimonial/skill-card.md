## Description:

Creates UGC-style testimonial scripts, storyboards, and finished video clips from a product and buyer persona, while reminding users not to present generated content as real customer reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce marketers, operators, and developers use this skill to draft, storyboard, and generate UGC-style product testimonial ads for campaign iteration and A/B testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated UGC-style ads may be mistaken for real customer testimonials if presented without disclosure.

Mitigation: Label AI-generated content when required and do not claim generated scenes are real buyer reviews.

Risk: Prompts, product images, model reference images, and credentials may be sent to the selected cloud provider.

Mitigation: Use only provider credentials and input assets that are approved for the selected provider and campaign.

Risk: Long talking-head clips can have weak lip-sync, face consistency, or expression quality.

Mitigation: Use short talking-head shots, keep a consistent model reference, add subtitles or separate voiceover, and review outputs before publishing.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Video backend configuration](references/video-backends.md)
- [brand-kit skill reference](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/ugc-testimonial)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash commands, JSON storyboard examples, configuration snippets, and generated media file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce MP4 clips, a final stitched video, subtitle files, concat manifests, JSON status output, and dry-run cost/request summaries.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
