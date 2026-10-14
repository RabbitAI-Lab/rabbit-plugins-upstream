## Description:

Guides evidence-based security reviews of code and changes, requiring verification gates before reporting confirmed findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modusensus](https://clawhub.ai/user/modusensus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this Chinese-language workflow to audit code or changes, validate suspected vulnerabilities, and document evidence-backed conclusions. Unverified claims are marked inconclusive or downgraded to observations rather than presented as confirmed findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The separate euthyna CLI and verification commands operate on local repositories and may write report files.

Mitigation: Confirm the CLI's provenance, review exact commands before running them, and obtain approval and use a sandbox for reproduction commands when possible.

Risk: Unmeasured checks or missing evidence could be mistaken for a clean security result.

Mitigation: Mark unavailable measurements as unevaluated and require evidence and gate validation before reporting confirmed findings.

## Reference(s):

- [euthyna on ClawHub](https://clawhub.ai/modusensus/skills/euthyna)
- [Verification gates](references/verification-gates.md)
- [Fact producers](references/fact-producers.md)
- [Fact contract](references/fact-contract.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands]

**Output Format:** [Markdown security audit report with evidence, finding verdicts, and reproduction commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a dated report file; findings distinguish true positives, false positives, and inconclusive cases.]

## Skill Version(s):

0.7.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
