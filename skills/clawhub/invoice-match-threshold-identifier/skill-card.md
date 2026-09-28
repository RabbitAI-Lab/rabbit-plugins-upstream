## Description:

Derive an invoice-match threshold from a supplied allowed variance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations teams use this skill to calculate a numeric match threshold for invoice reconciliation from a supplied allowed variance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running local code with sensitive or unrelated inputs.

Mitigation: Review the package before running it; supply only the declared reconciliation_rule field, without credentials or private directories.

Risk: Using a computed threshold without checking its suitability for a reconciliation decision.

Mitigation: Review the supplied variance and resulting threshold against the applicable reconciliation policy before use.

## Reference(s):

- [Reconciliation Threshold Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/invoice-match-threshold-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON object containing a numeric match_threshold]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Computes a result without persisting a business artifact.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
