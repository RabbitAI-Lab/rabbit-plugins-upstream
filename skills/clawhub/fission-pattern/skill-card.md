## Description:

Guides creation of a consistent set of e-commerce product images from one reference photo, with varied angles and scenes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and content creators use this skill to plan and generate coordinated product listing and detail-page image sets from a single product photo and selling points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference product images and prompts are sent to the selected image-generation provider.

Mitigation: Select a provider acceptable for the data and avoid uploading confidential product imagery without approval.

Risk: Generating multiple images can incur provider charges.

Mitigation: Use dry-run to inspect requests and estimated costs before running the full set.

Risk: Generated images may misrepresent product appearance or details.

Mitigation: Review every image against the reference for product consistency and regenerate any inaccurate image.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Provider setup and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy CLI documentation](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and bash commands; generated JPEG, PNG, or WebP images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Individual images can be regenerated; image generation may incur provider charges.]

## Skill Version(s):

1.0.24 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
