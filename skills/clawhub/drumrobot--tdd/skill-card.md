## Description:

Test-Driven Development guidance for coding and bug fixing, covering the Red-Green-Refactor cycle, test execution workflow, and test design strategies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to apply a strict test-first workflow: write a failing test, make it pass, refactor, and verify relevant test suites before reporting completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases such as "verify" or "not working" may activate a strict test-first workflow when the user did not intend to start TDD.

Mitigation: Use the skill for explicit TDD or test-first requests, or narrow the trigger policy before deployment.

Risk: The workflow can cause an agent to write tests and run project test commands early in a task.

Mitigation: Review planned test edits and command scope, especially in repositories with slow, destructive, or environment-dependent test suites.

## Reference(s):

- [TDD skill page](https://clawhub.ai/drumrobot/skills/tdd)
- [TDD cycle guide](artifact/cycle.md)
- [Test execution guide](artifact/run.md)
- [Test strategy guide](artifact/test-strategies.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands]

**Output Format:** [Markdown guidance with code snippets and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to edit test files and run project test commands as part of a TDD workflow.]

## Skill Version(s):

0.3.2 (source: server release metadata and CHANGELOG.md, released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
