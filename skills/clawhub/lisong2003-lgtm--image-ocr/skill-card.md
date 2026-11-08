## Description:

从图片和扫描 PDF 中提取中文、英文、数字、表格、代码和算式文本，并按需要输出文本、Markdown、CSV 或 JSON。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

适用于需要从截图、照片或扫描 PDF 中读取内容的用户；提取文本、表格、代码和算式，并整理为所需格式。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Language-model downloads and optional dependency repair can make network requests, despite the offline OCR description.

Mitigation: Review setup and language-download steps before use; prepare dependencies and models deliberately, and restrict network access when offline operation is required.

## Reference(s):

- [ClawHub release](https://clawhub.ai/lisong2003-lgtm/skills/image-ocr)
- [Feature log](references/feature-log.md)
- [Tesseract fast language data](https://raw.githubusercontent.com/tesseract-ocr/tessdata_fast/main)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV, Code, JSON]

**Output Format:** [Plain text, Markdown tables, CSV, code blocks, or JSON with coordinates and confidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Low-confidence results are marked for review; complex merged tables are flattened, and full LaTeX layout recognition is unsupported.]

## Skill Version(s):

0.3.7 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
