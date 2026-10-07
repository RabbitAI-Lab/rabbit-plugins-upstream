## Description:

Sequence stops for a field route.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Field dispatchers and service teams use this skill to order stops in a supplied GeoJSON route and estimate distances between them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unrelated private information may be exposed if included in the route input.

Mitigation: Provide only the route data needed for the current request.

Risk: Straight-line distance estimates may not reflect actual road routes.

Mitigation: Check the proposed stop order and travel distances against road conditions before dispatch.

## Reference(s):

- [Field Route Sequencer on ClawHub](https://clawhub.ai/wxt-ai/skills/field-route-manifest-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [route_plan contains route_id, ordered_stops, leg_km, and total_km.]

## Skill Version(s):

1.1.1 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
