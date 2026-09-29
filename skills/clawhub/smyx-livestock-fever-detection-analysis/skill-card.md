## Description:

Screens livestock and poultry thermal or visible-light images and videos for possible fever or low-temperature anomalies and reports early warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock and poultry caretakers use the skill to screen thermal or visible-light media for individual and group temperature anomalies and review historical reports. Results are screening alerts, not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Livestock images, video, URLs, and report history are sent to a third-party cloud service.

Mitigation: Use only with authorized media and URLs; confirm the provider's retention and access controls before sharing private farm imagery or sensitive internal URLs.

Risk: The skill silently creates or reuses persistent identities and stores service tokens for cloud history access.

Mitigation: Treat the local workspace database as sensitive, restrict access to it, and review identity controls before enabling report history.

Risk: Visual temperature screening may be mistaken for a confirmed disease diagnosis.

Mitigation: Use alerts only for screening and seek veterinary assessment and laboratory testing for diagnosis and treatment decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-fever-detection-analysis)
- [API interface reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis text or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include anomaly levels, estimated temperatures, report links, and an optional saved result file.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
