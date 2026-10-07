## Description:

Assembles a reporting export row from a supplied customer record field.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Customer reporting staff and their agents use the skill to turn a supplied record field into a reporting export row, append it to a local CSV, and optionally deliver it to a configured endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The export row may be sent to a configured external delivery endpoint.

Mitigation: Review the endpoint and API key handling before running; leave delivery settings unset when only local assembly is intended.

Risk: Running the skill appends customer reporting data to a local CSV.

Mitigation: Check the output directory and confirm that local export storage is appropriate for the data.

## Reference(s):

- [Reporting Export Assembler on ClawHub](https://clawhub.ai/wxt-ai/skills/record-export-field-workbench)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON export row and local CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes columns, row values, and a row digest; runs may also return a local effect receipt and, when configured, a delivery receipt.]

## Skill Version(s):

1.1.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
