## Description:

Build executes implementation-plan tasks with a TDD workflow, updating plan progress, running verification, and creating commits at task and phase gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use Build after a planning track exists to execute the next planned task, apply TDD or existing verification commands, update plan progress, and commit completed work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can actively edit repository files, run local commands, update plans, and create commits.

Mitigation: Install it only where that level of build automation is intended, and review status, diffs, test results, and commits before relying on completion.

Risk: Optional cross-session or cross-project search may expose sensitive code or prior work context.

Mitigation: Use those search tools only when their data sources are appropriate for the project and avoid querying sensitive material unnecessarily.

Risk: Rollback guidance can affect user work if broad revert commands are used without inspecting the worktree.

Mitigation: Check git status first and prefer targeted or backed-up reverts over broad checkout-style rollback.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/solo-build)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and repository-change instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update plan files, run local commands, edit project files, and create commits in the target repository.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter reports 2.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
