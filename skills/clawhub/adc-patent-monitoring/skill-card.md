## Description:

监控ADC新申请、专利族、法律状态和竞争风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent intelligence and IP teams use this skill to generate weekly or monthly ADC patent monitoring reports covering new WO applications, family and legal-status signals, applicant activity, and competitive risk. It is intended for Eureka Desktop workflows backed by the PatSnap patent MCP server and a valid PatSnap account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on a trusted PatSnap MCP server configuration and a PatSnap Bearer Token for patent queries.

Mitigation: Confirm the MCP server source and credential handling before installation, and use only approved PatSnap credentials in Eureka Desktop.

Risk: Generated HTML reports can contain sensitive competitive and patent intelligence.

Mitigation: Store, share, and archive generated reports according to the organization's confidential-business-information handling rules.

Risk: The HTML template loads Chart.js from an external CDN when the report is opened.

Mitigation: Open reports only in environments where that network access is acceptable, or replace the dependency with an approved local asset before broader deployment.

Risk: If Eureka Desktop, the PatSnap MCP server, or valid credentials are unavailable, the report workflow cannot collect evidence or produce a complete report.

Mitigation: Run the documented connectivity check before report generation and stop rather than publishing a report when required patent evidence cannot be collected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/adc-patent-monitoring)
- [ADC Report HTML Template](artifact/references/adc_report_template_v4.1.html)
- [PatSnap Analytics Patent Detail URL Template](https://analytics.zhihuiya.com/patent-view/abst?patentId={patent_id})

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, structured JSON patent data, and generated HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Eureka Desktop, the PatSnap patent MCP server, and a valid PatSnap account or API access.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
