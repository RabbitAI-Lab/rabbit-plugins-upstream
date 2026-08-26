## Description:

CSV解析与生成帮助代理按RFC 4180解析和生成CSV，处理引号、分隔符、编码、数字日期格式和Excel兼容问题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data analysts, and external agent users can use this skill for CSV parsing, generation, validation, cleanup, and cross-tool compatibility with spreadsheet and Python workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is flagged as suspicious because it includes API-key and command-execution guidance that is broader than a local CSV task requires.

Mitigation: Review the skill before installing, avoid providing API keys unless a specific service and scope are documented, and execute generated commands only after human review.

Risk: The skill claims Excel formula-injection handling, but the security guidance says not to rely on that claim by itself.

Mitigation: Apply independent CSV export sanitization for cells that could be interpreted as formulas before opening files in spreadsheet tools.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/csv)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code blocks and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated CSV content, Python snippets, validation guidance, and export recommendations.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
