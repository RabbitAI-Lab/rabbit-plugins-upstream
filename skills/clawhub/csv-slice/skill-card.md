## Description:

Helps agents inspect local CSV files, select columns, filter or deduplicate rows, and count records using a standard-library Python script.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation all rights reserved

## Use Case:

Developers and other CSV users can ask an agent to preview rows, select columns, filter or deduplicate records, and count data rows without installing third-party Python packages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests Write and WebFetch permissions beyond those needed to inspect CSV files.

Mitigation: Review permissions before installation and limit the agent to local CSV reading and necessary command execution.

Risk: Documentation describes dry-run and --apply file edits that the CSV script does not support.

Mitigation: Use the script's actual --help options and do not assume it can preview or apply file edits.

## Reference(s):

- [ClawHub CSV Slice release](https://clawhub.ai/zhaoxinghua09-cell/skills/csv-slice)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Displays selected CSV rows or counts; JSON mode includes headers, rows, total count, and deduplication count.]

## Skill Version(s):

1.0.3 (source: ClawHub release; bundled SKILL.md says 1.1.0 and manifest.json says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
