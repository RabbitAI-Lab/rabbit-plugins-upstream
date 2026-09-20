## Description:

Stellar Trail defines an always-on six-phase execution protocol with cross-session memory practices for agent responses, including classification, clarification, planning, implementation, validation, reporting, checkpointing, restore, compression, and handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hoshiyomix](https://clawhub.ai/user/hoshiyomix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to impose a structured response lifecycle and persistent memory discipline across ordinary work sessions. It is suited to workflows that intentionally require explicit phase markers, validation gates, restore checks, and session handoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is overbroad and attempts to shape every agent response with an always-on workflow and memory discipline.

Mitigation: Install only when that behavior is intentional, and review the documented disable controls before deployment.

Risk: Optional boot-hook, explorer, snapshot, vault, and self-heal scripts can affect local persistence, repo archives, and background-service behavior.

Mitigation: Review those scripts before use and avoid deploying them unless their local state and service effects are understood.

Risk: Persistent memory practices may retain session context across boundaries.

Mitigation: Use the documented memory deletion controls when persistent context is not appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hoshiyomix/skills/stellar-trail)
- [Ground Base Knowledge](references/ground-base-knowledge.md)
- [Lifecycle Protocol](references/lifecycle-protocol.md)
- [Memory Architecture](references/memory-architecture.md)
- [Environment Resilience](references/environment-resilience.md)
- [Task Files Explorer](references/task-files-explorer.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands, configuration]

**Output Format:** [Markdown responses with phase and memory markers, plus optional shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes optional local scripts for validation gates, self-heal checks, repo snapshots, vault sync, and a task files explorer.]

## Skill Version(s):

3.5.4 (source: server release evidence and artifact integrity.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
