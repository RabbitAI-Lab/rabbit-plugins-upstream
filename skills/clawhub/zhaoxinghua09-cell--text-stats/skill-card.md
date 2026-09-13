## Description:

Text Stats provides zero-dependency text and code statistics, including character counts, line counts, top word frequencies, estimated reading time, and directory summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, writers, and agent users use this skill to inspect text or code files and directories for counts, word-frequency summaries, and estimated reading time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented global install command is unpinned.

Mitigation: Review files before installing and prefer a pinned CLI version or pinned Git commit.

Risk: Some documentation describes dry-run and --apply behavior that does not match this read-only script.

Mitigation: Treat the included script as read-only text analysis and verify behavior with --help before relying on copied documentation language.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/text-stats)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON from a Python CLI, with Markdown usage guidance for agents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only file and directory analysis; successful CLI runs exit with rc=0.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and changelog mention 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
