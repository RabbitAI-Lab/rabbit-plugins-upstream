## Description:

Monitors patent litigation risk for specified assignees by finding litigated patents, expanding INPADOC families, cross-checking PatSnap legal data with public web sources, and producing target-centric risk reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

IP, legal, and patent intelligence teams use this skill to monitor patent litigation exposure for one or more target assignees. It supports family expansion, case timeline analysis, inventor trend review, and practical regional risk, defense alert, and trend forecasting conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Assignee names and patent identifiers may be sent to PatSnap/MCP and web search providers.

Mitigation: Use the skill only with target lists approved for querying through those services.

Risk: Generated HTML reports and downloaded patent images may contain sensitive business research.

Mitigation: Store and share report artifacts only with intended IP, legal, or patent intelligence reviewers.

Risk: The included legacy renderer can preserve remote image URLs in confidential reports.

Mitigation: Prefer embedded image data or review generated report HTML before sharing confidential outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/litigation-risk-monitor)
- [PatSnap Open Platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance, files]

**Output Format:** [Agent workflow guidance that produces a local HTML report with structured JSON and CSV attachments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include patent family analysis, litigation timelines, case deep dives, inventor trends, and regional risk conclusions.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
