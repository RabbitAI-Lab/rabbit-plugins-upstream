## Description:

Audits an OpenClaw workspace for directory, task, memory, knowledge-index, and temporary-file issues and recommends fixes without changing files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users and developers can inspect workspace organization, task progress, memory logs, knowledge indexing, and stale files before deciding whether to make changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports can expose local workspace file names and paths.

Mitigation: Review reports before sharing them outside the workspace.

Risk: Cleanup suggestions may be inappropriate for a particular workspace.

Mitigation: Review each suggestion and explicitly approve changes before acting on it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-workspace-auditor)
- [Workspace auditor design](docs/DESIGN.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance]

**Output Format:** [Severity-graded Markdown report or structured JSON findings with suggested fixes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only inspection; skipped checks are identified when prerequisites are absent.]

## Skill Version(s):

1.0.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
