## Description:

A Chinese-language AI assistant for industrial park investment and leasing teams that supports customer follow-up, property search, reception preparation, quotation proposals, site-selection recommendations, contract drafting, channel management, local SQLite data access, and configured knowledge-base workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[perrykono-debug](https://clawhub.ai/user/perrykono-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External commercial leasing and investment teams use this skill as an operational assistant for prioritizing today's customers, reviewing customer context, planning next actions, preparing proposals, and keeping follow-up records current. It supports business workflows but keeps pricing concessions, contracts, discounts, customer-facing messages, and status changes subject to human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The assistant can store, update, and cache customer, channel, pricing, room, and proposal data in local WorkBuddy files, SQLite, and configured Tencent Docs.

Mitigation: Require human review and explicit approval before writes, contracts, discounts, customer-facing messages, or customer/status changes.

Risk: Some company or competitor intelligence may be draft, mock, stale, or incomplete.

Mitigation: Treat generated intelligence as a working draft and verify it against live, authoritative sources before business use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/perrykono-debug/skills/industrial-park-investment-assistant)
- [AI Execution Checklist](references/AI执行检查清单.md)
- [Full-Cycle Investment SOP](references/招商实战_全周期SOP.md)
- [Customer Segmentation and Profiles](references/招商实战_客户分级与画像.md)
- [Property Inventory Reference](references/园区基础_房源信息.md)
- [Rent Quotation Reference](references/园区基础_租金报价.md)
- [Local Industrial Policy Reference](references/政策文件_地方产业政策.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON configuration examples, Python scripts, shell commands, and structured operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include customer summaries, follow-up recommendations, quotation and TCO proposal drafts, site-selection documents, dashboards, and local data-sync artifacts.]

## Skill Version(s):

3.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
