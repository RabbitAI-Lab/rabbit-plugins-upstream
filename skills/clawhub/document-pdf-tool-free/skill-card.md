## Description: <br>
PDF文档工具（免费版） helps agents extract text and tables from PDFs, create, merge, split, watermark, encrypt, and OCR PDF documents for personal workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to have an agent handle single PDF tasks such as text extraction, table extraction, PDF creation, merging, splitting, watermarking, encryption, and OCR. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read PDF contents, write output files, install common Python dependencies, and run PDF-processing commands. <br>
Mitigation: Install and run it only in trusted workspaces, review proposed commands before execution, and keep PDF inputs and outputs scoped to the intended project directory. <br>
Risk: The optional callback_url parameter could send processing results or document-derived data to an external destination. <br>
Mitigation: Use callback_url only with trusted endpoints and avoid callbacks for sensitive documents unless the destination is approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/document-pdf-tool-free) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional code blocks, shell commands, and structured JSON-style results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write output files and may use optional callback URLs when requested by the user.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
