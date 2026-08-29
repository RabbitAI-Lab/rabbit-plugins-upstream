## Description:

Generic test-writing discipline for writing tests, adding coverage, and fixing failing tests across languages and frameworks, with emphasis on test quality, real assertions, anti-patterns, and rationalization resistance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to plan, write, and review tests that prove behavior, avoid mock-heavy or assertion-light coverage, and resist rationalizations for skipping tests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested database resets, Docker volume teardown, or test commands could be misapplied to production or shared data.

Mitigation: Run destructive reset or teardown commands only against disposable test environments after confirming the active project, database, and container context.

Risk: Generic test-writing guidance can be over-applied without repository or framework context, producing misleading tests or weak assertions.

Mitigation: Use the repository's CI command, checked-in test runner, and any active framework-specific skill as the authority for tooling and conventions; review generated tests for behavior-focused assertions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-writing-tests)
- [Anti-Patterns: Extended Notes](references/anti-patterns-extended.md)
- [Rationalization Table](references/rationalization-table.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands]

**Output Format:** [Markdown guidance with inline code or shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable artifacts are bundled; outputs depend on the repository and test framework being used.]

## Skill Version(s):

4.4.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
