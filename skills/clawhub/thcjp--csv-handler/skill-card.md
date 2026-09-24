## Description:

CSV文件处理专家 helps agents detect CSV encoding and delimiters, profile and clean data, merge or split files, convert types, and parse schedule or cost CSVs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data analysts, and operations teams use this skill to inspect, clean, merge, split, convert, and export CSV data for engineering, finance, scheduling, and automation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for an API key without clear need for local CSV processing.

Mitigation: Do not provide or export an API key unless the publisher explains the specific service and purpose; keep secrets out of files and logs.

Risk: Broad activation language could lead the agent to use the skill outside CSV-specific tasks.

Mitigation: Use this skill only for CSV inspection, cleaning, conversion, splitting, merging, schedule parsing, or cost parsing requests.

Risk: Split and export operations can write files to unintended locations or expose sensitive data.

Mitigation: Confirm input files, output directories, filenames, and permissions before running file-writing operations on sensitive data.

Risk: Malformed CSV rows may be skipped during parsing.

Mitigation: Review row counts, sample outputs, and logs before relying on cleaned or converted results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/csv-handler)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON-style result examples and code or shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or create cleaned, merged, split, converted, or exported CSV files when the agent has file access.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 2.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
