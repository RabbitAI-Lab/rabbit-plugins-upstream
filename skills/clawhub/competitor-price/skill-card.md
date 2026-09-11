## Description:

基于主 ASIN 与已授权竞品商品页中记录的展示价格快照，说明相对价格位置、时间点和证据缺口；不宣称实时价格，也不用于销量、利润、库存、订单或自动调价。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon marketplace operators use this skill to compare a primary ASIN with authorized competitor product-page snapshots for price positioning and evidence gaps. It helps frame an ARI operations report request while keeping the scope separate from real-time pricing, inventory, order, profit, or automatic repricing decisions.

### Deployment Geography for Use:

Global, subject to supported Amazon marketplaces and ARI account availability.

## Known Risks and Mitigations:

Risk: The skill is positioned around competitor price snapshots, but the bundled ARI assistant behavior also covers broader review analytics, exports, monitoring, account settings, and paid operations.

Mitigation: Review the full skill before installing and use it only if those broader ARI capabilities are acceptable for the target environment.

Risk: The skill requires ARI API access and can store an API key locally.

Mitigation: Authorize only from a trusted local environment, do not paste API keys into chat or reports, and revoke or rotate the key from the publisher account page when access is no longer needed.

Risk: Some ARI workflows can consume credits, export reports or reviews, or change monitoring and confirmation settings.

Mitigation: Keep paid runs, exports, schedule/watch changes, and auto-confirm settings behind explicit user intent and review returned credit, balance, and cost information before confirming.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/competitor-price)
- [Operation Workflow](references/operation-workflow.md)
- [ARI CLI and API Reference](references/reference.md)
- [User Guide](使用说明.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text guidance with optional shell commands, report links, and export files when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and may return report IDs, report URLs, credit usage, or local CSV/Markdown/HTML exports depending on the requested workflow.]

## Skill Version(s):

1.4.8 (source: frontmatter, _meta.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
