## Description:

Calculates a metric trend from CSV data, creates a stakeholder digest, and optionally delivers it to a configured endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use this skill to summarize metric trends and create a local HTML digest for stakeholder reviews. Delivery to a configured service is optional.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional delivery can send business metrics to an untrusted endpoint.

Mitigation: Keep delivery disabled unless needed; use an explicit delivery config and a trusted HTTPS endpoint.

Risk: A delivery API key may be exposed if the destination or redirect behavior is not controlled.

Mitigation: Provide an API key only for a trusted destination with controlled redirects.

Risk: The skill writes a local digest under the selected output directory.

Mitigation: Use a dedicated output directory with appropriate access controls.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [HTML digest file and JSON result with local and delivery receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-only by default; optional configured delivery]

## Skill Version(s):

1.2.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
