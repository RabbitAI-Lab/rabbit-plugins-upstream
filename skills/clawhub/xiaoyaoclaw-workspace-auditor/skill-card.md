## Description:

OpenClaw Workspace Auditor performs read-only local health checks on OpenClaw workspaces for directory structure, task progress files, memory logs, knowledge-base indexing, and temporary or large files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw workspace maintainers use this skill to inspect local workspace hygiene and receive prioritized findings with suggested fixes without automated changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad audit or health-check requests may invoke the skill on an unintended workspace.

Mitigation: Specify the intended workspace path or root before running the scan.

Risk: Reports can expose local file paths, filenames, and workspace hygiene details.

Mitigation: Review report content before sharing it outside the local workspace.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-workspace-auditor)
- [OpenClaw Workspace Auditor Documentation](https://github.com/dtsola/xiaoyaoclaw-workspace-auditor)
- [OpenClaw Setup Guide](https://www.yuque.com/dtsola/igp1aa/adcicbai2zlem0bz)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown report by default, with optional JSON output and suggested shell commands for user-approved fixes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only local scanner; configurable workspace root, stale-age threshold, and large-file threshold.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
