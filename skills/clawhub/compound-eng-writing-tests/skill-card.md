## Description:

Generic test writing discipline: test quality, real assertions, anti-patterns, and rationalization resistance. Use when writing tests, adding test coverage, or fixing failing tests for any language or framework. Complements language-specific skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill when writing, improving, or repairing tests across languages and frameworks. It helps produce discriminating behavioral tests, avoid false-pass patterns, and review golden or expected-output changes as specification changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may recommend running real project test suites or project-local wrappers that interact with sensitive test infrastructure.

Mitigation: Review proposed commands before execution and use repository-approved test environments, isolation, and credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-writing-tests)
- [ia-writing-tests Specification](artifact/SPEC.md)
- [Anti-Patterns: Extended Notes](artifact/references/anti-patterns-extended.md)
- [False-Pass Oracle Traps](artifact/references/false-pass-oracle-traps.md)
- [Isolation and Sandbox Traps](artifact/references/isolation-and-sandbox-traps.md)
- [Rationalization Table](artifact/references/rationalization-table.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code and command examples when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only skill; no install hooks, credential handling, persistence, or tool calls are declared in server security evidence.]

## Skill Version(s):

4.5.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
