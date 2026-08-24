## Description:

Sequence stops for a field route.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Field service operations teams use this skill to turn user-supplied GeoJSON stop data into a concise route plan for dispatch coordination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Field-route location data may include sensitive operational locations.

Mitigation: Provide only route data the user is authorized to share with the agent.

Risk: Generated route ordering may be incorrect or incomplete for real-world dispatch constraints.

Mitigation: Have dispatch staff review the route plan before using it for field operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/field-route-manifest-identifier)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Concise route_plan object with route_id, ordered_stops, leg_km, and total_km.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-supplied stops_geojson and does not require credentials or private file access.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
