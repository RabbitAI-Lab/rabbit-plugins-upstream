## Description:

Derive an invoice-match threshold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Invoice reconciliation teams use this skill to calculate a match threshold from an allowed variance supplied in the current request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An incorrect allowed variance can produce an unsuitable invoice-match threshold.

Mitigation: Review the input JSON before running; supply only a numeric allowed_variance between 0.00 and 0.50 in 0.01 increments.

## Reference(s):

- [Reconciliation Threshold Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/invoice-match-threshold-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Numeric match_threshold between 0.50 and 1.00; no persisted artifact.]

## Skill Version(s):

1.1.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
