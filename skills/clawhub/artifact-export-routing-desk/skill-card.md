## Description:

Plans an artifact delivery route and records the selected route in a local route plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace operators use this skill to plan an artifact delivery route and record a local route plan. The local record does not confirm an external delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the downstream step creates a local route-plan record in the chosen output directory.

Mitigation: Use a dedicated writable output directory and review the resulting record.

Risk: The request JSON may contain sensitive information if private files are supplied.

Mitigation: Do not pass sensitive private files unless they are needed for the routing task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/artifact-export-routing-desk)
- [Artifact Export Routing Desk README](artifact/README.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Route string, JSON route decision and local JSON receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The downstream step writes a route-plan receipt in a caller-selected output directory; no external delivery is confirmed.]

## Skill Version(s):

3.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
