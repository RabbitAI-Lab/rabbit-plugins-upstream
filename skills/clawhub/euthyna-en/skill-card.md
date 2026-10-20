## Description:

Guides evidence-based code security audits, verifies vulnerability claims against six gates, and downgrades unsupported findings to observations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modusensus](https://clawhub.ai/user/modusensus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to audit repositories and code changes or verify suspected vulnerabilities with reproducible evidence, explicit uncertainty, and a checked report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit and verification commands may execute untrusted project code or tests.

Mitigation: Review exact commands and obtain approval before verification or PoCs; use a sandbox where possible.

Risk: Audit reports and repository history may expose sensitive security details.

Mitigation: Choose a restricted report destination and review its contents before sharing.

Risk: Missing audit tools or measurements can leave security criteria unassessed.

Mitigation: Mark unavailable checks as not evaluable rather than reporting a clean result.

## Reference(s):

- [ClawHub release: euthyna (English)](https://clawhub.ai/modusensus/skills/euthyna-en)
- [Verification gates](references/verification-gates.md)
- [Change audit](references/change-audit.md)
- [Dependency audit](references/dependency-audit.md)
- [Fact producers](references/fact-producers.md)
- [Fact contract](references/fact-contract.md)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Shell commands]

**Output Format:** [Markdown audit report with code citations and reproduction commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records findings, inconclusive checks, and criteria not evaluated; writes a report file.]

## Skill Version(s):

0.8.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
