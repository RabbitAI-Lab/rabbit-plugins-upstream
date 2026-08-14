## Description:

Creates and iteratively updates Chinese patent pre-evaluation reports from invention disclosures, draft technical materials, or existing reports, using PatSnap/智慧芽 search evidence when configured.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent and intellectual-property staff, inventors, and patent agents use this skill to turn technical concepts, disclosure drafts, or prior reports into structured Chinese pre-application patent evaluation reports. It supports novelty-point extraction, PatSnap/智慧芽 evidence collection, feature comparison, patentability risk assessment, abnormal-application risk checks, and application strategy recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpublished invention details may be exposed through patent-search inputs sent to PatSnap/智慧芽 MCP services.

Mitigation: Minimize disclosure by sending only keywords, IPC classes, and abstracted technical features where possible, and follow the skill's confidentiality guidance before running searches.

Risk: API keys or MCP credentials could be mishandled if placed in prompts, shared documents, or source control.

Mitigation: Store credentials only in the MCP client's secure configuration or environment and avoid including them in reports or chat prompts.

Risk: AI-assisted patentability conclusions and search results may be incomplete or require professional judgment.

Mitigation: Require review by intellectual-property staff or a patent agent before using the report for filing decisions.

## Reference(s):

- [Skill page](https://clawhub.ai/yuanzhian-patsnap/skills/patent-pre-evaluation-report)
- [Report workflow reference](references/report-workflow.md)
- [PatSnap developer documentation](https://open.patsnap.com/devportal)
- [PatSnap/智慧芽 MCP server marketplace](https://open.zhihuiya.com/marketplace/mcp-servers)
- [PatSnap/智慧芽 security center](https://www.zhihuiya.com/security-center)

## Skill Output:

**Output Type(s):** [Files, Analysis, API Calls, HTML, Guidance]

**Output Format:** [Self-contained HTML report with structured tables, evidence summaries, risk judgments, and application strategy guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires configured PatSnap/智慧芽 MCP services for live patent and literature search evidence; incomplete or unverified evidence is marked for supplementation or review.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
