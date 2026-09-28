## Description:

Создаёт одностраничное PDF-резюме отчёта для руководителя на русском языке с ключевыми выводами, вопросами для обсуждения, встроенным OCR для латиницы и автоматической сверкой чисел с текстом страниц.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iirtegova](https://clawhub.ai/user/iirtegova)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill when a PDF report, study, strategy deck, presentation, or scan needs a one-page Russian executive summary for leadership. It is intended for extracting and formatting document-grounded findings and discussion questions, not for translating PDFs or answering narrow one-off questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill keeps local processing artifacts for each PDF, including extracted text and an HTML copy of the summary.

Mitigation: Use an appropriate local state directory, manage retention according to the document sensitivity, and install only when this local storage behavior is acceptable.

Risk: HTML output may expose the same document-derived content as the PDF summary.

Mitigation: Send or share the HTML copy only when it is specifically needed; prefer the ready PDF output for normal use.

Risk: Incorrect or unsupported summary claims could mislead readers if validation warnings or draft status are ignored.

Mitigation: Review script verdicts, warnings, rejected facts, and draft markings before relying on or distributing the generated executive summary.

## Reference(s):

- [Канон одностраничного резюме для руководителя](artifact/references/summary_canon.md)
- [ClawHub skill page](https://clawhub.ai/iirtegova/skills/pdf-rezume)

## Skill Output:

**Output Type(s):** [text, markdown, PDF, HTML, shell commands, guidance]

**Output Format:** [PDF file with an optional HTML copy, JSON status from helper scripts, and concise user-facing guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill validates numeric claims against extracted page text, processes OCR locally, and marks draft PDFs when checks do not pass.]

## Skill Version(s):

1.3.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
