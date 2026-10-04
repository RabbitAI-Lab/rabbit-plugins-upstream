## Description:

Analyzes driver-facing camera video for visible facial flushing and sweat-related changes, returning health-risk reminders and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Drivers and fleet operators use this skill to analyze in-cabin driver video for visible flushing and sweating, review alerts, and retrieve historical reports. Results are visual health reminders, not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive driver face video or video URLs are sent to external cloud services.

Mitigation: Notify drivers and obtain informed consent before use; review cloud retention and access controls.

Risk: Reports are silently linked to an internal identity and historical reports can be retrieved or exported.

Mitigation: Restrict report access and sharing, and verify that identity association matches the intended driver.

Risk: Authentication tokens may be stored in a local workspace database.

Mitigation: Limit workspace access and protect or remove stored credentials according to local policy.

Risk: Visual flushing or sweating alerts may be mistaken for a medical diagnosis.

Mitigation: Treat alerts as observations only and seek qualified medical assessment when appropriate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-driver-flushing-sweat-detection-analysis)
- [Analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or JSON analysis results; Markdown report lists with links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include visual observations, warnings, suggested actions, and links to cloud reports.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
