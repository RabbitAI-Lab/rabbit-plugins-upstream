## Description:

基于 Amazon 商品详情与评论证据梳理用户价值、适用场景和可验证的产品定位方向；需要 ARI API Key，不用于市场规模、销量预测或广告执行。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, operators, and support agents use this skill to turn product detail and review evidence into positioning direction, pain-point summaries, scenario fit, and prioritized improvement guidance. It supports concise answers and fuller reports when enough product and review data are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI actions can consume credits, and account confirmation or monitoring settings may change ongoing behavior.

Mitigation: Use quote-only flows before paid actions, require explicit confirmation for paid runs and setting changes, and disable or avoid auto-confirm when every charge should be approved first.

Risk: The skill uses an ARI API Key and can send credential-bearing requests to the configured ARI endpoint.

Mitigation: Keep API keys out of chat and reports, use browser setup or local configuration, and leave ARI_BASE_URL unset unless intentionally using a trusted self-hosted endpoint.

Risk: Reports and exports can store Amazon review data locally or in the ARI account.

Mitigation: Treat generated exports as business data, limit sharing to intended recipients, and review report links and files before distributing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/product-positioning)
- [Operation workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Concise text summaries or Markdown reports, with CLI commands for setup and optional local Markdown, HTML, or CSV exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include ASIN, site, sample size, reporting window, reportId, reportUrl, creditsUsed, and current balance when returned by ARI.]

## Skill Version(s):

1.4.7 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
