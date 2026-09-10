## Description:

Generic test-writing discipline for producing high-quality behavioral tests with real assertions, rationalization resistance, and coverage guidance across languages and frameworks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when writing tests, adding coverage, fixing failing tests, or reviewing test quality. It helps agents choose discriminating cases, use realistic fixtures, avoid weak mocks and tautological assertions, and report verification honestly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated test changes could encode weak assertions, unreviewed golden-output updates, or misleading green results.

Mitigation: Review generated tests as normal code changes, require discriminating assertions, and confirm that bug reproducers or absence checks can fail for the intended reason.

Risk: Repository test commands and realistic fixtures can affect databases, snapshots, integration services, or other persistent test assets.

Mitigation: Run commands in the repository's intended test environment, use isolated temporary fixtures where practical, and inspect changes to golden files, snapshots, databases, and integration fixtures before acceptance.

## Reference(s):

- [Test design](references/test-design.md)
- [Regression proof](references/regression-proof.md)
- [Test smells](references/test-smells.md)
- [Extended anti-patterns](references/anti-patterns-extended.md)
- [Oracle smells](references/oracle-smells.md)
- [Isolation and sandbox traps](references/isolation-and-sandbox-traps.md)
- [False-pass oracle traps](references/false-pass-oracle-traps.md)
- [Generated-corpus techniques](references/generated-corpus-techniques.md)
- [Test completion](references/test-completion.md)
- [Rationalization table](references/rationalization-table.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown prose with test plans, code snippets, and shell command recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include test case designs, assertions, fixture guidance, verification results, failures, skipped checks, and known omissions.]

## Skill Version(s):

4.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
