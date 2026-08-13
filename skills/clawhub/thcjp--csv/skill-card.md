## Description:

CSV解析与生成 helps agents parse, clean, validate, and generate RFC 4180-compatible CSV data, including quoting, delimiter, encoding, date, numeric, and Excel-compatibility handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data analysts, and other external users use this skill to have an agent read, validate, clean, transform, and generate CSV content for workflows involving Excel, Google Sheets, pandas, and similar tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may suggest file writes or command execution while helping parse or generate CSV data.

Mitigation: Approve writes and commands only for intended CSV paths and review proposed changes before execution.

Risk: The artifact mentions API keys and callback URLs generically, which could be mistaken for required setup.

Mitigation: Treat API-key and callback references as generic documentation unless a specific workflow requires them.

Risk: CSV files can contain sensitive or business-critical data.

Mitigation: Review CSV contents and destination paths before sharing, transforming, or writing files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/csv)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with Python and shell examples; generated or transformed CSV text or files when approved.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Markdown-only skill. File writes and command execution should be approved for intended CSV paths.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
