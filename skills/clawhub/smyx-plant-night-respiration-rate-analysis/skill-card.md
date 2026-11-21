## Description:

Estimates relative nighttime plant respiration from canopy thermal imagery and optional ambient CO₂ data, returning an analysis report and monitoring guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Plant-factory, greenhouse, and controlled-environment agriculture operators can use the skill to estimate relative nighttime respiration from thermal images or video, optionally with CO₂ measurements. It returns a structured report with activity levels and environmental guidance for monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks the release suspicious and its scan partial, citing unclear credential handling, remote registration, destination checks, export-only behavior, and remote processing disclosure; it does not establish malicious intent.

Mitigation: Avoid installation or use with sensitive images or credentials until these behaviors, processing destinations, and data handling are clarified.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-night-respiration-rate-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured JSON analysis results and text or Markdown report summaries, listings, and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Relative respiration intensity index (0–100%), activity level, risk notes, environmental guidance, and report links when returned by the service]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
