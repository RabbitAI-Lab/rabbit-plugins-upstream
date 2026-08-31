## Description:

Supports software implementation planning with optional file-based persistence for requests that need a durable record of unresolved architecture or scope decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this workflow to decide when planning is warranted, produce implementation plans or inline checklists, and preserve recovery state for multi-phase software work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Invoking the scaffold script creates local .plan/ planning files and may update .gitignore.

Mitigation: Run the scaffold only in the intended repository and review the resulting files before committing or sharing related work.

Risk: Planning files may contain implementation details, project context, or decisions that are not meant for external audiences.

Mitigation: Review generated plans before sharing them outside the project team.

Risk: Using --force can replace an existing incomplete task plan.

Mitigation: Use --force only after deciding that the new plan should supersede the existing incomplete work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-planning)
- [Skill specification](SPEC.md)
- [Execution and decomposition patterns](references/execution-and-methodology.md)
- [Operational patterns](references/operational-patterns.md)
- [Plan deepening](references/plan-deepening.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown plans, inline checklists, and shell commands for scaffolding local planning files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create .plan/task_plan.md and add .plan/ to .gitignore when the scaffold script is invoked.]

## Skill Version(s):

4.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
