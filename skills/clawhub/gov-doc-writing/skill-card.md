## Description:

此技能用于创建符合中国政府及央企规范的 Word 文档（.docx），适用于公文、国央企文档、规范文书和正式报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[a-lhliang](https://clawhub.ai/user/a-lhliang)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, document authors, and agents use this skill to generate .docx files that follow Chinese government and state-owned enterprise formatting conventions, including title, heading, body, table, image, attachment, signature, and page-number styles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dependency version ranges can make installs less reproducible.

Mitigation: Pin the docx dependency exactly before deployment.

Risk: Example imports use an absolute local skill path that may not exist in another environment.

Mitigation: Adjust the require path to the installed skill path before running examples.

Risk: The document generator writes a .docx file to the requested output path.

Mitigation: Choose explicit output paths and review whether an existing file would be overwritten.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/a-lhliang/skills/gov-doc-writing)
- [Publisher profile](https://clawhub.ai/user/a-lhliang)
- [SKILL.md](artifact/SKILL.md)
- [Document creation script](artifact/scripts/create_gov_doc.js)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, files, guidance]

**Output Format:** [Markdown guidance with JavaScript snippets and Node.js commands; generated documents are .docx files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write a local .docx file to the requested output path.]

## Skill Version(s):

1.12.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
