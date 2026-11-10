## Description:

Replaces the fabric shown in a garment reference image using a fabric swatch to create a visual preview while preserving the garment's cut and layout.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion designers and ecommerce teams can preview how a garment style may look in different fabrics before physical sampling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment and fabric images may be sent to an external image provider, which can expose unreleased designs or proprietary fabric details.

Mitigation: Use only approved images and confirm the selected provider's data handling is acceptable before sending them.

Risk: The image generator can be used for tasks beyond fabric replacement.

Mitigation: Keep the prompt and inputs scoped to the intended garment preview and review the generated result.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Image model flags](artifact/references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [Generated garment fabric preview images (JPEG, PNG, or WebP)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual previews only; they do not represent physical fabric hand, weight, or production samples.]

## Skill Version(s):

1.0.30 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
