## Description:

Helps maintainers, QA engineers, contributors, and product teams plan useful unit tests, improve coverage, and verify changes against regression risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, maintainers, open-source contributors, and product teams use this skill to turn testing and coverage goals into practical implementation steps, checklists, code changes, and verification notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger terms may activate the skill during general testing or quality discussions.

Mitigation: Use explicit skill invocation when this workflow is desired, and invoke a narrower skill when the task is outside unit-test coverage work.

Risk: Generated test plans or code changes may miss project-specific behavior or introduce misleading coverage improvements.

Mitigation: Review proposed tests against the codebase's expected behavior and run the project's existing test and coverage commands before relying on the result.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [Unit Test Coverage Helper README](README.md)
- [Writing Great Unit Tests: Best and Worst Practices](https://segmentfault.com/a/1190000009709754)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with optional code blocks, shell commands, checklists, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are tailored to the user's codebase context and should state assumptions, limits, and remaining follow-up work when helpful.]

## Skill Version(s):

0.20260811.40534 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
