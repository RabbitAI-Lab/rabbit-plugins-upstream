## Description:

Translates PDFs while preserving document layout and producing bilingual and translated-only versions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and other document users translate papers, guidelines, and reports from PDFs while retaining layout. The skill also supports batch translation, document triage, and optional editable Word output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch mode may follow symlinks outside the selected folder and transmit those documents for translation.

Mitigation: Batch-process only trusted folders and avoid symlinks; review the input set before running.

Risk: Document text is sent to the configured translation provider.

Mitigation: Choose an endpoint approved for the documents' sensitivity; do not submit confidential, legal, medical, or business documents unless external processing is acceptable.

Risk: An API key stored in the local configuration file may be exposed to other local users.

Mitigation: Protect the configuration file with user-only permissions or supply the key through a protected environment.

Risk: OCR-based translations of scanned PDFs are preview quality and can contain recognition errors.

Mitigation: Have a human check translations before formal use; do not rely on scanned-document output for clinical or submission decisions.

## Reference(s):

- [Doc Holmes on ClawHub](https://clawhub.ai/docsor1212/skills/doc-holmes)
- [Publisher homepage](https://skillhub.cn)
- [Document triage criteria](artifact/references/triage.md)
- [Batch translation rules](artifact/references/batch-iron-rules.md)
- [Engine compatibility](artifact/references/engine-matrix.md)

## Skill Output:

**Output Type(s):** [Files, Markdown, JSON]

**Output Format:** [Translated PDF or optional editable DOCX, with JSON audits and Markdown/HTML batch reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces bilingual and translated-only PDFs; scanned-document translations are marked preview quality.]

## Skill Version(s):

2.8.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
