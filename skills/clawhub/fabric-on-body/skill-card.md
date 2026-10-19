## Description:

Creates garment previews with a selected fabric while preserving the reference garment's cut and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion designers and product teams use a garment reference and fabric swatch to preview material variations before physical sampling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected garment and fabric images and prompts are sent to an external image provider.

Mitigation: Use an approved provider and avoid private, regulated, or internal-only files and URLs unless sharing is authorized.

Risk: Image-generation calls may incur provider charges.

Mitigation: Select the provider explicitly and use a dry run to check destination and estimated cost before generation.

## Reference(s):

- [Fabric on Body release](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Image model options](references/model-flags.md)
- [Provider setup and data flow](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Text guidance and commands with generated garment preview images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fabric texture, sheen, and drape may change; review previews for unintended changes to garment structure.]

## Skill Version(s):

1.0.23 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
