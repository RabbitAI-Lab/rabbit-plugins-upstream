## Description:

Conspect guides an agent through a five-stage workflow for analyzing Excel and CSV data and generating professional reports, with user confirmation for content and style choices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songzhou666](https://clawhub.ai/user/songzhou666)

### License/Terms of Use:

MIT-0

## Use Case:

People preparing business reports can use Conspect to inspect one or more Excel or CSV sources, analyze their data, choose report content and style, and produce a dashboard or report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review findings report that user approvals may be skipped and content may exceed selected choices.

Mitigation: Confirm the content and style choices, then compare the generated report with those choices before using it.

Risk: The report template loads third-party JavaScript.

Mitigation: Review the generated report and its script dependency before opening it with sensitive data.

Risk: The preview output path is reported as unrestricted.

Mitigation: Check the preview destination and ensure it is an intended location before generating the preview.

Risk: Security review coverage was partial and some analyzers were degraded.

Mitigation: Treat the scan results as incomplete and review the findings before installation.

## Reference(s):

- [Conspect on ClawHub](https://clawhub.ai/songzhou666/skills/conspect)
- [Source repository (server-resolved provenance)](https://github.com/songzhou666/conspect)
- [Resolved source commit](https://github.com/songzhou666/conspect/commit/8d80bcfe2affe10dd90e7b4143191b1885b3e3be)
- [Conspect usage guide](https://github.com/songzhou666/conspect/blob/8d80bcfe2affe10dd90e7b4143191b1885b3e3be/references/cli-usage.md)
- [Conspect data quality review guide](https://github.com/songzhou666/conspect/blob/8d80bcfe2affe10dd90e7b4143191b1885b3e3be/references/quality-audit.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, HTML, JSON, PDF, DOCX]

**Output Format:** [Markdown reports and HTML dashboards, with JSON workflow artifacts and optional PDF or DOCX exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [PDF and DOCX exports require optional dependencies; report content and style are selected with user confirmation.]

## Skill Version(s):

0.1.2 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
