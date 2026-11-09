## Description:

The adjudication discipline and delivery gate for code security audits. Use when the user asks to audit the security of a piece of code, a pull request, a change, or to verify an existing vulnerability claim.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modusensus](https://clawhub.ai/user/modusensus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use the skill to audit code, changes, and vulnerability claims. It gathers deterministic evidence and applies explicit gates so claims without adequate support remain observations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The separate euthyna CLI implementation is outside the inspected skill bundle.

Mitigation: Review the CLI separately before installing or running it; approve exact verification commands and run tests or PoCs in a disposable environment without valuable data or credentials.

## Reference(s):

- [Euthyna (English) on ClawHub](https://clawhub.ai/modusensus/skills/euthyna-en)
- [Bug Classes](references/bug-classes.md)
- [Change Audit](references/change-audit.md)
- [Dependency Audit](references/dependency-audit.md)
- [Fact Contract](references/fact-contract.md)
- [Fact Producers](references/fact-producers.md)
- [Meta Mechanisms](references/meta-mechanisms.md)
- [Verification Gates](references/verification-gates.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands]

**Output Format:** [Evidence-based audit reports with findings or observations, gate results, and reproduction commands; CLI tools also produce JSON or text and optional Mermaid history diagrams.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Claims are tied to evidence; conclusions that do not pass the gates are downgraded to observations.]

## Skill Version(s):

0.10.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
