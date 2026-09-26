## Description:

Analyzes aquarium camera videos for unusual fish swimming postures and reports observed anomalies, their duration, and suggested follow-up actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers and operators use fixed-camera footage to review unusual fish swimming behavior, monitor trends, and decide when to inspect water conditions or consult an aquatic animal professional. The observations are not disease diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private aquarium footage or supplied video URLs are sent to an external cloud service.

Mitigation: Confirm authorization and review the service's retention and sharing terms before submitting private footage or internal URLs.

Risk: The skill automatically creates or reuses an identity and stores authentication data locally; history queries may expose previous reports.

Mitigation: Review account access and local credential storage, and use only an authorized account to query history.

Risk: Posture alerts may be misleading for species with naturally unusual swimming behavior.

Mitigation: Configure species-specific baselines and have a person review alerts before taking action; do not treat results as a disease diagnosis.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-abnormal-swimming-detection-analysis)
- [API interface reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or historical-report listing, with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes abnormal-posture observations, duration or proportion, alerts, and suggested actions when available.]

## Skill Version(s):

1.0.10 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
