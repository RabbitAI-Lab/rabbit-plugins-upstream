## Description:

Analyzes child-area camera videos for dangerous climbing or leaning near windows and balconies and returns risk alerts and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and developers use this skill to submit window- or balcony-facing household videos for child-climbing risk analysis, review alerts, and retrieve historical reports. It is an aid to supervision, not a replacement for an adult caregiver.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child or household camera footage and identifiers are sent to an external analysis service.

Mitigation: Obtain guardian consent before using minors' footage, limit exposure of video and identifiers, and confirm the provider's retention and deletion policy.

Risk: Account linking happens automatically, local token/profile data persists, and report history is stored in the cloud.

Mitigation: Review the service and its account-linking behavior before installation; restrict access to local credentials and cloud reports.

Risk: Analysis may not reliably detect every dangerous action or provide immediate warning.

Mitigation: Keep adult supervision in place and respond directly to observed danger rather than relying solely on alerts.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-child-window-climbing-detection-analysis)
- [Child window and balcony detection API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Structured analysis, Report links]

**Output Format:** [Text with JSON-formatted analysis results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save results to a file or list historical cloud reports; reported risks require human verification.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; bundled SKILL.md says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
