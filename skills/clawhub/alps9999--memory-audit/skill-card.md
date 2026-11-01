## Description:

只读扫描 AI 记忆目录与会话日志，评估记忆使用度和索引完整性，并生成分档结果与维护建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[alps9999](https://clawhub.ai/user/alps9999)

### License/Terms of Use:

MIT

## Use Case:

AI assistant users and developers can audit a local memory library to see which entries are used, identify index gaps, and review maintenance suggestions before making changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Report exports can overwrite files in memory, session, or rule folders.

Mitigation: Write reports to a fresh path outside those folders, and avoid shared temporary paths and symlinks.

Risk: Crafted filenames can insert executable content into HTML reports.

Mitigation: Use JSON for directories with untrusted filenames, keep reports private, and review recommendations before changing memories.

## Reference(s):

- [ClawHub release](https://clawhub.ai/alps9999/skills/memory-audit)

## Skill Output:

**Output Type(s):** [Analysis, JSON, HTML report, Maintenance guidance]

**Output Format:** [Text summary with optional JSON or HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only audit; recommendations require human review.]

## Skill Version(s):

1.0.0 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
