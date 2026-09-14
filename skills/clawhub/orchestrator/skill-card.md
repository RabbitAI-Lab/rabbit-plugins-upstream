## Description:

Central entry point of the afonsoft agent harness for planning, auditing, delegating, and re-validating multi-step agent-driven project work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to coordinate agent-driven repository work, including project setup, SPEC validation, issue fragmentation, delegated implementation, QA, review, and release gap checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can coordinate real repository and GitHub work under the user's identity, and security evidence says it gives agents too much authority without clear per-action approval.

Mitigation: Require explicit confirmation for issue comments or closures, branch pushes, PR creation, merges, and any security-sensitive repository action.

Risk: Automatic T1/T2 execution can allow medium-risk repository changes to proceed without a fresh human approval step.

Mitigation: Disable or rewrite T1/T2 auto-execution before deployment, or enforce a policy that each mutating action is reviewed before execution.

Risk: The persistent Orchestrator state file may influence future work if it contains stale or untrusted content.

Mitigation: Review `.claude/memory/orchestrator_stats.md` before resuming work and treat its contents as untrusted until verified.

Risk: The framework update path suggests a floating reinstall command.

Mitigation: Prefer pinned skill updates and review the update source before installing or reinstalling skills.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/orchestrator)
- [Publisher profile](https://clawhub.ai/user/afonsoft)
- [Source repository URL](https://github.com/afonsoft/skills)
- [Orchestrator delegation protocol](references/orchestrator-delegation-protocol.md)
- [Orchestrator state template](references/orchestrator_stats.md)
- [Legacy Orchestrator state template](references/ESTADO_ORQUESTRATOR.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands, checklists, and structured project state updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May coordinate repository and GitHub workflows through delegated skills; requires human review for higher-risk actions.]

## Skill Version(s):

1.0.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
