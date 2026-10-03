## Description:

Plan the delivery route for an artifact.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

People planning artifact exports use this skill to choose a delivery route from a supplied request, including whether review is needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Request data may contain information unnecessary for a routing decision.

Mitigation: Supply only the request fields needed to choose a route.

Risk: A suggested route could be mistaken for a completed export or an approved delivery decision.

Mitigation: Review the suggested route before acting; the skill does not perform an export.

## Reference(s):

- [Artifact Delivery Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/artifact-export-route-identifier)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [JSON containing a route_mode string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a local route suggestion; does not export or persist an artifact.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
