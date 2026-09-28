## Description:

Plans artifact delivery routes and describes selected and candidate routes from the supplied request and workspace guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace users use the skill to plan an artifact delivery route or describe a selected route with alternatives and a reason. Its response is a recommendation, not confirmation that a delivery system was updated.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A suggested or recorded route may be mistaken for an actual update to a delivery system.

Mitigation: Treat the response as routing guidance and verify any external registration or delivery separately.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wxt-ai/skills/artifact-export-routing-desk)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text string or structured object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [route_mode is a concise string; recorded_route contains selected_route, candidate_routes, and reason.]

## Skill Version(s):

2.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
