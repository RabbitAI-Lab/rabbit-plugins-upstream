## Description:

基于 Amazon 商品字段和评论反馈，识别商品描述的信息缺口并给出改写建议；需要 ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and e-commerce operators use this skill to run evidence-based product-description analysis from Amazon product fields and review feedback. It returns description-focused improvement guidance without writing bullet points, creating ads, or automatically publishing changes to Amazon pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The packaged ARI client exposes broader review-intelligence, monitoring, export, competitor, alert, and workflow actions than the narrow product-description listing suggests.

Mitigation: Install only after accepting the broader ARI account scope, and constrain use to description analysis unless the user explicitly requests another supported ARI action.

Risk: Paid collection or AI analysis can spend ARI credits, and auto-confirm settings may allow some operations to proceed without a fresh prompt.

Mitigation: Run quote and capability checks first, report credits and balance, require explicit user confirmation for paid operations, and review auto-confirm thresholds before use on sensitive accounts.

Risk: The skill can read Amazon product and review data, export files locally, and change monitoring or watch state.

Mitigation: Use an account-scoped ARI API key, do not expose the key in outputs, confirm export destinations and watch IDs before changes, and audit locally exported files.

## Reference(s):

- [Skill README](README.md)
- [Dedicated Operations Workflow](references/operation-workflow.md)
- [ARI CLI and API Reference](references/reference.md)
- [ARI API Key Management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Product Management](https://ari.funewa.com/zh/products)
- [ClawHub Skill Listing](https://clawhub.ai/funewa/skills/description-writer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON command responses and local export files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ARI report IDs, report URLs, credit usage, account balance, and locally saved CSV, Markdown, or HTML export paths.]

## Skill Version(s):

1.4.5 (source: frontmatter, _meta.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
