## Description:

Build a dispatch manifest from an ordered field-service route plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Field-service dispatchers and operations teams use this skill to turn an ordered route plan into a dispatch manifest for handoff. It saves a local manifest and can deliver it when a target is configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive route or customer-stop data may be sent to a configured web endpoint without clear per-run confirmation.

Mitigation: Review the route data and delivery destination before running; leave delivery settings unset for local-only output, or configure only an approved endpoint and credentials.

## Reference(s):

- [Dispatch Manifest Builder on ClawHub](https://clawhub.ai/wxt-ai/skills/field-route-manifest-workbench)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON dispatch manifest with local artifact and delivery receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes route ID, ordered stops, leg distances, and total distance; delivery receipt is returned when configured.]

## Skill Version(s):

1.1.1 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
