## Description:

Combines plan the delivery route for an artifact with register an artifact delivery route.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams and developers use this skill to plan and record delivery routes for workspace artifacts so routine project deliverables follow consistent export handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An external tool implementation connected to the named operations could exceed the documented artifact-route planning and recording scope.

Mitigation: Confirm connected implementations remain limited to the documented advise_export_route and record_export_route behavior before deployment.

Risk: Incorrect route guidance could send workspace artifacts through the wrong delivery workflow.

Mitigation: Review the returned route_mode or recorded_route against active workspace guidance before acting on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/artifact-export-route)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [guidance, text]

**Output Format:** [Text response with operation-specific output fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Planning returns route_mode; recording returns recorded_route.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
