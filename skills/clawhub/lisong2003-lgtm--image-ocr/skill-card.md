## Description:

本机OCR图片/扫描PDF；不上传，装模型/依赖才联网。触发词：OCR、文字识别、表格。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

开发者和需要从截图、照片或扫描 PDF 中提取内容的用户可用它在本机识别文字、数字、表格、代码和算式，并按需要导出为文本或结构化格式。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial and noted a source-code portability checker in an OCR skill, with some tool-misuse analysis incomplete.

Mitigation: Review the checker and scripts before use, limit file and shell access to what the OCR task requires, and consider a complete scan before installation.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/lisong2003-lgtm/skills/image-ocr)
- [图签字段映射](references/title-block-schema-map.md)
- [故障排查](references/troubleshooting.md)
- [功能清单](references/feature-log.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, CSV, JSON, JSONL]

**Output Format:** [纯文本、Markdown 表格、CSV、代码块、JSON 或 JSONL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [可包含置信度、坐标和需人工核对标记；复杂合并表格及低质量或手写图像需人工复核。]

## Skill Version(s):

0.4.0 (source: SKILL.md frontmatter, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
