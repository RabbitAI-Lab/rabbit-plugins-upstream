## Description:

Generate Excel formulas from descriptions, explain formulas, diagnose spreadsheet errors, convert formulas across spreadsheet platforms, and provide bilingual Excel reference guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xueyetianya](https://clawhub.ai/user/xueyetianya)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, analysts, and developers use this skill to generate, explain, debug, and adapt Excel, Google Sheets, WPS, and Calc formulas from natural-language spreadsheet tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill keeps a persistent local history of formula and search inputs without clear disclosure or controls.

Mitigation: Disclose the history behavior, make it optional, limit retained entries, sanitize sensitive inputs, and harden local file permissions before routine use on shared or backed-up systems.

Risk: Spreadsheet formulas and search terms may contain business-sensitive information.

Mitigation: Review inputs before use and avoid entering confidential spreadsheet data unless the local history behavior and storage location are acceptable.

## Reference(s):

- [Excel Formula ClawHub page](https://clawhub.ai/xueyetianya/skills/excel-formula)
- [BytesAgain homepage](https://bytesagain.com)
- [tips.md](artifact/tips.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, plain text, shell command output, and CSV or spreadsheet formula snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are usually Chinese or bilingual and may include generated spreadsheet formulas, explanations, troubleshooting steps, conversion notes, quick-reference entries, or CSV template content.]

## Skill Version(s):

2.0.1 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
