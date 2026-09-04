## Description:

Scans local WeChat received-file folders, organizes files by type or month, deduplicates by content, and generates reports while defaulting to read-only dry-run behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect and organize local WeChat received-file directories across one or more accounts. It is intended for headless, scheduled, or automated file-reporting and copy workflows where users can run a dry-run before applying changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill scans local WeChat received-file folders and may expose file names, paths, account labels, and storage information in reports.

Mitigation: Run the default dry-run first, use --source to restrict the scan to an intended directory, and review report output before sharing it.

Risk: Using --apply or --trash changes local file organization and may move originals to the system trash after copying.

Mitigation: Use --apply only after reviewing the dry-run, confirm the destination directory, and use --trash only when source cleanup is intended; Linux skips trash cleanup rather than permanently deleting files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oracis/skills/wechat-file-organizer)
- [Server-resolved GitHub provenance](https://github.com/oracis/wechat-file-organizer/tree/main/wechat-file-organizer)
- [Project homepage](https://github.com/oracis/wechat-file-organizer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with shell command examples and optional JSON report output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default dry-run prints a local report; --json emits machine-readable accounts and file records; --apply copies organized files; --trash moves originals to the system trash where supported.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
