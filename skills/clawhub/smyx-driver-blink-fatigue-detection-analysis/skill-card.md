## Description:

Analyzes driver-facing video for blink-rate and eye-closure indicators and returns fatigue warnings and reports through a remote service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and fleet operators can submit driver-facing video or a video URL to obtain fatigue indicators, warnings, and report links, or query historical reports. Results are driver-assistance prompts, not medical diagnoses or a substitute for attentive driving.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver-facing video is sent to a remote service and may contain sensitive biometric information.

Mitigation: Obtain informed consent before upload and verify the service operator, retention practices, and applicable privacy requirements.

Risk: Historical report lookup and automatic account provisioning may occur without an explicit confirmation step.

Mitigation: Confirm the intended account, history-access authorization, and endpoint scope before use; prefer a release that prompts before upload or history lookup.

Risk: The skill may store authentication tokens in plaintext locally.

Mitigation: Review token storage and access controls before installation; prefer a release with protected credential storage.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-driver-blink-fatigue-detection-analysis)
- [Driver fatigue analysis API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Report links]

**Output Format:** [JSON or readable text and Markdown report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include blink and eye-closure metrics, fatigue warnings, recommended actions, and links to historical reports.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata; embedded SKILL.md lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
