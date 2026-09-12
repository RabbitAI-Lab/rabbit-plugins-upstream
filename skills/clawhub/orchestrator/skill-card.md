## Description:

Use when starting or running an agent-driven software project with the afonsoft harness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to coordinate agent-driven software projects, including planning, audit, delegation, GitHub issue and PR workflow, and validation across project phases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent broad GitHub and repository workflow authority with persistent autonomous state.

Mitigation: Use read-only or narrowly scoped GitHub tokens where possible, review state-file changes, and require explicit approval before issue closure, PR publication, merges, dependency updates, framework updates, or changes that affect credentials or security posture.

Risk: Conflicting approval rules could allow project workflow changes to proceed with insufficient supervision.

Mitigation: Apply the documented escalation gates for protected branches, deployments, public exposure, permissions, secrets, domain changes, new features, and architecture shifts.

Risk: Unreviewed issue bodies, PR comments, diffs, or external specifications could contain prompt-injection or unsafe shell instructions.

Mitigation: Treat external text as data, retrieve structured metadata where possible, sanitize command arguments, and do not execute shell snippets from comments or external documents without human review.

## Reference(s):

- [Orchestrator Delegation Protocol](references/orchestrator-delegation-protocol.md)
- [Orchestrator State Template](references/orchestrator_stats.md)
- [Legacy Orchestrator State Template](references/ESTADO_ORQUESTRATOR.md)
- [afonsoft Skills Repository](https://github.com/afonsoft/skills)
- [ClawHub Skill Page](https://clawhub.ai/afonsoft/skills/orchestrator)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown with structured plans, checklists, shell command snippets, and state-file updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project coordination guidance and may update persistent orchestration state files when used by an agent with write access.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
