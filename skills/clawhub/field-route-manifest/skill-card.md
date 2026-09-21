## Description:

Combines sequence stops for a field route with building a dispatch manifest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Field service coordinators and operations teams use this skill to order service stops into a route plan and turn the ordered route into a dispatch manifest for handoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Field-service stop and location data may be sensitive operational information.

Mitigation: Use the skill only in runtimes approved to process the provided stop and location data.

Risk: Runtime tools bound to sequence_service_stops or create_dispatch_manifest may add behavior outside this documentation-only artifact.

Mitigation: Review the external tool bindings in the deployment runtime before installation or use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/field-route-manifest)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown route plans and dispatch manifests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a route_plan from stops_geojson and a dispatch_manifest from the ordered route_plan.]

## Skill Version(s):

1.0.7 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
