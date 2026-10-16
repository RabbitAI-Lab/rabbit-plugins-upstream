## Description:

Guides the conversion of flat-lay garment photos into dimensional ghost-mannequin product images while preserving garment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and product teams use this skill to turn flat-lay clothing photos into dimensional, mannequin-free product shots with controlled volume, drape, and detail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment images, prompts, and product details are sent to the configured cloud image provider.

Mitigation: Check the selected provider with --doctor or --dry-run and use only approved providers for sensitive product images.

Risk: Optional npx-based setup commands can fetch and run external packages.

Mitigation: Pin or review the package and version before running optional setup commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/to-3d)
- [Provider CLI reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with image-generation prompts and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executed commands can save generated garment images; inspect results for fidelity before publishing.]

## Skill Version(s):

1.0.22 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
