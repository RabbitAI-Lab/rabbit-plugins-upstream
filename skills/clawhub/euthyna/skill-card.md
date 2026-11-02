## Description:

Provides an evidence-driven workflow for auditing code security findings, validating suspected vulnerabilities through six gates, and downgrading unsupported claims to observations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modusensus](https://clawhub.ai/user/modusensus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to audit code, changes, and suspected vulnerabilities with measured evidence and explicit validation gates. It keeps unsupported conclusions classified as observations rather than confirmed findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reproduction commands or exploit demonstrations can affect the environment being audited.

Mitigation: Review the separate CLI before installation, approve each exact reproduction command, and use a disposable test environment without sensitive data.

Risk: Locally saved audit reports may contain sensitive findings.

Mitigation: Store audit reports locally with access restricted to people authorized to review the findings.

## Reference(s):

- [Fact Contract](references/fact-contract.md)
- [Dependency Audit](references/dependency-audit.md)
- [Change Audit](references/change-audit.md)
- [Verification Gates](references/verification-gates.md)
- [Bug Classes](references/bug-classes.md)
- [Meta Mechanisms](references/meta-mechanisms.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Evidence-backed Markdown audit reports with measurements and, when appropriate, reproduction sketches or approved commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Claims without sufficient evidence remain observations rather than confirmed findings.]

## Skill Version(s):

0.9.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
