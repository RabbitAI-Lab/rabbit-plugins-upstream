## Description:

Combines up to eight product images into one coordinated outfit image on a model while aiming to preserve each item's visual details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers use this skill to combine product photos into a coordinated look on one model for product imagery. It supports optional model and scene references to help keep a set of images visually consistent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploading product, model, or face images may expose private or sensitive material to the selected provider.

Mitigation: Review the provider's image and prompt handling, and confirm you are allowed to upload each image.

Risk: The selected backend may ignore some reference images; ClawScan specifically notes this for Replicate.

Mitigation: Confirm that the chosen backend supports all supplied references and inspect the result for every requested item.

Risk: The security analysis is incomplete and does not establish that the skill is safe.

Mitigation: Treat the release as suspicious before installing and review the provider's image and prompt handling.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Seedream 5.0 parameter reference](references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, Prompt text, Shell commands, Guidance]

**Output Format:** [Generated image files with accompanying prompt and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Combines up to eight product images; optional model or scene reference images can also be supplied. Review generated images to confirm all requested items are represented accurately.]

## Skill Version(s):

1.0.31 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
