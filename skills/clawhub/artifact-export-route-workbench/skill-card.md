## Description:

Register an artifact delivery route.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to select and record a local artifact delivery route from supplied route guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied route preferences can affect later delivery-path decisions.

Mitigation: Review route_mode against workspace guidance before relying on the recorded route.

Risk: The helper writes a route-plan record to the supplied output directory.

Mitigation: Use a dedicated writable workspace directory and review the resulting record.

## Reference(s):

- [Artifact Delivery Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/artifact-export-route-workbench)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the selected route, candidates and reason; writes a local route-plan JSON file and reports a receipt. No external delivery is confirmed.]

## Skill Version(s):

1.1.0 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
