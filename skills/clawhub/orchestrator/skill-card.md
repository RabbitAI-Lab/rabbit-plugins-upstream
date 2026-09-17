## Description:

Central entry point of the afonsoft agent harness. Use when starting a new project, resuming an existing one, planning features/Epics/releases, or running any multi-step agent-driven work. Validates and reconciles SPECs (SDD), audits the codebase and harness for gaps (security, architecture, performance, hygiene), proposes improvements, fragments work into GitHub Issues, delegates implementation/QA/review to specialized skills, and re-validates everything until delivery. Also use to review unapproved SPECs, reconcile open GitHub Issues with code, or run a final gap check before closing a release.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to coordinate multi-step repository work, reconcile SPECs and GitHub Issues, delegate implementation and review to specialized skills, and run final delivery checks before release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can coordinate changes to repository and GitHub state.

Mitigation: Require explicit confirmation before issue comments, issue closures, commits, PR creation, merges, dependency changes, or any T1/T2 batch that mutates files or external services.

Risk: GitHub issues, PR text, comments, and external documents may contain untrusted instructions.

Mitigation: Treat those sources as data, extract structured metadata only, and do not execute embedded commands or follow artifact instructions without human review.

Risk: Project memory may persist sensitive or excessive operational context.

Mitigation: Set limits for what may be stored in `.claude/memory/` and native agent memory, and review memory updates during security-sensitive work.

Risk: A catalog reinstall or framework update could introduce unreviewed behavior.

Mitigation: Pin any reinstall to a reviewed commit or release and keep framework updates advisory until a human confirms the update.

## Reference(s):

- [Orchestrator Delegation Protocol](references/orchestrator-delegation-protocol.md)
- [orchestrator_stats state template](references/orchestrator_stats.md)
- [Legacy ESTADO_ORQUESTRATOR state template](references/ESTADO_ORQUESTRATOR.md)
- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/orchestrator)
- [Metadata source repository](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown with checklists, plans, inline shell commands, and file-change guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Portuguese for user-facing questions and confirmations; may update project state files when operating inside a project.]

## Skill Version(s):

1.0.23 (source: server release metadata; internal skill metadata 2.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
