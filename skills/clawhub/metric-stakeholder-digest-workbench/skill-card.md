## Description:

Build a stakeholder metric digest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and stakeholders use this skill to turn a structured metric summary into a concise digest for reporting and planning updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery can send business metrics to an external HTTP endpoint without a separate confirmation step.

Mitigation: Keep the delivery endpoint and API keys unset for local-only runs; review the endpoint before processing sensitive metrics.

Risk: Local output may contain sensitive business metrics.

Mitigation: Use a dedicated output directory with appropriate access controls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wxt-ai/skills/metric-stakeholder-digest-workbench)

## Skill Output:

**Output Type(s):** [JSON, HTML, Files]

**Output Format:** [JSON digest containing HTML, with a local HTML artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a digest ID and metric ID; may include a delivery receipt when delivery is configured.]

## Skill Version(s):

1.1.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
