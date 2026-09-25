## Description:

Analyzes driver videos for unsafe driving behaviors and produces driving-safety reports and recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Drivers, fleet safety teams, and developers use the skill to review driving footage for potential fatigue, distraction, seatbelt use, and other unsafe behaviors, or to retrieve prior analysis reports. Reports are educational aids, not substitutes for professional driver training.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver videos or video URLs are processed by a remote cloud service and may contain identifiable people or vehicles.

Mitigation: Obtain appropriate permission before uploading footage, avoid sensitive recordings where possible, and review the publisher's retention, deletion, and access controls.

Risk: The skill silently creates or reuses an identity, stores authentication tokens locally, and can fetch cloud report history on broad triggers.

Mitigation: Use only in a trusted environment; restrict access to local credentials and confirm authorization before retrieving or sharing report history.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-drive-analysis)
- [Driving analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis results, driving-safety report text, or Markdown history tables with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be saved to a file; historical reports are retrieved from a cloud service.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; bundled SKILL.md lists 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
