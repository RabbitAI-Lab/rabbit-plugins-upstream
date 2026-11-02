## Description:

Provides stack-agnostic guidance for writing tests, adding coverage, and fixing failing tests, with an emphasis on meaningful assertions and avoiding common test anti-patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill when writing tests, expanding test coverage, or fixing failing tests. It helps them choose cases that detect plausible regressions and verify behavior through observable outcomes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cleanup examples using TRUNCATE, DROP DATABASE, or docker compose down -v can delete data.

Mitigation: Before applying these commands, verify that the database and Compose volumes contain only disposable test data.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/iliaal/skills/compound-eng-writing-tests)
- [Skill instructions](artifact/SKILL.md)
- [Test design](artifact/references/test-design.md)
- [Regression proof](artifact/references/regression-proof.md)
- [Test smells](artifact/references/test-smells.md)
- [False-pass oracle traps](artifact/references/false-pass-oracle-traps.md)
- [Isolation and sandbox traps](artifact/references/isolation-and-sandbox-traps.md)
- [Test completion](artifact/references/test-completion.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown guidance with code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Repository- and language-specific; no fixed output length.]

## Skill Version(s):

5.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
