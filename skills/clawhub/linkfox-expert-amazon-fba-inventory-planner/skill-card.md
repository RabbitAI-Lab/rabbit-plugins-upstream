## Description:

亚马逊 FBA 库存计划与补货专家。适用于库存规划、销量速度估算、补货时间计算、安全库存设置、库存风险检查、FBA 补货测算和库存计划报告的场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and operations teams use this skill to plan FBA replenishment, safety stock, inbound timing, aged-inventory actions, and cash impact from user-provided or retrieved inventory and sales data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated LinkFox cloud service calls and API keys can expose account access if configured for untrusted endpoints.

Mitigation: Install only for intended LinkFox use, keep gateway/base URL settings pointed at trusted LinkFox endpoints, and protect API keys.

Risk: Amazon seller authorization flows and account-linked inventory reports may expose sensitive seller data.

Mitigation: Authorize only intended seller accounts, review requested actions before proceeding, and do not provide phone or SMS codes unless authorization is deliberate.

Risk: Public file uploads, scheduled background tasks, and local report/data caching can retain or disclose operational data.

Mitigation: Upload only intended files, review scheduled task contents and webhook targets, and remove local cached reports when they contain sensitive data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-amazon-fba-inventory-planner)
- [Data Contract & Missing-Data Degradation](artifact/skills/amazon-fba-inventory-planning/references/data-contract.md)
- [Demand Forecasting for Amazon FBA Inventory Planning](artifact/skills/amazon-fba-inventory-planning/references/demand-forecasting.md)
- [Safety Stock & Reorder Point Guidance for Amazon FBA](artifact/skills/amazon-fba-inventory-planning/references/safety-stock.md)
- [Amazon FBA Fees Reference (2026)](artifact/skills/amazon-fba-inventory-planning/references/fba-fees.md)
- [Multi-Warehouse & AWD Allocation (FBA Planning)](artifact/skills/amazon-fba-inventory-planning/references/multi-warehouse.md)
- [Ads-Inventory Linkage for FBA Planners](artifact/skills/amazon-fba-inventory-planning/references/ads-inventory-linkage.md)
- [Exception Alerts & Priority Scoring (FBA Planner)](artifact/skills/amazon-fba-inventory-planning/references/exception-priority.md)
- [Weekly FBA Inventory Plan Output Guide](artifact/skills/amazon-fba-inventory-planning/assets/weekly-plan-output-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses, HTML reports, CSV/JSON planning files, and script outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long reports may be written to local report/data directories; recommendations depend on user-provided or authorized inventory and sales data.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
