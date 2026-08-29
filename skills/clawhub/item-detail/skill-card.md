## Description:

Generates Chinese-typography ecommerce item detail image modules from product photos and concise selling points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce operators, designers, and agents use this skill to create Chinese product detail visuals from a product image and short selling points. It helps generate modular assets such as hero banners, selling-point icon rows, material blocks, detail displays, and parameter blocks for product listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and optional brand references may be sent to dLazy or a selected model provider.

Mitigation: Avoid confidential product photos, secrets, and private customer data; use dry-run and provider selection to inspect what will be sent before running generation.

Risk: Generated Chinese text, product details, or layout may be inaccurate or hard to read.

Mitigation: Generate modules in batches, choose the clearest result, and review all text and product fidelity before publishing.

Risk: Selling-point prompts may create unsupported claims, certifications, promotions, or comparisons if not constrained.

Mitigation: Use only verified product claims and remove any generated claim that is not supported by product evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-detail)
- [Model flags](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance with bash commands and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image modules should be reviewed for readable Chinese text, product fidelity, and supported claims before publication.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
