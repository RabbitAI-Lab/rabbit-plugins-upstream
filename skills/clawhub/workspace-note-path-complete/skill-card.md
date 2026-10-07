## Description:

Plans a knowledge-base placement path, writes a workspace CSV export, and optionally delivers the result to a configured destination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to derive an archive path from a file request, create a local CSV export, and optionally deliver its record to a configured destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delivery settings can send export metadata and local file paths to an unintended HTTP endpoint.

Mitigation: Use only a trusted, intended delivery endpoint; otherwise clear delivery-related settings to keep the workflow local.

Risk: The workflow writes a local export file.

Mitigation: Run it with a dedicated output directory and review the intended output before use.

## Reference(s):


## Skill Output:

**Output Type(s):** [Files, Structured data]

**Output Format:** [CSV file and JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The response includes the identified path, recorded path, local file receipt, and delivery status.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
