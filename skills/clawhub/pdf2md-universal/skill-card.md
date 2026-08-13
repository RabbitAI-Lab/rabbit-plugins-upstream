## Description:

Converts text-based or scanned PDFs into structured Markdown and reports estimated token savings for downstream AI reading, archiving, or knowledge-base ingestion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shiyan521](https://clawhub.ai/user/shiyan521)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and AI-heavy document workflows use this skill to turn reports, financial filings, papers, ebooks, and scanned PDFs into Markdown before feeding them to an AI system or storing them in a knowledge base.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanned-PDF OCR can use an external vision adapter, which may expose confidential document content.

Mitigation: Use --ocr none or a trusted local OCR tool for sensitive PDFs, and treat remote OCR as document upload unless the adapter proves otherwise.

Risk: The BAILIAN_ADAPTER environment variable or --bailian-adapter option points the workflow at Python code that is imported during OCR.

Mitigation: Only configure adapter paths that come from trusted, reviewed code and a provider approved for the documents being processed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/shiyan521/skills/pdf2md-universal)
- [README](README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown file with a text token comparison report and command-line guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can run in estimate-only mode; scanned-PDF OCR may be limited to the first 50 pages.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
