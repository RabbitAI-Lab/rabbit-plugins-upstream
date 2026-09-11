## Description:

Govern agent-driven projects, audit preconditions, create documentation, turn gaps into GitHub Issues, and coordinate execution, tests, and QA in a continuous loop.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to coordinate agent-driven software projects from repository setup through SPEC planning, GitHub issue tracking, implementation delegation, validation, QA, and PR preparation. It is intended for projects that use the afonsoft agent harness and require user-facing questions and confirmations in Portuguese (pt-BR).

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can exercise broad repository and GitHub control, including issue, PR, merge, branch, and worktree operations.

Mitigation: Require explicit human confirmation before closing issues, posting comments, opening PRs, merging branches, creating worktrees, or changing protected branches.

Risk: Issue text, PR descriptions, diffs, comments, and external SPEC documents can contain untrusted instructions.

Mitigation: Treat those sources as data; use approved SPEC files and structured GitHub metadata as the authority for implementation decisions.

Risk: Framework update guidance can lead to unpinned catalog reinstalls.

Mitigation: Verify any framework update by exact commit before reinstalling or accepting a changed skill catalog.

## Reference(s):

- [orchestrator Skill on ClawHub](https://clawhub.ai/afonsoft/skills/orchestrator)
- [afonsoft skills repository](https://github.com/afonsoft/skills)
- [Orchestrator Delegation Protocol](references/orchestrator-delegation-protocol.md)
- [ESTADO_ORQUESTRATOR state template](references/ESTADO_ORQUESTRATOR.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, checklists, file paths, and delegated agent workflow steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coordinates other skills, GitHub issue workflows, state files, validation checkpoints, and Portuguese user-facing confirmations.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata; source skill metadata reports 2.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
