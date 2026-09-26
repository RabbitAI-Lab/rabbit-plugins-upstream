## Description:

Translates PDFs through a user-configured translation service while preserving document layout and producing bilingual and translated PDF outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, translators, and other document users translate academic papers, guidelines, and reports while retaining PDF layout. Batch processing supports resume and per-file reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document text is sent to the configured translation service.

Mitigation: Use an endpoint authorized for the documents being translated and review its data-handling terms.

Risk: A local API key or configuration file could be exposed to others on a shared machine.

Mitigation: Use your own API key and keep local configuration private.

Risk: External PDF and OCR tools, or binaries selected through environment settings, may be untrusted.

Mitigation: Install pdf2zh-next and tesseract from trusted sources and avoid environment-specified binary paths on shared or untrusted machines.

Risk: OCR translations of scanned PDFs may contain errors.

Mitigation: Treat tier-C results as preview quality and have a person check translations before formal use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/doc-holmes)
- [Publisher homepage](https://skillhub.cn)
- [Triage guidance](artifact/references/triage.md)
- [Engine compatibility](artifact/references/engine-matrix.md)
- [Batch processing guidance](artifact/references/batch-iron-rules.md)

## Skill Output:

**Output Type(s):** [Shell commands, PDF files, JSON reports, HTML reports]

**Output Format:** [Markdown guidance and local PDF, JSON, and HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bilingual and translated PDFs; batch audit and status reports; scanned-PDF results marked preview quality.]

## Skill Version(s):

2.1.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
