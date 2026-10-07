## Description:

Plans an artifact delivery route, writes a local route record, and optionally submits the result to a configured delivery target.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use the skill to select an artifact delivery route, keep a local route record, and optionally submit the record to a configured destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery can submit route results and a local file path to an external HTTP endpoint using an API key without an additional confirmation step.

Mitigation: Review the configured endpoint, transmitted data, and credentials before enabling delivery; leave delivery unconfigured for local-only use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wxt-ai/skills/artifact-export-route-complete)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON route result and delivery receipt, with a local route-plan file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Without delivery configuration, records locally and contacts no external service.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
