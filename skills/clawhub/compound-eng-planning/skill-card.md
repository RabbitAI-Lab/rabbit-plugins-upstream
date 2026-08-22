## Description:

Software implementation planning with file-based persistence (.plan/). Use when planning code changes touching 3+ files or with ambiguous scope. Skip for typos, single-file fixes, and research/scanning/audit work that produces reports rather than code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to turn ambiguous or multi-file software implementation work into concrete, reviewable plans with scoped phases, file responsibilities, verification steps, and execution handoff options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local .plan/ files may contain sensitive project details if the agent records private implementation context.

Mitigation: Use the skill only in workspaces where local planning notes are acceptable, and review .plan/ content before sharing, committing, or exporting workspace files.

Risk: The scaffolding script can update .gitignore to exclude .plan/.

Mitigation: Review .gitignore changes after scaffolding if the workspace has strict repository hygiene or policy controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-planning)
- [Execution & Decomposition Patterns](references/execution-and-methodology.md)
- [Operational Patterns](references/operational-patterns.md)
- [Plan Deepening](references/plan-deepening.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown planning documents with inline shell commands and local workspace file updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create .plan/task_plan.md, .plan/findings.md, and .plan/progress.md, and can add .plan/ to .gitignore when scaffolding is used.]

## Skill Version(s):

4.4.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
