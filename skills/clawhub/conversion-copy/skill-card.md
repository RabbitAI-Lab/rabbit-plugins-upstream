## Description:

Combines Amazon product-detail and review evidence to diagnose buyer decision barriers and propose conversion-copy improvements without predicting conversion rate, managing ads, or publishing listing changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and supporting agents use this skill to turn product details and review signals into evidence-based listing copy recommendations for the listing/conversion workflow. It is not intended for conversion-rate or sales prediction, ad bidding, or automatic publication of Amazon listing changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary flags paid ARI actions and persistent account or monitoring changes as broader than the narrow conversion-copy description.

Mitigation: Install only where ARI account access, credit-spending workflows, product monitoring, competitor bindings, and exports are acceptable for the operator.

Risk: Auto-confirm settings can allow small paid actions to proceed without a separate prompt.

Mitigation: Review or disable auto-confirm settings when every paid action should require explicit approval.

Risk: The skill depends on an ARI API key.

Mitigation: Use the documented ARI key setup flow or environment variable handling, and do not include API keys in reports, prompts, or command examples.

## Reference(s):

- [ARI CLI and API Reference](references/reference.md)
- [Amazon Conversion Copy Operations Workflow](references/operation-workflow.md)
- [ARI API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Products](https://ari.funewa.com/zh/products)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with supporting CLI commands and JSON-backed report references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and may invoke quoted, confirmation-gated ARI actions that consume credits.]

## Skill Version(s):

1.4.5 (source: server release metadata, skill frontmatter, _meta.json, and scripts/ari.py VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
