## Description:

Derive an invoice-match threshold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operations teams use this skill during routine invoice reconciliation to derive a numeric match_threshold from a supplied allowed variance rule.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A returned threshold could be applied to financial workflows without policy or accounting review.

Mitigation: Review the match_threshold before downstream use and confirm it fits the organization's reconciliation policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/invoice-match-threshold-identifier)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Structured response containing match_threshold as a number]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one numeric threshold from the current request's reconciliation_rule.allowed_variance input.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
