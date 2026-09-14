## Description:

Generic test-writing discipline for producing behavior-proving tests, improving assertion quality, resisting test anti-patterns, and adding coverage across languages and frameworks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when writing tests, adding coverage, fixing failing tests, or reviewing test quality. It helps agents choose discriminating cases, avoid false-pass assertions, verify regressions, and report what was actually exercised.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can recommend test-infrastructure cleanup or reset actions that would be harmful against shared or production resources.

Mitigation: Review proposed commands and apply destructive cleanup only to local, disposable, or explicitly test-scoped resources.

Risk: Testing guidance may produce incorrect confidence if an agent runs the wrong project command or accepts a skipped, empty, or false-pass suite as evidence.

Mitigation: Confirm the repository's pinned runner, CI command, executed test count, and failure controls before treating results as proof.

## Reference(s):

- [ia-writing-tests Specification](artifact/SPEC.md)
- [Test Design](artifact/references/test-design.md)
- [Regression Proof](artifact/references/regression-proof.md)
- [Test Smells](artifact/references/test-smells.md)
- [Anti-Patterns: Extended Notes](artifact/references/anti-patterns-extended.md)
- [Oracle Smells](artifact/references/oracle-smells.md)
- [Isolation and Sandbox Traps](artifact/references/isolation-and-sandbox-traps.md)
- [False-Pass Oracle Traps](artifact/references/false-pass-oracle-traps.md)
- [Generated-Corpus Techniques](artifact/references/generated-corpus-techniques.md)
- [Test Completion](artifact/references/test-completion.md)
- [Rationalization Table](artifact/references/rationalization-table.md)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, markdown]

**Output Format:** [Markdown with test code, runner commands, and verification summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include test plans, assertion recommendations, narrow and full-suite commands, and concise handoff notes.]

## Skill Version(s):

4.5.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
