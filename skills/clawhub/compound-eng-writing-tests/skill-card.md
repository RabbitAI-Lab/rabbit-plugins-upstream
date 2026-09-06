## Description:

Generic test writing discipline for test quality, real assertions, anti-patterns, and rationalization resistance when writing, adding, or fixing tests across languages and frameworks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to plan, write, and review discriminating behavioral tests, especially when adding coverage, fixing failing tests, or avoiding mock-driven and tautological test suites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated tests or source changes could be incorrect, brittle, or misaligned with the project contract.

Mitigation: Review proposed changes and run the repository's focused and full test commands before accepting them.

Risk: The skill may ask an agent to inspect project files and run test commands as part of normal test-writing work.

Mitigation: Use the repository's checked-in runners and existing sandbox or CI controls, and review command output before treating results as evidence.

## Reference(s):

- [Anti-Patterns: Extended Notes](references/anti-patterns-extended.md)
- [False-Pass Oracle Traps](references/false-pass-oracle-traps.md)
- [Isolation and Sandbox Traps](references/isolation-and-sandbox-traps.md)
- [Rationalization Table](references/rationalization-table.md)
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-writing-tests)
- [Publisher profile](https://clawhub.ai/user/iliaal)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code, command, and configuration examples when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose test files, assertions, focused and full test commands, and review notes tailored to the repository under work.]

## Skill Version(s):

4.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
