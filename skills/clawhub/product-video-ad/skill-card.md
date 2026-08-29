## Description:

Generates short product advertising videos by turning selling points into a storyboard, generating clips per shot, stitching them together, and adding subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, creators, and marketing developers use this skill to plan and generate 15-30 second product ad videos from product selling points, reference images, storyboard files, and brand constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and reference images may be sent to the selected generation provider.

Mitigation: Use --dry-run first, avoid sensitive or private image URLs, and confirm provider data handling before running paid generation.

Risk: The bundled shared backend includes an unrelated remove-watermark task.

Mitigation: Use the product-video-ad workflow only, and do not use remove-watermark unless you have clear rights to the source material.

Risk: Per-shot generation can produce inconsistent product appearance across clips.

Mitigation: Review the storyboard and brand file before generation, use the same product reference image across shots, and rerun only the affected clip when needed.

## Reference(s):

- [Backend Invocation Reference](references/provider-cli.md)
- [Video Backend Configuration](references/video-backends.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with JSON/YAML configuration examples and shell commands; scripts produce MP4, SRT, and concat-list files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run review before generation; final video assembly and subtitle handling depend on the local ffmpeg installation.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
