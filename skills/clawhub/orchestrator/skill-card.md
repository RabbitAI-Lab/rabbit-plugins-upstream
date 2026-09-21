## Description:

Orchestrator coordinates agent-driven project work by planning and validating SPECs, auditing codebase and harness gaps, decomposing work into GitHub issues, delegating implementation and QA to specialized skills, and rechecking delivery readiness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to coordinate multi-step agent-driven project work, including planning, SPEC validation, codebase audits, issue decomposition, delegation to specialized skills, QA gates, and release-readiness checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has broad orchestration authority for multi-step development workflows, including planning, delegation, GitHub interaction, and project memory updates.

Mitigation: Install it only for projects where this level of coordination is intended, review autonomy settings, and require confirmation before issue closure, commits, PRs, merges, dependency updates, framework updates, or security-sensitive changes.

Risk: Persistent project memory can retain stale, incorrect, or sensitive context across sessions.

Mitigation: Inspect `.claude/memory/` regularly, remove sensitive content, and verify stored task state before resuming work.

Risk: Delegated work can propagate incorrect plans or unsafe instructions if external issues, PRs, diffs, or comments are treated as commands.

Mitigation: Treat external artifacts as untrusted data, use structured metadata where possible, and require human review before executing shell snippets or instructions from external content.

## Reference(s):

- [Orchestrator Delegation Protocol](references/orchestrator-delegation-protocol.md)
- [orchestrator_stats](references/orchestrator_stats.md)
- [ESTADO_ORCHESTRATOR](references/ESTADO_ORQUESTRATOR.md)
- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/orchestrator)
- [Skill metadata repository URL](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code blocks and structured plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write project memory files, SPEC files, issue plans, audit summaries, and validation reports when used inside an agent workspace.]

## Skill Version(s):

1.0.24 (source: server release metadata; artifact frontmatter metadata.version is 2.6.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
