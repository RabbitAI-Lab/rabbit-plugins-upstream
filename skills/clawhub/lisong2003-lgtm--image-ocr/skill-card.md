## Description:

在本地从图片、扫描件和多页 PDF 提取中文、英文、数字、表格、代码及算式，并可输出 Markdown、CSV 或 JSON。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

开发者和日常用户可用此技能从无法直接复制文字的图片或扫描件中提取内容，并将表格或代码整理为可编辑文本。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Model files may be downloaded automatically, so operation may contact the network despite offline-oriented documentation.

Mitigation: For strict offline use, preinstall required models, pass --no-auto-download, and block outbound network access.

Risk: OCR results may remain in a local cache and expose sensitive extracted text to later local access.

Mitigation: Use --no-cache for sensitive work and --clear-cache to remove stored results.

## Reference(s):

- [ClawHub release: 图片文字识别](https://clawhub.ai/lisong2003-lgtm/skills/image-ocr)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV, JSON]

**Output Format:** [Extracted text, Markdown tables, CSV, or line-level JSON with coordinates and confidence information.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally; OCR accuracy varies with image quality, and handwriting-heavy or degraded scans need manual review.]

## Skill Version(s):

0.3.5 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
