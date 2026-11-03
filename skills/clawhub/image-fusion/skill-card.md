## Description:

Combines up to eight product images into one coordinated, model-worn look while aiming to preserve each item's visual details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams use this skill to combine product photos into coordinated, model-worn look images for catalogs and marketing content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images, including optional face or brand-reference photos, are sent to the chosen cloud provider.

Mitigation: Choose the provider explicitly and check consent and retention terms before uploading images.

Risk: Pricing estimates may conflict, and Replicate is not suitable for multi-image fusion in this workflow.

Mitigation: Review --dry-run and verify current pricing and image limits before paid generation.

Risk: The external dLazy CLI and remote service behavior were not inspected.

Mitigation: Use a trusted version of the CLI and review the request before execution.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, Shell commands]

**Output Format:** [Generated raster image files (typically JPEG) saved to a chosen path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One or more images may be produced with batch generation; format and resolution depend on provider settings.]

## Skill Version(s):

1.0.29 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
