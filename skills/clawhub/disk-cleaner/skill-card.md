## Description:

Cross-platform disk space analysis and cache cleaning for Windows, macOS, and Linux, with platform detection, cache discovery, safety tiering, and user-confirmed deletion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liyumingben](https://clawhub.ai/user/liyumingben)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to inspect disk usage and clean regenerable or clearly classified caches across Windows, macOS, and Linux. It is suited for disk-full situations, package-manager cache cleanup, temporary-file cleanup, and identifying large cache-like directories before deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cleanup paths and defaults can permanently delete unrelated or persistent user data.

Mitigation: Run a dry-run scan first and review every selected path, size, and tier before confirming deletion.

Risk: Forced cleanup and recycle-bin emptying reduce the chance to recover accidentally selected data.

Mitigation: Avoid --force and use --no-trash unless recycle-bin cleanup is intentional.

Risk: Electron app storage, logs, developer caches, and symlinked cache directories need extra scrutiny.

Mitigation: Check those paths carefully before selection and skip any item whose purpose or target path is unclear.

## Reference(s):

- [Disk Cleaner ClawHub Page](https://clawhub.ai/liyumingben/skills/disk-cleaner)
- [Cleanup Catalog](references/cleanup-catalog.md)
- [Platform Paths](references/platform-paths.md)
- [Python Downloads](https://www.python.org/downloads/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Code]

**Output Format:** [Markdown guidance with shell command examples; JSON output is available from the cleanup script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can produce a read-only scan, an interactive deletion plan, or machine-readable JSON depending on the selected command flags.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
