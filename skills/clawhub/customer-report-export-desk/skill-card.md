## Description:

Prepares a customer record field and assembles a reporting export row.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Customer reporting teams and developers use this skill to prepare a named customer record field and assemble a reporting export row. The downstream operation appends a local CSV export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A local CSV export can retain customer data beyond the reporting task.

Mitigation: Run downstream only on intended records, use a dedicated output directory, and remove the CSV when it is no longer needed.

## Reference(s):

- [Customer Report Export Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/customer-report-export-desk)

## Skill Output:

**Output Type(s):** [JSON, CSV file]

**Output Format:** [JSON result and local CSV export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a record field or export row; downstream appends a local CSV and returns an effect receipt. No external service is contacted.]

## Skill Version(s):

3.0.0 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
