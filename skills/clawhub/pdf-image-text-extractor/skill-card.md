## Description: <br>
从图片或 PDF 文档中识别并提取文字内容，支持多种图片格式和 PDF 文件，自动判断是否包含文字并保留原始格式输出结构化结果。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Office workers, students, researchers, content creators, and individual users use this skill to extract editable text from images and PDFs while preserving readable structure for copying, review, or Markdown export. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Extracted text may contain sensitive content and may be saved as Markdown when requested. <br>
Mitigation: Process only documents the user intends to analyze and avoid saving extracted Markdown for sensitive contracts, IDs, medical records, or confidential business files unless workspace retention is acceptable. <br>
Risk: Text extraction accuracy can be reduced by unclear images, scanned PDFs, complex layouts, or password-protected PDFs. <br>
Mitigation: Tell users when content is unclear, scanned, complex, or unsupported, and present extracted text as best effort for review before downstream use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/pdf-image-text-extractor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text or JSON from the PDF extraction script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [PDF page text may be separated by Markdown page dividers; extraction quality depends on source document clarity and layout.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
