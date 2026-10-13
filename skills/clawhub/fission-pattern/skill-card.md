## Description:

Turns one product photo and its selling points into a coordinated set of e-commerce images with varied angles, scenes, and compositions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and merchants use the skill to plan and generate a consistent product-photo set for listings or detail pages from a single reference image and product selling points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, prompts, and optional brand references are sent to the chosen cloud image provider.

Mitigation: Confirm that the material can be shared with the selected provider before generation, and configure provider credentials deliberately.

Risk: Generating multiple images can incur provider charges.

Mitigation: Use dry-run or doctor mode to check the selected provider and estimated cost before paid generation.

Risk: Generated images may drift from the actual product or present unsuitable model styling.

Mitigation: Review the complete set for product fidelity and edit the brand example when its default model demographic or Chinese-only workflow is unsuitable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Provider setup and output guide](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown instructions and commands; generated JPEG product images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Multiple shots use the same reference image; images can be saved locally when generation is requested.]

## Skill Version(s):

1.0.20 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
