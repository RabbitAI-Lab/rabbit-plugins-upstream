## Description:

去水印去文字。带水印 / 文字 / logo 的图 → 干净图，背景纹理自然补全。当用户说「去水印」「去文字」「擦掉 logo」「把字去了」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and image editing agents can remove watermarks, promotional text, badges, and decorative frames from images, then reconstruct the covered areas for use in an authorized image workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious because scanners report capabilities broader than the stated image-cleanup purpose; analysis is incomplete.

Mitigation: Review the requested task and generated commands before execution, and keep use within the intended image-cleanup workflow.

Risk: Images and prompts may be sent to external providers.

Mitigation: Check the selected provider and its data handling before sending images or prompts, especially if they contain sensitive material.

Risk: Removing overlays reconstructs obscured content and may alter nearby image details.

Mitigation: Use only images you are authorized to edit, preserve copyright and legally required markings, and inspect the generated image before relying on it.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Provider and CLI configuration](references/provider-cli.md)
- [Model command flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Prompt guidance]

**Output Format:** [Reconstructed image files (typically JPEG) with shell commands and prompt text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covered content is inferred by the image model; surrounding pixels or perspective may also change slightly.]

## Skill Version(s):

1.0.32 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
