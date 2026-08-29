## Description:

Orchestrates the full project lifecycle by auto-detecting state and routing to the correct phase.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to start or resume multi-phase project work, moving from brainstorming through specification, planning, and execution based on existing project artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create GitHub issues for deferred backlog items during phase transitions.

Mitigation: Review or disable automatic GitHub issue creation before use, and require confirmation for external-facing actions.

Risk: The skill persists mission state, plan history, review feedback, errors, and trust data under .attune files.

Mitigation: Inspect .attune files before sharing or committing them, and keep them out of shared repositories when they contain project history or review feedback.

Risk: Broad autonomy directives and --auto mode can reduce routine checkpoints during project execution.

Mitigation: Avoid broad autonomy directives on sensitive projects and keep safety checkpoints for destructive operations, external-facing actions, scope expansion, and budget overruns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-mission-orchestrator)
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline commands and JSON state schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update project artifacts, .attune state files, plan feedback history, and GitHub issues when enabled.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter says 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
