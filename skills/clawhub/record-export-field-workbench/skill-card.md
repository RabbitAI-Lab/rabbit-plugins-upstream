## Description:

Assemble a reporting export row.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and reporting operators use this skill to turn a supplied customer record field into a concise export row for routine reporting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill transforms whatever customer field data is supplied in the current request.

Mitigation: Provide only the record fields needed for the report and avoid unnecessary customer data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/record-export-field-workbench)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or structured text describing an export row object with columns, row_values, and row_digest.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transforms only the record_field object supplied in the current request.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
