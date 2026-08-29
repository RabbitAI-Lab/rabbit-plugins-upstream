## Description:

Software implementation planning with file-based persistence (.plan/). Use when planning code changes touching 3+ files or with ambiguous scope. Skip for typos, single-file fixes, and research/scanning/audit work that produces reports rather than code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this workflow to decide when implementation planning is warranted, create persistent planning artifacts, and hand off approved multi-phase code changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scaffold script can create or update local .plan/ files and add .plan/ to .gitignore.

Mitigation: Review repository state before running the scaffold script and inspect generated planning files before relying on them.

Risk: Optional execution handoff can route an approved plan into later agent implementation work.

Mitigation: Review the plan, scope boundaries, and acceptance checks before approving subagent-driven or inline execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-planning)
- [Execution and methodology](references/execution-and-methodology.md)
- [Operational patterns](references/operational-patterns.md)
- [Plan deepening](references/plan-deepening.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown planning documents and conversational guidance with optional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create or update .plan/task_plan.md, .plan/findings.md, .plan/progress.md, and .gitignore when the scaffold script is run.]

## Skill Version(s):

4.4.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
