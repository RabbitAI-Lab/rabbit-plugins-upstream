## Description:

用已有 Amazon ASIN 的商品详情与至少 10 条评论检查改版或重新上线准备度风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT

## Use Case:

External Amazon sellers and operators use this skill through an agent to assess relaunch readiness for existing ASINs from product-detail and review evidence. It helps identify listing, review, and operating risks before an updated product page or relaunch workflow is run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI review-analysis workflows may spend account credits, including service-side auto-confirmed charges.

Mitigation: Review or disable ARI auto-confirm behavior, check quotes and balances before paid runs, and monitor completed reports for charges.

Risk: Schedule, watch, competitor-tracking, and autoconfirm commands can create persistent account changes rather than one-time analyses.

Mitigation: Treat these commands as account-management actions, require explicit user intent, and periodically review active monitors and auto-confirm settings.

Risk: The skill requires access to an ARI API key for account operations.

Mitigation: Use the documented setup or local configuration flow, avoid placing keys in prompts or reports, and rotate the key if exposure is suspected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/launch-readiness)
- [README](artifact/README.md)
- [Dedicated Operations Workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API Reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI command output and report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an existing ASIN, ARI API key, supported Amazon site, and sufficient review evidence; paid workflows may require quote confirmation or service-side auto-confirm behavior.]

## Skill Version(s):

1.4.5 (source: frontmatter, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
