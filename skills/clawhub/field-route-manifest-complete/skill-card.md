## Description:

Sequences field-service stops into a route plan and dispatch manifest, saves the manifest locally, and optionally delivers it to a configured destination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Field-service dispatchers and developers use the skill to sequence location-based stops, prepare a dispatch manifest, and optionally submit or send it to a configured destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive route or dispatch details may be sent to an unintended endpoint when delivery settings are present.

Mitigation: Review delivery configuration before running; remove generic DELIVERY_ENDPOINT and DELIVERY_API_KEY variables unless external submission is intended.

Risk: Local dispatch records may be written to an unintended or shared location.

Mitigation: Use a dedicated, access-controlled output directory for route and dispatch records.

## Reference(s):

- [Field Route Sequencer on ClawHub](https://clawhub.ai/wxt-ai/skills/field-route-manifest-complete)

## Skill Output:

**Output Type(s):** [Structured data, Files]

**Output Format:** [JSON response and local JSON dispatch manifest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a route plan, dispatch manifest, local file receipt, and delivery status; external delivery is optional.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
