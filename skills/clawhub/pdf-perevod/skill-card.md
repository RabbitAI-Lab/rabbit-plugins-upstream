## Description:

Перевод PDF на русский с сохранением исходной вёрстки, графиков и оформления: английский текст заменяется русским прямо на странице. Читает и сканы (встроенный OCR без сети) — на них перевод рисуется поверх картинки.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iirtegova](https://clawhub.ai/user/iirtegova)

### License/Terms of Use:

MIT-0

## Use Case:

External users and document-focused agents use this skill when a user provides a PDF report, study, presentation, or scan and asks for Russian translation while preserving layout, graphics, and formatting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow stores a copy of the source PDF, extracted text, translations, OCR data, and the finished PDF in local state/output folders.

Mitigation: Use it only for PDFs where that local storage and deliverable-copy behavior is acceptable; avoid highly confidential PDFs unless this handling is approved.

Risk: OCR on scanned pages can misread text or numbers, affecting translation accuracy.

Mitigation: Review OCR-derived pages and script warnings before delivering the final PDF, and leave uncertain OCR blocks untranslated when verification is not possible.

Risk: Russian translations can exceed the original layout capacity or trigger unresolved numeric and terminology warnings.

Mitigation: Use the build/status warnings and tight-unit reports to shorten translations and resolve checks before producing the final PDF.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iirtegova/skills/pdf-perevod)
- [Правила перевода делового документа на русский](references/translation_rules.md)

## Skill Output:

**Output Type(s):** [Files, Text, Shell commands, Guidance]

**Output Format:** [JSON script responses and translated PDF files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores source PDF copies, extracted text, translations, OCR data, and generated PDFs in configured local state/output folders; final PDFs may be copied to a user deliverables folder.]

## Skill Version(s):

1.3.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
