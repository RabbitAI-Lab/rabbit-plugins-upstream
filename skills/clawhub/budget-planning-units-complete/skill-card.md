## Description:

Calculates a campaign-planning amount from a planning note, records the result locally, and optionally delivers it to a configured destination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and campaign-planning teams use this skill to calculate a budget amount from a planning note and create a local ledger entry, with optional delivery to a configured destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery can automatically submit finance-planning results to an external endpoint without a separate confirmation.

Mitigation: Leave delivery configuration unset for local-only use; before enabling delivery, review the destination and payload handling.

## Reference(s):


## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON result and local finance-planning ledger entry]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes calculation, local-artifact, and delivery receipts; external delivery is optional.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
