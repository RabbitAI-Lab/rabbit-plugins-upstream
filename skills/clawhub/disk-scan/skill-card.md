## Description:

Scans a local directory without changing files and reports its largest files and subdirectories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can inspect a chosen directory to find the files and subdirectories consuming the most disk space before deciding what to clean up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests write and network-capable tools even though its included disk scanner appears read-only.

Mitigation: Review before installation and grant only the minimum tools needed to scan explicit directories; withhold Write and WebFetch unless separately justified.

Risk: The documentation describes an --apply option that the included script does not provide.

Mitigation: Do not rely on the documented --apply behavior; inspect the included script and run scans only on directories you select.

## Reference(s):

- [ClawHub disk-scan release](https://clawhub.ai/zhaoxinghua09-cell/skills/disk-scan)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON scan results; Markdown guidance when used by an agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports total bytes and ranked files and subdirectories within the selected directory.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; artifact frontmatter lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
