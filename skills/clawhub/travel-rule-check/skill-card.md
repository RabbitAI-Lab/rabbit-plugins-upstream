## Description:

Checks virtual-asset transfers for missing sender and beneficiary identity, account or address, and geographic details using a local travel-rule precheck.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and compliance teams use this local checker to screen virtual-asset transfers for missing originator and beneficiary details before human regulatory review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A screening result could be mistaken for a legal compliance determination.

Mitigation: Treat results as a preliminary check, not legal advice; confirm applicable requirements with qualified compliance reviewers.

Risk: Transaction and KYC details may contain sensitive personal information.

Mitigation: Provide only data authorized for processing and limit access to screening inputs and results.

Risk: Broad compliance triggers and tool permissions could cause unintended activation.

Mitigation: Limit activation to explicit travel-rule checks and restrict agent tools to those needed for local execution.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/travel-rule-check)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or structured JSON screening result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exit code 0 for a passing check, 1 for missing details, and 2 for missing or invalid input.]

## Skill Version(s):

1.0.4 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
