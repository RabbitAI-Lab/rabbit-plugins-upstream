## Description:

中文课程论文综述写作与排版导出。触发词：算法综述 / 课程论文 / 作业综述 with 小四 + 宋体 + 双倍行距 + docx+pdf 输出要求；GB/T 7714 参考文献排版；学术作业类长文（约 20 页）。流程覆盖参考文献真实性核查、章节大纲、正文写作、docx+pdf 双格式导出。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huanmeng9527](https://clawhub.ai/user/huanmeng9527)

### License/Terms of Use:

MIT-0

## Use Case:

External users and students use this skill to plan, draft, format, and export Chinese coursework review papers that require verified references, GB/T 7714-2015 citations, docx output, and PDF conversion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Academic references may be inaccurate if generated without source verification.

Mitigation: Verify each reference against publisher, DOI, journal, or conference pages and keep a verification log before drafting.

Risk: System-level package installation can affect the user's Python environment.

Mitigation: Use a virtual environment for python-docx and related dependencies instead of system package overrides.

Risk: LibreOffice font substitution settings under ~/.config can affect later document conversions.

Mitigation: Change LibreOffice user configuration only after reviewing the impact, or keep conversion settings isolated for this workflow.

## Reference(s):

- [中文论文排版与导出技术规范](references/formatting-spec.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code and shell commands; generated docx and PDF files when the workflow is executed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided topic, student identity fields, filename, verified references, and outline approval before drafting.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
