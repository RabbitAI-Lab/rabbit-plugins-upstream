## Description:

从 Amazon 评论中的破损、缺件、开箱和收纳反馈提炼包装改进任务与证据；仅用于包装问题分析，不用于物流索赔、供应商下单或库存执行，需要 ARI API key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and product operators use this skill to turn review evidence about shipping damage, missing parts, unboxing, and storage into packaging improvement tasks. It checks ARI account status, product data, pricing, and existing review evidence before generating packaging-focused operational guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill name suggests packaging analysis, but the ARI CLI can also access account, billing, monitoring, export, competitor, alert, and paid-analysis workflows.

Mitigation: Install only when that broader ARI account access is acceptable, and avoid schedules, watches, competitors, exports, or paid reports unless those actions are explicitly intended.

Risk: Some analysis flows can consume ARI credits when account auto-confirm rules allow direct execution.

Mitigation: Set auto-confirm to always ask or request quote-only behavior when per-transaction approval is required.

Risk: The skill uses an ARI API key for account access.

Mitigation: Use the browser authorization or local configuration flow, keep the key out of chat and reports, and revoke or recreate the key if access is no longer desired.

Risk: Review-derived recommendations can be misleading when samples are small, incomplete, stale, or not comparable across products.

Mitigation: Keep the reported sample size, time window, site, and data gaps visible, and treat low-volume findings as directional until verified with more evidence.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/packaging-improve)
- [Usage Guide](使用说明.md)
- [ARI CLI and API Reference](references/reference.md)
- [Packaging Operation Workflow](references/operation-workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown prose with inline shell commands and links; CLI responses may be summarized from JSON results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Outputs may include report links, local export paths, credit usage, account status, and confirmation prompts for paid or state-changing actions.]

## Skill Version(s):

1.4.7 (source: server release evidence, frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
