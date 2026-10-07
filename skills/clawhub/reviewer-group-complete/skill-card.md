## Description:

Selects a reviewer group for a request, records the assignment locally, and optionally submits it to a configured delivery endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams use this skill to assign reviewer groups to business requests, save approval records, and optionally register them with a configured service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery may submit approval records to an external endpoint without a separate confirmation step.

Mitigation: Review or unset delivery-related environment variables and credentials; configure a trusted endpoint only when submission is intended.

Risk: The skill writes approval records to the selected local directory.

Mitigation: Use a dedicated output directory and review stored records before sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/reviewer-group-complete)
- [Usage and delivery configuration](artifact/README.md)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON result and local approval record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Result includes the selected reviewer group, recorded group, local record receipt, and delivery status.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
