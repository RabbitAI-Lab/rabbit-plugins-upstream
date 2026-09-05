## Description:

小红书"免费课程/证书"分享笔记生产工作流。筛课打分 → 素材拼图 → 证书姓名打码(中文OCR+嵌入图同步修复) → 竖版封面 → 文案初稿 → 发布 checklist 一站式产出。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External creators and agent users use this skill to evaluate free course or certificate topics, assemble screenshots, redact certificate identity details, create vertical cover images, draft Xiaohongshu copy, and prepare a publication checklist.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Redaction verification crops can contain sensitive certificate or account information.

Mitigation: Use a private temporary verification directory, inspect crops locally, and delete them before sharing or archiving the workspace.

Risk: In-place image edits can overwrite useful originals or make a failed redaction harder to recover from.

Mitigation: Avoid --inplace unless backups exist, and keep original certificate screenshots separate from generated publication assets.

Risk: Image/OCR dependencies affect redaction accuracy and reproducibility.

Mitigation: Install dependencies in a virtual environment from trusted package sources and manually review every redacted image before publication.

## Reference(s):

- [Course Screening Guide](references/course-screening.md)
- [ClawHub Skill Page](https://clawhub.ai/bonniegeng-max/skills/free-course-share)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated image-file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and tesseract; image helpers may produce stitched images, redacted certificate images, verification crops, and vertical cover images.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
