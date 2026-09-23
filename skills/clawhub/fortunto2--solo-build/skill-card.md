## Description:

Execute implementation plan tasks with TDD workflow, auto-commit, and phase gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fortunto2](https://clawhub.ai/user/fortunto2)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to execute implementation-plan tasks, run tests and quality checks, update progress, and create commits through a structured build workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make persistent repository changes and create git commits.

Mitigation: Invoke it only for a specific track or task, and review the repository diff and commit history before and after use.

Risk: The skill can run local build, test, lint, hook-installation, and other shell commands.

Mitigation: Use it only in repositories where autonomous local command execution is acceptable, and inspect configured hooks and workflow files before running.

Risk: Broad trigger phrases can cause the skill to continue across build phases.

Mitigation: Prefer explicit task or track arguments when invoking it, and verify the selected plan before allowing execution to proceed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/fortunto2/skills/solo-build)
- [Publisher Profile](https://clawhub.ai/user/fortunto2)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and code or file changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify repository files, install repository hooks, run local commands, update task progress, and create git commits.]

## Skill Version(s):

2.2.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
