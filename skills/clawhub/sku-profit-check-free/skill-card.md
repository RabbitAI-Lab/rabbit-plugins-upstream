## Description:

Recompute true gross profit and margin per SKU, including price, cost, first-leg freight, platform commission, ad spend, return loss, and FX conversion; flag miscomputed rows, low-margin rows, totals issues, duplicate rows, blanks, and negative values with source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, cross-border ecommerce operators, and finance teams use this skill during month-end SKU profit checks to recalculate gross profit and margin from user-provided tables. It helps identify rows where platform or internal margin figures omit freight, advertising, return loss, or FX effects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The core checker appears local, but the skill includes agent-directed paid upgrade, external install, and purchase instructions beyond the advertised offline tool.

Mitigation: Use the free local checker only after reviewing the skill source, and do not allow an agent to run payment-tool installation or purchase workflows unless the provider, package, product, and payment terms are separately verified by the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/sku-profit-check-free)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable Markdown or JSON results with per-row findings and source line numbers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; no API key or network is required for the core checker.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
