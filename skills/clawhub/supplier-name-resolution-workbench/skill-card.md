## Description:

Reconciles supplier names using supplied matching guidance and writes a local match report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Purchasing and operations teams use this skill to compare supplier names under supplied matching guidance and record the result for reconciliation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured delivery endpoint can receive reconciliation results and local report paths automatically, without a separate confirmation step.

Mitigation: Leave CLAWHUB_DELIVERY_ENDPOINT and delivery credentials unset unless outbound delivery is intended; review any --delivery-config destination before using supplier data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/supplier-name-resolution-workbench)

## Skill Output:

**Output Type(s):** [JSON, CSV files]

**Output Format:** [JSON match result and delivery receipt, with a local CSV reconciliation report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns matched status, canonical names, and similarity score; includes local report path and delivery status.]

## Skill Version(s):

1.1.1 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
