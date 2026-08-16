## Description:

Conspect is an automated multi-source spreadsheet analysis and business report rendering skill that turns uploaded Excel-style data into dashboards, charts, and presentation-ready reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songzhou666](https://clawhub.ai/user/songzhou666)

### License/Terms of Use:

MIT-0

## Use Case:

Business analysts, operators, managers, and developers use this skill to transform uploaded Excel, CSV, or similar spreadsheet data into automated business dashboards, chart selections, insight summaries, and report exports. It is intended for report generation, data dashboards, Excel charting, projection-ready summaries, and multi-table analysis rather than simple data cleanup or desktop BI replacement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a broad automatic local workflow that may read uploaded spreadsheet data, invoke bundled Python tools, and write multiple persistent artifacts.

Mitigation: Install and run it only in a dedicated project folder with non-sensitive or approved data, and review generated files before sharing them.

Risk: The security evidence flags broad automatic execution, file access, and write authority without enough user control.

Mitigation: Keep execution scoped to the intended skill directory and avoid allowing the workflow to search for or execute tool copies from unrelated locations.

Risk: Generated reports and charts may contain automated assumptions, inferred analyses, or misleading summaries if source data is incomplete or ambiguous.

Mitigation: Review the final dashboards, reports, assumptions, and data interpretations before using them for business decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/songzhou666/skills/conspect)
- [Server-resolved source repository](https://github.com/songzhou666/conspect)
- [Output specification](artifact/references/output-spec.md)
- [Trigger guide](artifact/references/trigger-guide.md)
- [Quality audit reference](artifact/references/quality-audit.md)
- [CLI and AI workflow reference](artifact/references/cli-ai-workflow.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, HTML, JSON, Files, Shell commands]

**Output Format:** [Markdown reports, HTML dashboards, PDF/Word exports, JSON insight data, and CLI status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates persistent report artifacts such as dashboards, analysis reports, verification reports, and localized filename copies.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata; artifact frontmatter and changelog report v3.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
