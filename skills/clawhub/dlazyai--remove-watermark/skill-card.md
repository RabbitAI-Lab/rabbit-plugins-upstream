## Description:

Helps remove text, watermarks, and promotional overlays from images by reconstructing the covered areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and commerce teams use this skill to prepare cleaner product imagery by removing unwanted text and decorative overlays, then reviewing the reconstructed image before reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private or sensitive source images may be sent to a cloud image provider.

Mitigation: Use only images you are comfortable sharing with the selected provider; avoid sensitive or private media.

Risk: Removing copyright, legal, safety, or ownership markings can misrepresent an image.

Mitigation: Use only images you are authorized to edit; preserve legally required and ownership markings.

Risk: The bundled tooling supports multiple providers and may run paid remote edits.

Mitigation: Select a provider explicitly and check a dry run before executing edits.

Risk: AI reconstruction can change obscured details or alter the composition.

Mitigation: Compare each edited result to its source and use a pixel-preserving editor when exact fidelity is required.

## Reference(s):

- [ClawHub remove-watermark release](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Provider CLI reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Edited image file and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reconstructed content may not preserve the original pixels or perspective; visually review results.]

## Skill Version(s):

1.0.17 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
