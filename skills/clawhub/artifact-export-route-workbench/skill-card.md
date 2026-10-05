## Description:

Registers an artifact delivery route, records the choice locally, and optionally submits it to a configured delivery service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents handling artifact delivery use this skill to select an available route and keep a local record of the decision. A configured delivery endpoint can also receive the route data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Route data may be sent to an external service when a delivery endpoint is configured.

Mitigation: For local-only use, unset delivery endpoint variables and review endpoint and API key settings before running.

Risk: The skill writes local route records.

Mitigation: Use a dedicated, writable output directory and review the recorded route.

## Reference(s):

- [Artifact Delivery Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/artifact-export-route-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON route decision and local route record; optional delivery receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the selected route, candidate routes, and a reason.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
