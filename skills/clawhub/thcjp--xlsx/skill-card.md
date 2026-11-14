## Description:

Supports agent-assisted reading, editing, fixing, and processing of spreadsheet files such as .xlsx, .xlsm, .xltx, .csv, and .tsv.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent users use this skill to automate spreadsheet data processing, conversion, cleanup, and batch-oriented file workflows when a spreadsheet is the primary input or output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad command-execution and vague API or network authority beyond what its spreadsheet purpose clearly scopes.

Mitigation: Require explicit approval before command execution or API/network use, and run the skill with least-privilege filesystem and network access.

Risk: Spreadsheet files may be untrusted or contain sensitive data.

Mitigation: Use only trusted spreadsheets, scan files before processing when appropriate, and avoid sensitive data unless the processing path is understood.

Risk: Generated commands or processing guidance could be incorrect or misleading.

Mitigation: Review proposed commands, file changes, and outputs before applying them to important workbooks or production data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/xlsx)
- [Skill homepage](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON-shaped result examples and optional shell command suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe spreadsheet processing results, execution status, error handling, and generated or modified file workflows.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
