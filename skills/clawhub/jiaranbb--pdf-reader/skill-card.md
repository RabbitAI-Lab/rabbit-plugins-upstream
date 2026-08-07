## Description: <br>
PDF Reader converts local PDF files into Markdown with page markers and JSON quality metrics, using text extraction first and OCR for scanned PDFs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiaranbb](https://clawhub.ai/user/jiaranbb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use PDF Reader to convert local PDFs, including financial reports, filings, papers, and scanned Chinese or English documents, into searchable Markdown for downstream research or reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive PDFs may be converted into Markdown at the chosen output path. <br>
Mitigation: Use the skill only with PDFs you intend to process locally, and review the selected output path before conversion. <br>
Risk: OCR-derived numbers or dates may be inaccurate. <br>
Mitigation: Visually verify important OCR-derived amounts, percentages, and dates against the original PDF before relying on them. <br>


## Reference(s): <br>
- [PDF Reader on ClawHub](https://clawhub.ai/jiaranbb/skills/pdf-reader) <br>
- [Project homepage](https://github.com/Jiaranbb/pdf-reader) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown file with page markers plus one-line JSON quality metrics on stdout] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads a user-selected local PDF and writes Markdown to the user-selected output path.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter, CHANGELOG, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
