## Description:

Helps users preview a garment style in a different fabric using a style image and fabric swatch while aiming to preserve the original cut and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Apparel designers and merchandising teams can compare how a garment might look in different fabrics before physical sampling, using garment and fabric reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment images, fabric swatches and prompts are sent to the selected cloud image provider.

Mitigation: Use only assets you may share, obtain required consent, and check the selected provider's account and data policies before submitting sensitive images or confidential designs.

Risk: An optional unpinned package-install fallback could retrieve a changed CLI release.

Mitigation: Prefer a pinned CLI/package version, and use the fallback only when you trust its source.

Risk: Generated images may misrepresent a fabric's real-world drape, feel or weight.

Mitigation: Treat results as visual previews and confirm material properties with physical samples.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider CLI and data flow reference](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and generated garment preview images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Previews illustrate visual fabric effects; they do not establish actual fabric feel or weight.]

## Skill Version(s):

1.0.20 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
