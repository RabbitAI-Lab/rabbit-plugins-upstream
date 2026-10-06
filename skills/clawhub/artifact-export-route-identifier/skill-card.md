## Description:

Plans a delivery route for an artifact from the supplied export request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to select a route mode for an artifact export request, taking restrictions and available routes into account. It recommends a route rather than delivering the artifact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unsuitable route recommendation, particularly for a restricted artifact, could conflict with delivery policy.

Mitigation: Review the route labels and restricted-artifact quarantine recommendation against your business policy before using them.

## Reference(s):

- [Artifact Delivery Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/artifact-export-route-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON object with a route_mode string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Route recommendation only; no delivery or persistence.]

## Skill Version(s):

1.1.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
