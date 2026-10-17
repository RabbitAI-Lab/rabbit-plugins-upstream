## Description:

Turns one product image and its selling points into a coordinated set of e-commerce images showing different angles, details, and scenes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use the skill to turn a single product photo into a consistent collection of listing and detail-page images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts may be sent to a selected cloud image provider.

Mitigation: Inspect requests with dry-run and use only providers approved for sensitive or unreleased images.

Risk: Image-generation runs may incur charges or expose API credentials if handled carelessly.

Mitigation: Review provider costs and key handling before running a full set.

Risk: Generated images may alter product details or imply unsupported features.

Mitigation: Compare each image with the source product and verify claims before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Model flags](references/model-flags.md)
- [Provider CLI and data flow](references/provider-cli.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Image files with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Multiple product views; image format and quality depend on the selected provider and settings.]

## Skill Version(s):

1.0.22 (source: SKILL.md frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
