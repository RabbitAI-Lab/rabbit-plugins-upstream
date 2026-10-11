## Description:

Translates PDFs while preserving layout and offers bilingual and translation-only PDFs, document triage, and batch processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Readers, researchers, and developers use this skill to triage and translate PDFs while retaining figures, formulas, and page layout, including batches of documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document text, OCR text, and optional extracted terms may be sent to the translation endpoint you configure.

Mitigation: Use an endpoint that meets your privacy requirements; avoid sensitive documents unless its handling is acceptable, or use offline direct mode when appropriate.

Risk: AI-assisted translation and scanned-PDF OCR can introduce errors, especially in formal or sensitive materials.

Mitigation: Have a human review translations before formal use; treat scanned-PDF outputs as preview quality and do not use them for submissions or clinical decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/doc-holmes)
- [SkillHub homepage](https://skillhub.cn)
- [Document triage criteria](references/triage.md)
- [Engine and endpoint compatibility](references/engine-matrix.md)
- [Batch processing rules](references/batch-iron-rules.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance, JSON reports, and PDF documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bilingual or translation-only PDFs; optional batch audit and summary report.]

## Skill Version(s):

3.0.0 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
