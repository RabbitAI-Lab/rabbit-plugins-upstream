## Description:

Generates conversion-focused ecommerce main images by combining a product image with concise Chinese selling-point copy and layout guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, designers, and ecommerce operators use this skill to produce single-image product listing creatives with readable Chinese selling points, badges, and product-preserving layout prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, prompts, and marketing copy may be sent to dLazy or another configured image provider.

Mitigation: Use only approved providers and inputs, and avoid confidential product assets unless the provider terms and data handling are acceptable.

Risk: Generated main-image copy may contain inaccurate product claims, unverified promotions, or overly broad marketing language.

Mitigation: Review all product claims, discounts, and promotional text against source-of-truth product and campaign data before publishing.

Risk: Provider credentials, CLI selection, or credit use may be misconfigured before execution.

Mitigation: Check provider credentials, credit costs, and that DLAZY_BIN/PATH resolves to a trusted CLI before running generation commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0-pro model flags](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and locally saved image assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are saved to user-selected paths; cloud providers may return hosted asset URLs and credit estimates.]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
