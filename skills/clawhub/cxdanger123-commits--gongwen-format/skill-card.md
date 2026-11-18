## Description:

把 Word 或 Markdown 文档一键排版为符合党政机关公文国标的 docx：字体字号行距标题合规、表格美化、图片防裁剪、大纲级别导航层级、Markdown 标题自动映射公文层级并使用 Word 自动编号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[cxdanger123-commits](https://clawhub.ai/user/cxdanger123-commits)

### License/Terms of Use:

MIT-0

## Use Case:

People preparing Chinese government or organizational documents can use this skill to format Word or Markdown content to the documented GB/T layout rules, or to check a Word document and receive a compliance report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports text rewrites that may conflict with the stated text-preservation guarantee.

Mitigation: Review the generated document and report against the original; use a copy and verify text before relying on the result.

Risk: The security assessment says the skill's file access scope is unclear and its scan coverage is partial.

Mitigation: Review the source and limit initial use to non-sensitive copies until the file access scope is understood.

## Reference(s):

- [GB/T 公文格式参数速查表](artifact/references/guobiao-params.md)
- [ClawHub skill release](https://clawhub.ai/cxdanger123-commits/skills/gongwen-format)
- [Publisher profile](https://clawhub.ai/user/cxdanger123-commits)

## Skill Output:

**Output Type(s):** [Files, Markdown]

**Output Format:** [Formatted DOCX documents and Markdown formatting or compliance reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Formatting preserves Word text by default. The --auto-number option can change numbering text, and Markdown heading prefixes may be removed when converted to automatic numbering.]

## Skill Version(s):

1.0.0 (source: target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
