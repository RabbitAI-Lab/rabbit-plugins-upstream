## Description:

Guides an agent to remove text, watermarks, logos, and promotional overlays from images while reconstructing covered areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and commerce teams use this skill to prepare clean images by removing permitted text, watermarks, and promotional graphics and reviewing reconstructed areas before reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Removing copyright watermarks, brand identifiers, certifications, or warnings could misrepresent ownership or product information.

Mitigation: Use only on images and marks you are authorized to edit; do not erase third-party copyright marks or required labels.

Risk: Selected images and prompts may be sent to external image-generation providers.

Mitigation: Confirm the selected provider and obtain permission before submitting private or sensitive images.

Risk: Model reconstruction may alter composition or invent covered product details.

Mitigation: Compare the output with the original and manually verify important product features before reuse.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Provider CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and edited image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reconstructed regions are inferred, and other image details may change; review results against the original.]

## Skill Version(s):

1.0.16 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
