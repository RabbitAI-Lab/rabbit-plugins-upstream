## Description:

Identifies Amazon review and product-detail evidence that may signal return-driving expectation gaps, then suggests product improvements without claiming actual return-rate prediction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce operators use this skill to review Amazon ASIN comments and product details for evidence-backed return-risk signals and product-improvement opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI may allow workflow or focus overrides beyond the advertised fixed return-risk workflow.

Mitigation: Use only the documented product/risk operations flow and verify commands do not include unexpected --workflow or --focus values before confirmation.

Risk: Confirmed collection or analysis can spend ARI credits.

Mitigation: Run quote first, continue only after explicit user confirmation, and reuse the quoted requestId rather than rerunning interrupted workflows.

Risk: Outputs may be mistaken for actual return-rate, refund, inventory, or customer-service decisions.

Mitigation: Treat results as review-evidence signals only and keep final operational decisions outside the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/return-risk)
- [Amazon return-risk operation workflow](artifact/references/operation-workflow.md)
- [Amazon return-risk API reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown narrative with CLI command snippets and ARI quote, run, and status results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection and analysis require an explicit user confirmation after quote.]

## Skill Version(s):

1.4.11 (source: release evidence, _meta.json, CHANGELOG, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
