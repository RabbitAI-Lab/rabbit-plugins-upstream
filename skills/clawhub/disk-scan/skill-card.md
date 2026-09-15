## Description:

Disk-scan helps an agent run a local, read-only disk usage scan that reports the largest files and subdirectories, with optional JSON output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, and operators use this skill to identify local disk space consumers by scanning a chosen directory and reviewing top files and subdirectory size rankings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence reports confusing write-capable documentation for a bundled scanner that appears read-only.

Mitigation: Treat --apply and backup references as documentation defects unless a future version clearly declares write behavior and safeguards.

Risk: Security guidance flags unpinned global install and default-branch Git instructions.

Mitigation: Prefer a pinned ClawHub release or reviewed commit and verify the publisher/source before installing or running locally.

Risk: A recursive local filesystem scan can expose sensitive path names or file-size metadata in copied output.

Mitigation: Scan only intended directories and review text or JSON output before sharing results outside the local environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/disk-scan)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON disk-usage summaries, with Markdown command examples in the skill guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Top-N file and subdirectory rankings from a local recursive scan]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
