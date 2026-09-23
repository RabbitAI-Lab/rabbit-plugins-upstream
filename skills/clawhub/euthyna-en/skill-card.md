## Description:

euthyna (English) guides agents through evidence-based code security audits by requiring deterministic facts, six-gate claim verification, and downgrades for unsupported conclusions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modusensus](https://clawhub.ai/user/modusensus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to audit code, repositories, pull requests, and suspected vulnerability claims with structured evidence, reproducible checks, and explicit inconclusive states.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit reports may contain sensitive project details.

Mitigation: Choose an approved report location before use and avoid Desktop or temporary paths for confidential projects.

Risk: The workflow references external euthyna CLI and dependency tools.

Mitigation: Run only trusted tool installations and verify tool paths before executing generated commands.

## Reference(s):

- [Defect-class specific requirements](artifact/references/bug-classes.md)
- [Stage B: change audit](artifact/references/change-audit.md)
- [Stage A: dependency audit](artifact/references/dependency-audit.md)
- [The fact contract (adjudication-layer consumption guide)](artifact/references/fact-contract.md)
- [Fact producers: when to run them, how, and how to read the output](artifact/references/fact-producers.md)
- [Meta-mechanisms: six things that make the process actually work](artifact/references/meta-mechanisms.md)
- [Stage C: claim verification (adjudication layer)](artifact/references/verification-gates.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance, Files]

**Output Format:** [Markdown audit reports with inline shell commands and structured finding verdicts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write an audit report file; conclusions are expected to carry evidence and reproducible checks.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
