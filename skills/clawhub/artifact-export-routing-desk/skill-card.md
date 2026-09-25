## Description:

Advise export routes and register artifact delivery decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace operators use this skill to plan artifact delivery routes and record the selected route for routine artifact export workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may choose the wrong stage when a request is unclear about whether to plan a route or register one.

Mitigation: Confirm whether the user wants route planning or route registration before applying the skill.

Risk: Incorrect route guidance could affect a business artifact delivery workflow.

Mitigation: Review the selected route before using it in downstream delivery or export processes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wxt-ai/skills/artifact-export-routing-desk)

## Skill Output:

**Output Type(s):** [text, guidance, configuration]

**Output Format:** [Plain text and structured object fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces route_mode as a string and recorded_route as an object with selected_route, candidate_routes, and reason.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
