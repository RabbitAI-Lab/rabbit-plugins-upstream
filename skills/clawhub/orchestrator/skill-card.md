## Description:

Govern agent-driven projects, audit preconditions, create documentation, turn gaps into GitHub Issues, and coordinate execution, tests, and QA in a continuous loop.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to coordinate software project governance, repository precondition checks, documentation provisioning, GitHub issue fragmentation, implementation loops, testing, QA, and release preparation when working with the afonsoft agent harness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can coordinate broad repository workflows, and the security evidence flags conflicting approval rules around silent changes, PR completion, batching, and merges.

Mitigation: Require explicit human approval before file writes, commits, branch creation, PR publication, or merges; run changes in an isolated branch or worktree and verify tests, lint, and build before integration.

Risk: The skill suggests reinstalling the catalog with an unpinned command.

Mitigation: Verify the package version, source catalog, and commit before running reinstall commands on important projects.

Risk: Issues, PR descriptions, diffs, comments, and external specifications can contain untrusted instructions.

Mitigation: Treat those materials as data, retrieve structured metadata when possible, and use approved project SPEC files and repository state as the source of truth.

## Reference(s):

- [Orchestrator Delegation Protocol](artifact/references/orchestrator-delegation-protocol.md)
- [ESTADO_ORQUESTRATOR](artifact/references/ESTADO_ORQUESTRATOR.md)
- [afonsoft/skills repository](https://github.com/afonsoft/skills)
- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/orchestrator)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with checklists, phase workflows, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-facing questions and confirmations are expected in Portuguese (pt-BR); internal documentation is in English.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
