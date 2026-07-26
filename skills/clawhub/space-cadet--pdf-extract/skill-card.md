## Description: <br>
Extracts text, tables, and structured content from PDF files with pdfplumber or PyMuPDF, including page selection and page-delimited output for analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and analysts use this skill to extract local PDF text, tables, or selected pages before search, analysis, or summarization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on an existing ~/.openclaw/workspace/pdf-tools helper that is not shipped or proven by the artifact. <br>
Mitigation: Review and trust the local helper before use, and verify the referenced virtual environment and PDF extraction tools before running commands. <br>
Risk: Extracted PDF text can contain confidential or regulated information. <br>
Mitigation: Limit extraction to intended files and pages, and avoid writing sensitive output to shared temporary files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/space-cadet/skills/pdf-extract) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and extracted plain text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Page-delimited text output with optional page and extraction-method selection.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
