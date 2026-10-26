## Description:

Analyzes video and optional audio for signs of emotional distress during pregnancy, returning an emotion report and suggested soothing actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pregnant users and authorized caregivers can review emotion-related observations from camera footage and optional audio, receive soothing suggestions, and view historical reports. Use requires explicit consent and careful handling of sensitive recordings and alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive video and optional audio may capture pregnant users or bystanders without meaningful consent.

Mitigation: Require the pregnant user's explicit consent; provide visible notice and an opt-out in shared spaces.

Risk: Cloud report history and local tokens may expose private health-related observations.

Mitigation: Verify account authorization and user identity binding; protect report access and stored tokens, and clarify deletion and reset controls before home or clinic use.

Risk: Emotion interpretations and automatic alerts may be inaccurate or reach an unwanted contact.

Mitigation: Keep interpretations non-diagnostic and let the pregnant user choose and approve alert contacts before enabling notifications.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pregnancy-emotion-soothing-analysis)
- [Pregnancy emotion soothing API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Report links]

**Output Format:** [Markdown or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes emotion observations, suggested soothing actions, and links or tables for cloud-hosted reports.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata; bundled frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
