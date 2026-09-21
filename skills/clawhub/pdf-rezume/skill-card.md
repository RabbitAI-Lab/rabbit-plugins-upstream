## Description:

Creates a one-page Russian executive-summary PDF from a user-provided PDF report, with local OCR support for scans and automated number checks against extracted page text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iirtegova](https://clawhub.ai/user/iirtegova)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users use this skill when they need a concise Russian executive brief from a PDF report, study, strategy document, presentation, or scan. It is intended for one-page management summaries with key findings, discussion questions, and source-grounded numbers, not for translating documents or answering ad hoc questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local job state can contain copies of the source PDF, extracted or OCR text, fact records, and generated output files.

Mitigation: Use the skill only for PDFs appropriate for local processing, and remove the job state when the platform or user no longer needs it.

Risk: An executive summary can mislead readers if numbers are invented, rounded, copied from the wrong page, or produced after script failures.

Mitigation: Follow the scripted fact registry and summary build checks; if the scripts cannot run or validation fails, report the failure instead of hand-building a replacement summary.

Risk: OCR quality can be limited for unsupported or poor-quality scans, including Russian scans when the Cyrillic OCR model is unavailable.

Mitigation: Review OCR warnings and avoid presenting unreadable pages as verified source material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iirtegova/skills/pdf-rezume)
- [summary_canon.md](artifact/references/summary_canon.md)

## Skill Output:

**Output Type(s):** [Files, JSON, Text, Guidance]

**Output Format:** [PDF summary file with JSON script responses; optional HTML copy only when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow stores local job state, including the copied source PDF, extracted or OCR text, fact records, and generated outputs until the platform or user removes them.]

## Skill Version(s):

1.3.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
