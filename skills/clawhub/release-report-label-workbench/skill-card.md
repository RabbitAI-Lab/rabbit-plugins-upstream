## Description:

Builds a stakeholder configuration report from a supplied release configuration entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release operations teams use this skill to turn a prepared configuration entry into a concise stakeholder report, save it locally, and optionally deliver it to a configured endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery can send report contents and the local artifact path to an external endpoint.

Mitigation: Review and control the delivery endpoint, API key, and delivery configuration before running; leave delivery unset unless external submission is approved.

Risk: Report content is saved to the local filesystem.

Mitigation: Use a dedicated output directory and exclude sensitive configuration values unless the report is authorized for them.

## Reference(s):

- [Stakeholder Report Publisher on ClawHub](https://clawhub.ai/wxt-ai/skills/release-report-label-workbench)

## Skill Output:

**Output Type(s):** [Markdown, JSON]

**Output Format:** [JSON report entry with Markdown content and a local Markdown file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a local file receipt and, if delivery is configured, a delivery receipt.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
