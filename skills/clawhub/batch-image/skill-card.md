## Description:

Guides agents through generating visually consistent ecommerce product images from a SKU list, with concurrency, retries, resume support, cost limits, and a contact sheet for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce teams and developers use this skill to plan and run batch product-image generation from SKU lists while keeping a consistent visual style and tracking costs and outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected prompts and product images are uploaded to the configured generation provider.

Mitigation: Confirm the provider and obtain approval before uploading sensitive product materials.

Risk: Batch jobs can consume provider credits, especially with many SKUs or retries.

Mitigation: Review the request and estimated cost with --dry-run, then set a spending limit before running the full batch.

Risk: Untrusted DLAZY_BIN values can change which executable is run; provider credentials also need protection.

Mitigation: Use a trusted executable path and keep API keys scoped and private.

Risk: Generated product imagery may not faithfully represent the item or satisfy marketplace requirements.

Mitigation: Manually review sampled and final outputs before marketplace upload.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/batch-image)
- [Provider CLI and data flow](artifact/references/provider-cli.md)
- [Model flags](artifact/references/model-flags.md)
- [Marketplace image specifications](artifact/references/platform-specs.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides generation of per-SKU images, a batch manifest, and an optional HTML contact sheet for human review.]

## Skill Version(s):

1.0.23 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
