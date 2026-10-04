## Description:

Sequence stops for a field route.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Field-service dispatchers and operations teams use this skill to sequence stops from supplied location data and receive a route plan with estimated leg and total distances.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Route inputs may expose sensitive customer location details.

Mitigation: Provide only the stop IDs and coordinates needed to plan the route; omit unnecessary customer information.

Risk: Straight-line distance estimates may not reflect actual road travel.

Mitigation: Verify the proposed stop order and travel distances against real road conditions before dispatch.

## Reference(s):

- [Field Route Sequencer on ClawHub](https://clawhub.ai/wxt-ai/skills/field-route-manifest-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Route plan includes the route ID, ordered stop IDs, leg distances in kilometers, and total distance in kilometers.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
