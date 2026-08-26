## Description:

Report to Article edits completed research reports into reader-friendly articles while preserving the original facts, evidence boundaries, relationships, source attributions, and judgment strength.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wujiaming88](https://clawhub.ai/user/wujiaming88)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, analysts, and editors use this skill to turn completed research reports, weekly reports, or research-heavy drafts into structured articles without adding unsupported facts or weakening source boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The edited article could drift from the source report by changing facts, dates, numbers, attribution, relationships, or judgment strength.

Mitigation: Build an atomic information checklist before editing, then perform forward coverage and reverse traceability checks before delivery.

Risk: The article could introduce unsupported background, causal claims, comparisons, or conclusions while improving readability.

Mitigation: Keep new background as an editorial suggestion unless the user explicitly authorizes additional research, and ensure transitions and headings only express relationships supported by the report.

Risk: Visuals could imply facts or patterns that the report does not support.

Mitigation: Use report-sourced images or data first, label conceptual diagrams as illustrative, and include a title, caption, source, and alt text for generated or redrawn visuals.

Risk: Long-report mode may create or update Markdown articles and optional asset files in the workspace.

Mitigation: Review generated files and assets before reuse, especially when the source report is long enough to trigger chunked writing.

## Reference(s):

- [Atomic Information and Bidirectional Review Template](references/info-checklist-template.md)
- [Article Structure and Section Design](references/logic-skeleton.md)
- [Long Report Protocol](references/long-report-protocol.md)
- [Reader-Oriented Prose Style](references/prose-style.md)
- [Objective Title Rules](references/title-rules.md)
- [Article Visual Guidelines](references/visual-guidelines.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown article text, with structured visual plans or generated assets when requested and supported.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Short reports are returned inline; long reports may be written as <report-name>-article.md with optional adjacent assets.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
