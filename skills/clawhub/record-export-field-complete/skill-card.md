## Description:

Prepares a customer record field, assembles a reporting export row, and writes it locally, with optional delivery to a configured endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and customer-reporting teams use this skill to turn customer record inputs into a local CSV reporting row and, when explicitly configured, submit the result to a delivery endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Customer record export data can be posted to an arbitrary configured HTTP endpoint without additional user confirmation.

Mitigation: Review and approve the delivery destination before running; avoid environments with unintended delivery endpoint or API key variables set.

Risk: Customer reporting rows are appended to a local file even without external delivery configuration.

Mitigation: Use a dedicated output directory and review the records and local storage permissions before running.

## Reference(s):

- [Customer Record Field Prep release](https://clawhub.ai/wxt-ai/skills/record-export-field-complete)

## Skill Output:

**Output Type(s):** [Files, Text]

**Output Format:** [CSV reporting row and JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [JSON includes the prepared field, export row, local file receipt, and delivery outcome.]

## Skill Version(s):

1.2.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
