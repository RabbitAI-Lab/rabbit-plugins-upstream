## Description:

企业风险平台2——金融机构风控管理平台完整复原手册。基于智慧芽PatSnap科创类数据，支持评级变动分析、科创风险快照、批量风险巡检、季度预警名单，自动扫描6个严重风险维度和8个关注风险维度，输出三层可解释风险快照报告（HTML）。含5步分步复原指令，客户可从零复原金融机构风控管理平台。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and implementation teams use this skill to recreate a PatSnap-backed financial institution risk-control dashboard with rating-change analysis, technology-risk snapshots, batch risk inspection, quarterly warning lists, and HTML/PDF report workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live PatSnap/Eureka MCP lookups may involve company names, credit codes, and query results that are sensitive business data.

Mitigation: Use live queries only when the organization permits those inputs to be sent to PatSnap services, and handle results under approved business-data controls.

Risk: Without PatSnap account authorization and MCP configuration, the skill can only provide the dashboard and analysis framework rather than live database-backed conclusions.

Mitigation: Complete the documented PatSnap/Eureka MCP setup before relying on live lookup behavior, and label any unconfigured output as demonstration or framework-only.

## Reference(s):

- [PatSnap Open Platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, configuration]

**Output Format:** [Markdown instructions with HTML, CSS, JavaScript, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a single-file HTML dashboard workflow and report-generation guidance; live queries require PatSnap/Eureka MCP configuration.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
