## Description:

Organizes local WeChat received files by scanning FileStorage/File directories, grouping files by type or month, detecting duplicates, and generating reports while remaining read-only by default.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect and organize local WeChat received-file folders, identify duplicate, large, and old files, and optionally copy organized files into a separate output directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill scans local WeChat received-file folders and computes file hashes for duplicate detection.

Mitigation: Run the default dry-run first and use --source to limit scanning to the intended WeChat directory.

Risk: Using --apply copies files into an organized output directory, which may duplicate local data or expose sensitive received files in a new location.

Mitigation: Review the dry-run report before --apply and choose a destination directory with appropriate access controls.

Risk: Using --scan-all or --include-media broadens scanning beyond the default received-file folder behavior.

Mitigation: Enable these options only when broader media-folder scanning is intentional.

## Reference(s):

- [Server-resolved source repository](https://github.com/oracis/wechat-file-organizer/tree/main/wechat-file-organizer)
- [ClawHub skill page](https://clawhub.ai/oracis/skills/wechat-file-organizer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with shell command examples; the bundled script emits terminal text reports or JSON when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default dry-run scans local files and reports counts, size totals, duplicate groups, old files, and largest files; --apply copies organized files to a destination directory.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact SKILL.md and manifest.yaml declare 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
