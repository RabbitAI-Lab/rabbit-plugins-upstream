## Description:

Guides agents to create visual garment previews that retain a reference garment's silhouette while replacing its fabric appearance using a fabric swatch.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion designers and e-commerce teams use this skill to preview how a garment style might look in alternative fabrics before selecting materials or preparing product imagery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment images, fabric swatches, and prompts are sent to the selected image provider.

Mitigation: Choose an approved provider and avoid confidential materials unless that provider is authorized to receive them.

Risk: Image-generation requests can incur charges and produce inaccurate fabric or garment details.

Mitigation: Use dry-run to review the request and estimated cost, then inspect generated previews against the original garment and swatch before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Image model options](artifact/references/model-flags.md)
- [Provider and data-flow guide](artifact/references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image previews require visual review and do not establish real fabric feel or weight.]

## Skill Version(s):

1.0.22 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
