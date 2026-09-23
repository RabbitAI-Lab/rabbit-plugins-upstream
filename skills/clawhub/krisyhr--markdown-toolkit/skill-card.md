## Description:

Markdown 排版工具箱用于格式化中文混排、转换微信公众号和小红书格式、生成目录、检查链接和标题层级。

This skill is ready for commercial/non-commercial use.

## Publisher:

[krisyhr](https://clawhub.ai/user/krisyhr)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and documentation authors use this skill to format Chinese and English Markdown, convert trusted Markdown to WeChat-ready HTML, convert Markdown tables and CSV, generate a table of contents, count words, and extract links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The WeChat HTML conversion can preserve unsafe markup from untrusted Markdown.

Mitigation: Use HTML conversion only on trusted Markdown and review or sanitize generated HTML before opening it in a browser or publishing it.

Risk: Generated output files may overwrite previous generated files with the same derived name.

Mitigation: Run the formatter on copies or check for existing generated filenames before writing output.

## Reference(s):

- [Markdown 中文排版规则](artifact/references/format-rules.md)
- [ClawHub skill page](https://clawhub.ai/krisyhr/skills/markdown-toolkit)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands]

**Output Format:** [Markdown, HTML, CSV, and plain text, often with shell commands for the Python formatter.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write generated files next to the source file with derived filenames.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
