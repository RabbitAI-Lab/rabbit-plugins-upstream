## Description:

Use when the user asks to implement an approved SPEC SDD using test-driven development.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement approved SPEC SDD work one requirement or acceptance criterion at a time using a red-green-refactor loop.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill continues through approved SPEC slices without asking for approval between each slice.

Mitigation: Review the SPEC approval status and task plan before invoking the skill, and monitor progress reports during execution.

Risk: The skill communicates progress and questions in Portuguese by default, which may not fit all teams.

Mitigation: Confirm the expected user-facing language before use or adapt the skill instructions for the target team.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/execute-tdd-spec)
- [Publisher profile](https://clawhub.ai/user/afonsoft)
- [Skill metadata repository URL](https://github.com/afonsoft/skills)
- [Tests guidance](tests.md)
- [Mocking guidance](mocking.md)
- [Refactoring guidance](refactoring.md)
- [Deep modules guidance](deep-modules.md)
- [Interface design guidance](interface-design.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown with inline code and command summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-facing progress and questions are in Portuguese by default.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
