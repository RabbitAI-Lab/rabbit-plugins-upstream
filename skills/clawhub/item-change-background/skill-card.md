## Description:

Helps turn plain-background product photos into realistic lifestyle scenes with matched lighting, reflections, and contact shadows while preserving product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and marketers use this skill to place product photos into believable commercial scenes while retaining the product's appearance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, prompts, and optional brand references may be sent to a chosen cloud image provider.

Mitigation: Check that provider's privacy and retention terms before uploading sensitive or unreleased assets.

Risk: Generated scenes may alter product details or suggest an implausible use.

Mitigation: Review outputs for product fidelity, credible lighting and shadows, and non-misleading placement before publishing.

Risk: Image generation may incur provider charges.

Mitigation: Use dry-run and configuration checks before making paid generation calls.

## Reference(s):

- [Image model options](artifact/references/model-flags.md)
- [Provider CLI and data flow](artifact/references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with prompt templates and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can generate and save product-scene images through a configured image provider.]

## Skill Version(s):

1.0.19 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
