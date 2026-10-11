## Description:

Generates visually consistent product images from a SKU list, with concurrency, retries, resume support, cost controls, and a contact sheet for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and developers use this skill to turn a CSV of products and reference images into consistent product photography, track batch results, and review images before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product descriptions and reference images are sent to the configured image-generation provider.

Mitigation: Use only intended images and prompts, and review the provider's data-sharing terms before running.

Risk: Large batches may incur substantial generation costs.

Mitigation: Start with a dry run and a small SKU sample, then set a batch credit limit.

Risk: Example brand settings or generated images may not match a merchant's requirements.

Mitigation: Customize the brand template and review sample outputs before publishing the full batch.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/batch-image)
- [Provider CLI reference](references/provider-cli.md)
- [Model flags](references/model-flags.md)
- [Platform specifications](references/platform-specs.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, Files, Shell commands, Guidance]

**Output Format:** [Product image files, JSON batch manifest, HTML contact sheet, and text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-SKU results, retries, resume state, and estimated credit budget controls.]

## Skill Version(s):

1.0.19 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
