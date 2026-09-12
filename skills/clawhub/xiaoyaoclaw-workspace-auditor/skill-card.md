## Description:

OpenClaw Workspace Auditor is a read-only local workspace health auditor that scans directory structure, task progress, memory logs, knowledge-base indexing, and temporary-file hygiene, then reports severity-graded findings with fix suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw workspace maintainers use this skill to inspect a local agent workspace for structure, progress, memory, knowledge-base, and temporary-file issues before deciding on manual fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The auditor traverses the workspace path supplied by the user and may summarize local file structure and health findings.

Mitigation: Run it only against the intended OpenClaw workspace and review the report locally; release evidence states the skill is read-only and does not send data out.

Risk: Fix suggestions may not match every team's workspace conventions.

Mitigation: Review suggested fixes before acting; the artifact states the skill reports issues and does not modify, delete, or move files.

## Reference(s):

- [OpenClaw Workspace Auditor GitHub Documentation](https://github.com/dtsola/xiaoyaoclaw-workspace-auditor)
- [OpenClaw Workspace Auditor ClawHub Release](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-workspace-auditor)
- [XiaoYaoClaw Documentation](https://www.yuque.com/dtsola/igp1aa/adcicbai2zlem0bz)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown report or JSON report with severity-graded findings and fix suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only local inspection; no external API calls or network use according to release evidence.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
