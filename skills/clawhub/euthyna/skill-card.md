## Description:

euthyna provides a security-audit decision discipline and delivery gates for reviewing code, pull requests, changes, or existing vulnerability claims using deterministic facts and six verification gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modusensus](https://clawhub.ai/user/modusensus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security engineers, and code reviewers use this skill to audit repository changes, dependency surfaces, and vulnerability claims before delivery. It helps separate measured facts from judgment, classify findings as true positives, false positives, or inconclusive, and avoid treating missing data as a clean result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit workflows may run target-repository tests, proof-of-concept commands, or verification commands.

Mitigation: Run audits in a disposable, secret-free sandbox and review commands before execution.

Risk: Reports can be misleading if missing measurements are treated as clean results.

Mitigation: Record unavailable measurements explicitly as not evaluated and avoid presenting them as evidence of safety.

Risk: Audit report output paths may be ambiguous during file generation.

Mitigation: Choose an explicit report output path before running workflows that write audit artifacts.

## Reference(s):

- [Bug Classes](references/bug-classes.md)
- [Change Audit](references/change-audit.md)
- [Dependency Audit](references/dependency-audit.md)
- [Fact Contract](references/fact-contract.md)
- [Fact Producers](references/fact-producers.md)
- [Meta Mechanisms](references/meta-mechanisms.md)
- [Verification Gates](references/verification-gates.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown audit reports with structured findings and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires concrete file:line evidence and may write an audit report file before gate validation.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
