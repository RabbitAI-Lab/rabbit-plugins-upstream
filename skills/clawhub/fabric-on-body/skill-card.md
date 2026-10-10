## Description:

Creates visual garment previews by applying a fabric swatch to a reference garment while preserving its cut and construction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion designers and product teams use garment reference images and fabric swatches to compare visual material options before physical sampling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and garment or fabric images may be sent to a selected cloud image-generation provider.

Mitigation: Check provider terms before submitting sensitive material, and use --dry-run to preview requests.

Risk: Optional external installation commands may fetch unpinned code.

Mitigation: Pin or verify the package and version before running network installs.

Risk: Generated previews may misrepresent real fabric drape, color, feel, or weight.

Mitigation: Check silhouette and material details against references and label results as visual previews rather than physical samples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider CLI reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Images, Guidance, Shell commands]

**Output Format:** [Garment preview image files (JPEG, PNG, or WebP) with Markdown guidance and optional JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual previews only; appearance does not establish real fabric feel or weight.]

## Skill Version(s):

1.0.19 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
