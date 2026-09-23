## Description:

Analyze CSV/Excel files with natural language. Get statistics, filter rows, find anomalies, generate summaries, and export results. No pandas needed - uses Python stdlib for lightweight operation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zacjiang](https://clawhub.ai/user/zacjiang)

### License/Terms of Use:


## Use Case:

Developers, analysts, and agents use this skill to inspect CSV files, summarize columns, filter rows, rank numeric values, detect simple z-score anomalies, group data, and export filtered results without installing pandas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release advertises Excel and natural-language support that is not evidenced by the included CSV-only command-line script.

Mitigation: Use it for CSV command workflows and verify any Excel or natural-language workflow before relying on it.

Risk: Filtered exports can write to a user-supplied output path.

Mitigation: Choose non-critical output paths and avoid overwriting important files.

Risk: Exported CSV values are not neutralized for spreadsheet formula injection.

Mitigation: Treat exports from untrusted data as untrusted and sanitize formula-like cells before opening them in spreadsheet applications.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zacjiang/skills/csv-analyzer)
- [ClawHub publisher profile](https://clawhub.ai/user/zacjiang)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and CSV output files when export is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Python standard-library CSV processing; filtered exports may overwrite an output path supplied by the user.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
