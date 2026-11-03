## Description:

Estimates relative nighttime plant respiration intensity from canopy thermal imagery and optional ambient CO₂ data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Plant factory operators and precision agriculture researchers use the skill to estimate relative nighttime respiration from canopy thermal images, optionally combined with CO₂ trends, and receive a structured monitoring report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images or videos may be sent off-device for LifeEmergence processing, with retention and charges to consider.

Mitigation: Confirm media-sharing, retention, and pricing terms before submitting imagery.

Risk: Use may silently enroll an account, retain credentials, or process media even when a configuration-only option is selected.

Mitigation: Require explicit enrollment controls and protected token storage; do not rely on configuration-only mode to prevent uploads or account activity.

Risk: The remote analytical model was not inspected, and HTTP logging safeguards need review.

Mitigation: Review credential and request-logging protections with the publisher before connecting an account.

## Reference(s):

- [Plant respiration analysis API reference](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-night-respiration-rate-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Structured report in JSON or Markdown with relative respiration estimates, qualitative levels, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Relative respiration intensity is reported on a 0–100% scale; history listings are formatted as Markdown tables.]

## Skill Version(s):

1.0.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
