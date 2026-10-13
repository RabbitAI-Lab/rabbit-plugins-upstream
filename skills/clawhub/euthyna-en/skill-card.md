## Description:

Guides evidence-based security audits of code, changes, and vulnerability claims through measured facts, verification gates, and a final report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modusensus](https://clawhub.ai/user/modusensus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to audit code or changes, assess suspected vulnerabilities, and deliver reports that distinguish verified findings from observations and unevaluated criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit reports are written to local disk and may contain sensitive code or findings.

Mitigation: Choose a secure report path and review access before sharing the file.

Risk: Some audit checks rely on a separately installed command-line tool.

Mitigation: Review the tool before installing it and mark unsupported checks as not evaluable rather than clean.

Risk: Verification and proof-of-concept commands may execute on the user's machine.

Mitigation: Review the exact commands, obtain explicit approval, and use a sandbox when possible.

## Reference(s):

- [ClawHub release](https://clawhub.ai/modusensus/skills/euthyna-en)
- [Claim verification gates](references/verification-gates.md)
- [Change audit](references/change-audit.md)
- [Dependency audit](references/dependency-audit.md)
- [Fact producers](references/fact-producers.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown audit report with cited evidence and reproduction steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a local report file and distinguishes verified findings, rejected claims, and inconclusive checks.]

## Skill Version(s):

0.7.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
