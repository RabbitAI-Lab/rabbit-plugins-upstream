## Description:

Scans a local directory and reports its largest files and subdirectories without modifying them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0 in release metadata; bundled documents state MIT for Python code and all rights reserved for documentation and theory

## Use Case:

Developers and users investigating disk usage can identify large files and subdirectories before deciding how to reclaim space.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests write and web-fetch authority beyond the read-only disk scan.

Mitigation: Review before installation and limit tool permissions to local read and execution where possible.

Risk: Documentation mentions --apply and write behavior even though the packaged scanner is read-only.

Mitigation: Verify the packaged script and its options before use; do not assume --apply is supported.

Risk: Scanning a directory exposes local file names and sizes to the agent.

Mitigation: Use only where broad local file visibility is acceptable and scope scans to intended directories.

## Reference(s):

- [ClawHub disk-scan release](https://clawhub.ai/zhaoxinghua09-cell/skills/disk-scan)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports total bytes and ranked files and subdirectories; accepts a directory, result limit, and optional JSON output.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata; bundled SKILL.md says 1.1.0 and manifest says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
