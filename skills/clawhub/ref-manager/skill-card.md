## Description:

Use when the user wants to collect, extract, verify, and import bibliographic references into EndNote from web pages, PDF files, or a folder of PDFs, and to produce an Excel reconciliation sheet with APA citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fangmingqi2005-create](https://clawhub.ai/user/fangmingqi2005-create)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to gather bibliographic metadata from web pages, PDFs, folders of PDFs, or raw APA text, verify DOI-backed records, and prepare EndNote import files plus an Excel reconciliation sheet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-provided PDF files, folders, URLs, and raw citation text, which may include sensitive source material.

Mitigation: Provide only intended files, avoid broad private folders or sensitive internal URLs, and review inputs before running the pipeline.

Risk: The skill fetches web pages and DOI metadata during citation extraction and verification.

Mitigation: Use it only with sources intended for online lookup and review or pin dependencies before repeated use.

Risk: Records without a DOI, with DOI lookup failures, or with DOI values absent from Crossref can remain uncertain.

Mitigation: Keep uncertain records marked for manual confirmation and ask the user to supply missing bibliographic fields before import.

## Reference(s):

- [APA 7th Edition Citation Rules](references/apa-7-rules.md)
- [Crossref API Reference](references/crossref-api.md)
- [EndNote Import Guide](references/endnote-import-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated citation files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces RIS, EndNote XML, Excel reconciliation, and JSON intermediate files in a user-selected output directory.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
