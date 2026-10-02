## Description:

Builds a dispatch manifest from an ordered field-service route plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Field-service dispatch teams use an ordered route plan to prepare a manifest of stops and travel distances for handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Route details may be written to a shared or sensitive output directory.

Mitigation: Choose a dedicated, writable output directory appropriate for storing the supplied route plan's manifest.

## Reference(s):

- [Dispatch Manifest Builder on ClawHub](https://clawhub.ai/wxt-ai/skills/field-route-manifest-workbench)
- [wxt-ai publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON dispatch manifest and local JSON file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes manifest ID, route ID, ordered stops and total distance; returns a local file receipt. Does not confirm an external dispatch action.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
