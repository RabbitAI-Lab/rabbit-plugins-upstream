## Description:

Analyzes a child's nighttime audio and video for rolling over, crying, and sleep talking, then provides sleep-quality reports and possible nightmare or restlessness alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents or guardians use the skill to review a child's nighttime sleep recordings, receive behavioral summaries and possible restlessness alerts, and access prior reports. Its observations are not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive recordings of a child's bedroom or media URLs may be sent to a third-party cloud service.

Mitigation: Obtain guardian consent before use and confirm the provider's retention, deletion, encryption, and access-control practices before uploading real recordings.

Risk: The skill may create or reuse an identity, store tokens locally, and retrieve prior cloud reports without an explicit prompt.

Mitigation: Review account and report access before use, restrict who can access local tokens, and avoid processing recordings when these behaviors are unacceptable.

Risk: Behavioral alerts can be mistaken for a medical diagnosis.

Mitigation: Treat the report as a caregiving aid, not a diagnosis; consult a pediatric or sleep specialist for persistent concerns.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-nightmare-rollover-detection-analysis)
- [Skill API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [JSON analysis reports or Markdown summaries and historical-report tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include alert messages, report links, and an optional saved report file.]

## Skill Version(s):

1.0.10 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
