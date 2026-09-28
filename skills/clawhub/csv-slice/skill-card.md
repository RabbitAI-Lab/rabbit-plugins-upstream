## Description:

Helps agents preview, filter, deduplicate, and count rows in local CSV files using Python's standard library.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and other agents use this skill to inspect local CSV data, select columns, filter or deduplicate rows, and get row counts without installing additional packages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests Write and WebFetch tools beyond what its read-only CSV viewer needs.

Mitigation: Review before installation and remove Write and WebFetch permissions unless they are required.

Risk: Documentation describes --apply and write-to-disk operations that the shipped script does not support.

Mitigation: Check the script's --help output and do not rely on the documented write behavior.

## Reference(s):

- [CSV Slice on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/csv-slice)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON from the CSV viewer; agent instructions in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads local CSV files without writing them; JSON output is available with --json.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
