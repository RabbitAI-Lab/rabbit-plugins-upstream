## Description:

批量提取图片文字、标注关键词、生成Word文档。当用户上传带文字的图片（单张或多张）时，自动识别文字，根据用户提供的关键词进行标注加粗，并输出为连续的Word文档格式。适用于学生整理课件重点、文献标注、复习资料制作等场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lilimoss-china](https://clawhub.ai/user/lilimoss-china)

### License/Terms of Use:

MIT

## Use Case:

External users, students, researchers, and editors use this skill to extract Chinese text from one or more uploaded images, bold user-specified keywords, and assemble Word-friendly Markdown output for notes, literature review, and study material preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OCR input images may contain confidential, legal, medical, business, or personal information.

Mitigation: Process only documents the user is authorized to handle and avoid sensitive materials unless the agent environment is approved for that data.

Risk: The optional helper script reads and writes user-specified local file paths.

Mitigation: Use explicit input and output paths and review the destination before running the helper script.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with image-labeled sections, bolded keyword matches, keyword occurrence statistics, and optional shell command guidance for the helper script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains uploaded image order, labels sections as Pic1, Pic2, and so on, and produces Word-friendly text rather than a binary .docx file.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
