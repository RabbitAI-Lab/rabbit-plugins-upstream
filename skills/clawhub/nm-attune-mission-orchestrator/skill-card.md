## Description:

Orchestrates full project lifecycle by auto-detecting state and routing to the correct phase.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to coordinate project work across brainstorming, specification, planning, and execution phases. It is intended for starting new projects, resuming interrupted workflows, and routing existing project artifacts to the next lifecycle phase.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can reduce user oversight while coordinating multi-phase project work.

Mitigation: Use supervised or full constraints for sensitive repositories, and avoid --auto unless the project risk and required approvals are already clear.

Risk: The skill can write persistent .attune/ state, plan history, feedback, and execution files that may contain project context.

Mitigation: Inspect and clean .attune/ files periodically, especially before sharing a repository or working with sensitive requirements.

Risk: The skill can create GitHub issues for deferred scope items during backlog triage.

Mitigation: Disable or review automatic issue creation with --no-auto-issues or equivalent supervision before enabling external-facing actions.

Risk: The skill delegates to execution and review skills, so downstream behavior depends on those installed skills and their constraints.

Mitigation: Install and review required dependency skills before use, and keep destructive-operation confirmation and proof-of-work checks enabled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-mission-orchestrator)
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON state files, review records, shell command examples, and generated project artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write .attune/ mission state, plan history, feedback JSON, and execution state; may also coordinate GitHub issue creation when enabled.]

## Skill Version(s):

1.9.18 (source: server release metadata; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
