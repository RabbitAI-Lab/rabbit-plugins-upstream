## Description:

Assemble a reporting export row.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Customer reporting teams use this skill to turn a supplied record field into a reporting export row and append it to a local CSV.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied reporting field values are appended to a local CSV in the chosen output directory.

Mitigation: Use a dedicated output directory and avoid shared or sensitive locations unless the export is intended there.

## Reference(s):

- [Reporting Export Assembler on ClawHub](https://clawhub.ai/wxt-ai/skills/record-export-field-workbench)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON export row and locally appended CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The export row includes columns, row values, and a row digest; execution also returns a local file receipt.]

## Skill Version(s):

1.1.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
