## Description:

Generates UGC-style testimonial video scripts, storyboards, and finished clips from a product and persona, with a casual creator-selfie feel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, growth marketers, and ecommerce creative teams use this skill to draft short UGC testimonial scripts and storyboard product recommendation videos for ad testing. Users should review claims, avoid presenting generated scenes as real buyer testimony, and follow the target platform's AI-labeling rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Storyboard processing can write generated video files outside the chosen output folder when unsafe shot IDs are used.

Mitigation: Use trusted storyboards, keep outputs in a disposable project folder, and restrict shot IDs to simple letters, numbers, underscores, and hyphens.

Risk: Prompts and reference images are sent to the selected generation provider.

Mitigation: Avoid sensitive or unapproved product, model, customer, or campaign assets unless the selected provider is approved for that data.

Risk: UGC-style videos can mislead viewers if framed as real customer testimony.

Mitigation: Do not claim generated scenes are authentic buyer experiences, and apply platform-required AI-generated content labels before publishing.

Risk: The shared task catalog includes an unrelated remove-watermark task.

Mitigation: Do not use watermark-removal behavior unless the user has clear rights to the source material.

## Reference(s):

- [Provider CLI Reference](artifact/references/provider-cli.md)
- [Video Backend Configuration](artifact/references/video-backends.md)
- [brand-kit reference](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON storyboard examples; scripts can emit JSON status and saved media file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce MP4 clips, a stitched final video, SRT captions, concat files, and dry-run request summaries depending on runtime options.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
