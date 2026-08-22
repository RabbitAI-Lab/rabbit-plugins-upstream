## Description:

Merges enterprise Excel, PDF, and image-based report data into unified spreadsheets, fills Word templates, and can generate financial analysis reports with ratios and risk assessment when explicitly requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[merlinbeard000](https://clawhub.ai/user/merlinbeard000)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, finance teams, and business analysts use this skill to consolidate enterprise reports, extract table data from PDFs, fill Word templates, and produce review-ready financial analysis documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial values extracted from scanned PDFs, screenshots, or image-based documents may be misread.

Mitigation: Use original Excel or text-based PDF inputs when available, run the skill's validation checks, and manually verify extracted values before relying on generated reports.

Risk: Generated Excel and Word outputs may contain incorrect mappings, formulas, ratio interpretations, or risk statements.

Mitigation: Review every generated spreadsheet and document, especially changed or blue-marked content, before using it for business decisions.

Risk: Enterprise and financial reports may contain sensitive business information.

Mitigation: Provide only the specific local files needed for the task and remove unnecessary sensitive data before processing.

## Reference(s):

- [Merge Modes Reference](references/merge_modes.md)
- [PDF Table Extraction Guide](references/pdf_extraction.md)
- [Image-Based PDF Handling Guide](references/image_pdf_guide.md)
- [Standard Post-Loan Analysis Report Template](references/standard_report_template.md)
- [ClawHub Skill Page](https://clawhub.ai/merlinbeard000/skills/enterprise-report-merger)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Analysis, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; generated Excel and Word files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local .xlsx and .docx outputs; generated financial values and scanned-PDF extractions require user review.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
