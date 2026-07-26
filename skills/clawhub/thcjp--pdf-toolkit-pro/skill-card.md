## Description: <br>
PDF工具箱Pro helps agents extract text, tables, and images from PDFs, use OCR, merge, split, rotate, fill forms, annotate, watermark, sign, and generate PDFs from HTML, Markdown, or code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, document operations teams, and agent users use this skill to automate PDF extraction, conversion, form filling, annotation, merging, splitting, and report generation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional callback and cloud OCR paths may expose sensitive PDF contents if used without review. <br>
Mitigation: Keep contracts, financial files, and other sensitive PDFs in local-only workflows unless cloud OCR or callback notifications are explicitly approved. <br>
Risk: The skill expects read, write, and command execution access for document processing and may generate scripts or bulk file outputs. <br>
Mitigation: Review generated commands, scripts, and output paths before execution, especially before bulk edits or writes. <br>
Risk: OCR and table extraction can be inaccurate for low-quality scans, handwriting, complex layouts, or cross-page tables. <br>
Mitigation: Manually verify important extracted text and tables before relying on them for contracts, financial records, or operational decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/pdf-toolkit-pro) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code snippets, shell commands, configuration notes, and file path conventions for generated PDF artifacts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or describe generated files such as extracted text, CSV or Excel tables, images, filled PDFs, annotated PDFs, merged PDFs, split page directories, metadata JSON, and helper scripts.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact frontmatter says 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
