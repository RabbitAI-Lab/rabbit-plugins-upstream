## Description:

stellar-trail defines a six-phase agent workflow with persistent cross-session memory checkpoints, visible audit markers, validation gates, and optional local scripts for compliance checks, repository snapshots, skill healing, vault sync, and task-file exploration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hoshiyomix](https://clawhub.ai/user/hoshiyomix)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their operators use this skill to enforce a structured response lifecycle across conversations, including classification, clarification, planning, implementation, validation, reporting, and cross-session memory handoff. It is most relevant where an operator wants strict workflow discipline and persistent project-state recovery cues across agent sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to activate broadly across agent sessions and persist self-reactivation cues into project logs.

Mitigation: Install only in a disposable or clearly owned environment where this persistent workflow behavior is desired, and review generated memory or log entries before relying on them.

Risk: Optional bundled scripts can modify runtime or boot-related project state, including healing skill installs, refreshing snapshots, and syncing vault copies.

Mitigation: Run these scripts only after reviewing the affected paths and use status or check modes before applying state-changing operations.

Risk: The bundled file explorer can serve project files through a local preview path when enabled.

Mitigation: Enable the explorer only for intended local inspection workflows and avoid exposing sensitive project directories through preview access.

## Reference(s):

- [Environment Resilience](references/environment-resilience.md)
- [Ground Base Knowledge](references/ground-base-knowledge.md)
- [Integration](references/integration.md)
- [Integrity Standard](references/integrity-standard.md)
- [Lifecycle Protocol](references/lifecycle-protocol.md)
- [Memory Architecture](references/memory-architecture.md)
- [Phase 1 Input Analysis](references/phase-1-input-analysis.md)
- [Phase 2 Clarification](references/phase-2-clarification.md)
- [Phase 3 Planning](references/phase-3-planning.md)
- [Phase 4 Implementation](references/phase-4-implementation.md)
- [Phase 5 Validation Review](references/phase-5-validation-review.md)
- [Phase 6 Report](references/phase-6-report.md)
- [Task Files Explorer](references/task-files-explorer.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with visible phase and memory markers, plus optional shell commands for bundled local utilities.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce persistent memory notes, project log updates, validation reports, and local utility commands when the operator enables those behaviors.]

## Skill Version(s):

3.5.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
