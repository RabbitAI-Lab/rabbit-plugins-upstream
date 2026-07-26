## Description: <br>
Review Chinese engineering and construction documents in DOCX, text-based PDF, XLSX, or XLSM format, extracting project facts, contacts, schedules, quantities, safety measures, missing items, conflicts, and review questions into a local, traceable pre-review report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lantianbaicai](https://clawhub.ai/user/lantianbaicai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and project reviewers use this skill to locally extract evidence from Chinese engineering and construction documents, then prepare a checklist of confirmed facts, schedules, quantities, safety excerpts, conflicts, missing items, and questions for human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reviewed engineering documents and extracted text may contain customer, contact, pricing, project, or commercially sensitive details. <br>
Mitigation: Use a controlled local output folder, consider --skip-extracted-text for sensitive material, and redact reports before sharing. <br>
Risk: The skill performs pre-review and extraction only; its output is not a regulatory compliance finding or professional engineering approval. <br>
Mitigation: Have a qualified human confirm revisions, names, roles, dates, quantities, safety measures, and any statement affecting construction, cost, schedule, or liability. <br>
Risk: Unsupported, scanned, damaged, password-protected, or poorly structured documents can produce missing, ambiguous, or incomplete extraction results. <br>
Mitigation: Convert legacy formats, run OCR for scanned PDFs, preserve source files, and mark unreadable or conflicting values as pending confirmation. <br>


## Reference(s): <br>
- [Review Rules](references/review-rules.md) <br>
- [Output Schema](references/review-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown report, structured JSON fields, optional XLSX table, and local extracted text files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs local extraction for one source file at a time and can omit Excel output or extracted text when requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
