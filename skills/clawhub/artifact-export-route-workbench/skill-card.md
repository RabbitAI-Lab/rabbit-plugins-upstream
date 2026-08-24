## Description:

Register an artifact delivery route.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to register an artifact delivery route from route information supplied in the current request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The selected route depends on route information supplied in the active workspace guidance and current request.

Mitigation: Provide only the route information needed for the current task and review the recorded route before relying on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/artifact-export-route-workbench)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Concise recorded_route object with selected_route, candidate_routes, and reason.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses route information supplied in the current request; no credentials, private files, commands, persistence, or external access are requested.]

## Skill Version(s):

1.0.7 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
