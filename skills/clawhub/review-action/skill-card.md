## Description:

Amazon 评论转行动 combines Amazon product details and review data to turn recurring customer issues into product, packaging, listing, and supplier action tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon operators and product teams use this skill to convert ASIN review evidence into prioritized product, packaging, listing, and supplier follow-up actions. It supports evidence-grounded operational decisions rather than buyer contact, page edits, or purchasing execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI account credits automatically when server-controlled auto-confirm rules allow paid workflows to proceed.

Mitigation: Set the confirmation policy to always ask before using paid workflows if automatic credit spending is not desired, and check quoted credits before confirming operations.

Risk: The skill stores an ARI API key locally, and the security evidence notes that local key file handling is not hardened against symlink manipulation.

Mitigation: Use the skill only on trusted machines, avoid shared environments, and revoke or recreate the ARI API key if local credential exposure is suspected.

Risk: Review-based recommendations can be incomplete when samples, collection windows, product details, or supported marketplaces are limited.

Mitigation: Review the reported data scope, sample size, collection window, and cited review evidence before treating suggested product or supplier actions as decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/review-action)
- [Operation Workflow](references/operation-workflow.md)
- [ARI CLI and API Reference](references/reference.md)
- [ARI User Center](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or concise text with ARI CLI commands when setup, troubleshooting, or confirmed operations require them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include data scope, cited review evidence, trend caveats, action priorities, report identifiers, credit usage, and report links when returned by ARI.]

## Skill Version(s):

1.4.7 (source: frontmatter, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
