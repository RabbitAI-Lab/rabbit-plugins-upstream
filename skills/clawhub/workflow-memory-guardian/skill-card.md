## Description:

Workflow-Memory Guardian defines a mandatory five-phase execution protocol and persistent memory lifecycle for agents so work can be classified, clarified, planned, executed, reported, and restored across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hoshiyomix](https://clawhub.ai/user/hoshiyomix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to apply a structured execution workflow and cross-session memory discipline to project work. It is intended for agents that should preserve task state, user decisions, artifacts, and next steps between sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Always-on persistent memory can restore or retain project context across interactions without enough scoping or user controls.

Mitigation: Use the skill only where persistent memory is intentional, and configure opt-in activation, per-project storage paths, retention limits, and clear inspect, correct, and delete procedures.

Risk: Unchanged installation on shared machines or sensitive projects could expose unrelated prior context to later chats.

Mitigation: Avoid unchanged deployment in shared or sensitive environments; isolate memory storage by project and user before enabling the protocol.

Risk: Mandatory clarification and checkpoint behavior can conflict with quick-response expectations or with tasks that should not preserve state.

Mitigation: Document when the protocol applies, provide an explicit disable or narrow-scope path, and record user-approved overrides as durable decisions.

## Reference(s):

- [Integration - Interlock Deep-Dive, worklog, Task IDs, Edge Cases](references/integration.md)
- [The 95% Integrity Standard - Manifest, Formula, Recall Check](references/integrity-standard.md)
- [Lifecycle Protocol - M0-M3 Detailed Procedures](references/lifecycle-protocol.md)
- [Memory Architecture - Files, Templates, Write Rules](references/memory-architecture.md)
- [Phase 1 Reference - Input Analysis](references/phase-1-input-analysis.md)
- [Phase 2 Reference - Clarification Proposal](references/phase-2-clarification.md)
- [Phase 3 Reference - Planning](references/phase-3-planning.md)
- [Phase 4 Reference - Implementation](references/phase-4-implementation.md)
- [Phase 5 Reference - Report Summary](references/phase-5-report.md)

## Skill Output:

**Output Type(s):** [guidance, text, markdown]

**Output Format:** [Markdown instructions with protocol markers and memory file templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instruction-only; no API calls or executable code.]

## Skill Version(s):

2.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
