## Description:

Analyzes aquarium videos for unusual fish swimming posture and reports abnormal events, duration, and suggested follow-up actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarists and aquarium operators use this skill to review camera footage for unusual fish swimming posture, track abnormal swimming time, and consult historical reports. Results are monitoring guidance, not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium videos or video URLs are sent to an external cloud service.

Mitigation: Confirm each upload with the user and verify the service operator, data retention, and deletion policy before use.

Risk: The skill may create or reuse a local identity, retain tokens, and query account-linked cloud report history.

Mitigation: Confirm before listing history; review access controls and how to delete local identity/token data and cloud reports.

## Reference(s):

- [Skill API documentation](references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-abnormal-swimming-detection-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis report or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include abnormal-duration ratios, suggested actions, and report links.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
