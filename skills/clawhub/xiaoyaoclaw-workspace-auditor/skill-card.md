## Description:

Audits an OpenClaw workspace locally for directory, task, memory, knowledge-index, and temporary-file issues, then provides severity-graded findings and suggested fixes without changing files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users and workspace maintainers use this skill to identify workspace organization, task progress, memory-log, knowledge-index, and stale-file issues before deciding how to address them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports may expose local file names, paths, modification ages, and selected status or index content when shared.

Mitigation: Choose the scan root carefully and review or redact reports before sharing them.

Risk: Suggested fixes may be unsuitable for a particular workspace.

Mitigation: Review recommendations and obtain user approval before making any changes.

## Reference(s):

- [OpenClaw Workspace Auditor on ClawHub](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-workspace-auditor)
- [Workspace audit design](docs/DESIGN.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance]

**Output Format:** [Severity-graded Markdown report or structured JSON findings with suggested fixes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only local audit; reports file paths and may include status or index details.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
