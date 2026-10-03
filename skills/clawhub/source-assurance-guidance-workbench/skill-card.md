## Description:

Resolves imported field values using source-agreement guidance and records the result locally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teams reconciling imported business fields use this skill to select values under source-agreement guidance and retain a local resolution record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local CSV records may retain resolved business-field values.

Mitigation: Choose a dedicated output directory and avoid sensitive data unless local retention is acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/source-assurance-guidance-workbench)

## Skill Output:

**Output Type(s):** [Structured data, Files]

**Output Format:** [JSON resolution object and local CSV record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the selected value and agreement count; creates a local record in the specified output directory.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
