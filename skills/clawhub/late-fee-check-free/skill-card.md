## Description:

Checks Chinese tax late-payment surcharge calculation tables by recomputing row arithmetic, cross-checking totals, detecting duplicate or missing entries, and citing source rows for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill to validate late-payment surcharge tables during month-end close, reconciliation, inventory, or tax repayment review. It helps check arithmetic consistency and completeness, but its results should not be treated as tax or legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake arithmetic and table-validation results for tax or legal advice.

Mitigation: Present results as calculation and consistency checks only, and have tax decisions reviewed against the relevant authority or professional advice.

Risk: The artifact documentation mentions anonymous usage statistics, while the security evidence notes that inspected code does not show a network call.

Mitigation: Review runtime behavior before deployment where telemetry policy matters, and use the tool only when a local Chinese-language late-fee table checker is needed.

Risk: The free version intentionally omits several advanced checks listed by the artifact.

Mitigation: Review the reported checks-not-run list and do not treat a clean result as coverage of omitted or out-of-scope tax determinations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/late-fee-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Human-readable console text or structured JSON findings with cited source rows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs local table checks on user-provided text or JSON input; reports insufficient input instead of inferring missing facts.]

## Skill Version(s):

1.0.38 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
