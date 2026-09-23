## Description:

Removes watermarks, text, logos, badges, and promotional frames from images and reconstructs the covered background texture.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to clean authorized product or source images by removing visible text, watermarks, logos, badges, borders, and promotional overlays before reusing the image or passing it to other image-generation skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and images may be sent to the selected cloud provider.

Mitigation: Install and run only when comfortable sharing the input images and prompts with that provider.

Risk: The skill can be misused to remove copyright watermarks, brand identifiers, warnings, certifications, or other legal labels from third-party content.

Mitigation: Use it only for images you own or are authorized to edit, and do not remove legal, safety, certification, copyright, or brand-identifying labels from third-party material.

Risk: Removed regions are reconstructed by the model rather than restored pixel-for-pixel, so product details, perspective, or texture may be inaccurate.

Mitigation: Review each edited image before use, especially where text or logos covered important product details; use professional image-editing tools when pixel-level preservation is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are image edits reconstructed by a cloud image model; exact covered pixels are inferred and should be reviewed.]

## Skill Version(s):

1.0.12 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
