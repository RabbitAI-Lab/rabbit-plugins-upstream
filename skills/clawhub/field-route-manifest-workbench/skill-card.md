## Description:

Build a dispatch manifest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Field service operations teams use this skill to turn a supplied ordered route_plan into a concise dispatch_manifest for handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Route plans can contain operationally sensitive location or scheduling details.

Mitigation: Provide only the route-plan details needed to build the dispatch manifest.

Risk: The manifest can only be as accurate as the supplied route_plan values.

Mitigation: Review route_id, ordered_stops, leg_km, and total_km before using the manifest for field-service handoff.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/field-route-manifest-workbench)

## Skill Output:

**Output Type(s):** [text]

**Output Format:** [JSON-compatible object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns dispatch_manifest with manifest_id, route_id, stops, and total_km from the supplied route_plan.]

## Skill Version(s):

1.0.7 (source: artifact/SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
