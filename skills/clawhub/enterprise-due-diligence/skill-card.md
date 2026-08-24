## Description:

企业尽调技能，对目标企业进行法律、财务、业务三维度尽职调查，自动从公开数据源和用户提供材料整理工商、股权、司法、知识产权、财务和业务信息，并生成结构化尽调报告与检查清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[merlinbeard000](https://clawhub.ai/user/merlinbeard000)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, investors, and business teams use this skill for investment due diligence, merger and acquisition review, supplier or partner background checks, and IPO-readiness screening. It helps collect public company information, incorporate user-provided materials, classify P0/P1/P2 risks, and prepare human-reviewable deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may send the target company name to external company-data services.

Mitigation: Use it only for companies the user intends to investigate, disclose external lookup behavior, and avoid adding unnecessary personal or confidential information to lookup prompts.

Risk: Generated due-diligence findings can be incomplete, stale, or inconsistent across public sources.

Mitigation: Verify findings against official records and professional advice, preserve source and timestamp notes, and keep unverified fields marked as pending verification.

Risk: User-provided reports, contracts, screenshots, or financial materials may contain sensitive business or personal data.

Mitigation: Provide only materials needed for the report, redact unrelated sensitive data, and limit sharing of generated outputs to authorized reviewers.

Risk: Optional company-data connectors require API credentials.

Mitigation: Store credentials in environment variables or connector configuration, never embed them in prompts, source files, or generated reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/merlinbeard000/skills/enterprise-due-diligence)
- [Data quality rules](artifact/references/data_quality.md)
- [Report template specification](artifact/references/report_template.md)
- [Checklist template specification](artifact/references/checklist_template.md)
- [Risk classification framework](artifact/references/risk_classification.md)
- [Company-data connector reference](artifact/references/mcp_connectors.md)
- [Qichacha open API](https://open.api.qichacha.com)
- [Tianyancha MCP endpoint](https://mcp.tianyancha.com/v1)
- [Qixin MCP endpoint](https://mcp.qixin.com/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Human-facing analysis and guidance, JSON data inputs, shell commands, and Word .docx due-diligence report and checklist files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses source-attributed findings, pending-verification markers for incomplete data, P0/P1/P2 risk classification, and optional lite or standard report templates.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence; artifact frontmatter and marketplace metadata list 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
