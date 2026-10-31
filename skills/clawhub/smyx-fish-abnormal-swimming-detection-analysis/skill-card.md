## Description:

Analyzes aquarium-camera footage to identify abnormal fish swimming postures and summarize how much observed time is spent in those postures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarists and aquarium operators use the skill to review fixed-camera footage, track unusual swimming posture, and receive summaries that can prompt closer observation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The export-only option still processes footage.

Mitigation: Wait for a fix before relying on the option as export-only, and confirm its behavior before use.

Risk: Using the service involves uploading footage, remote account creation, and local token storage; the provider's retention terms need review.

Mitigation: Before use, confirm acceptance of footage uploads and account/token handling, verify the provider's retention terms, and use a dedicated identity rather than an existing secret as an account identifier.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-abnormal-swimming-detection-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured fish-posture analysis report in JSON or Markdown, with summary metrics and report links when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes posture categories, observed durations, and abnormal-time proportion; visual observations are not disease diagnoses.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
