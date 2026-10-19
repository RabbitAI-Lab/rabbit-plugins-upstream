## Description:

Guides evidence-based security audits of code and changes, requiring verification before suspected vulnerabilities become findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modusensus](https://clawhub.ai/user/modusensus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to audit repositories, changes, or suspected vulnerabilities and document evidence-backed conclusions in a written report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit instructions are available only in Chinese.

Mitigation: Use a Chinese-speaking reviewer or verify a translation before relying on the workflow.

Risk: Audit and proof-of-concept verification may run commands against a repository.

Mitigation: Review each proposed command, obtain explicit approval, and prefer an isolated environment for proof-of-concept checks.

Risk: Unavailable measurements could be mistaken for a clean audit.

Mitigation: Mark unmeasured checks as unevaluated and do not present them as evidence of safety.

## Reference(s):

- [euthyna on ClawHub](https://clawhub.ai/modusensus/skills/euthyna)
- [Verification gates](artifact/references/verification-gates.md)
- [Change audit](artifact/references/change-audit.md)
- [Fact producers](artifact/references/fact-producers.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Markdown audit report with evidence and verification steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are classified as true positive, false positive, or inconclusive; unsupported claims remain observations.]

## Skill Version(s):

0.8.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
