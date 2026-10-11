## Description:

Guides removal of watermarks, text, logos, and promotional overlays from images by reconstructing covered areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and e-commerce teams use this skill to prepare cleaner images they are authorized to edit for downstream design workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images and prompts are sent to the configured cloud provider.

Mitigation: Use only providers you trust with the supplied images and prompts.

Risk: Removing watermarks or labels can misuse others' images or obscure important information.

Mitigation: Edit only images you have rights to change; retain required labels and disclosures.

Risk: Reconstructed areas can contain inaccuracies, and image generation can consume credits.

Mitigation: Inspect edited areas manually and use --dry-run to review the provider, model, and request before incurring costs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Image model flags](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and edited image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reconstructed image areas are inferred rather than pixel-faithful.]

## Skill Version(s):

1.0.19 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
