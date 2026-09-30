## Description:

Analyzes short adult facial videos to report contact-free heart-rate-variability (HRV) trends and historical reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Adults and health-monitoring teams use short, still facial videos to follow HRV trends, review past reports, and receive stress or fatigue reminders. Results are for personal trend awareness, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial video or video URLs are processed by the publisher's cloud service, exposing sensitive biometric and health-adjacent data.

Mitigation: Obtain informed consent and confirm the service's retention, deletion, and access controls before submitting real facial videos.

Risk: An account identity is silently created or reused and report history is linked to that identity.

Mitigation: Review the identity and history behavior with users and restrict access to reports.

Risk: Tokens and profile data are stored in the workspace database.

Mitigation: Use a protected workspace with scoped permissions and review local data-handling controls before use.

Risk: HRV estimates from facial video can be mistaken for medical-grade rhythm assessment.

Mitigation: Use results only for trend awareness and seek qualified medical evaluation for clinical concerns.

## Reference(s):

- [HRV API reference](references/api_doc.md)
- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-facial-hrv-trend-monitoring-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured report or JSON, with optional saved file and report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes HRV trend metrics, reminders, and historical report listings.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
