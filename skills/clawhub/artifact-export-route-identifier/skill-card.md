## Description:

Plan the delivery route for an artifact.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to choose a concise route mode for a workspace artifact delivery or export request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The selected route mode may be incorrect for the user's business process because the skill returns a concise routing label rather than performing delivery or access-control checks.

Mitigation: Review the route_mode output for business correctness before using it to drive artifact delivery decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/artifact-export-route-identifier)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [String]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a concise route_mode value for the supplied export_request.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
