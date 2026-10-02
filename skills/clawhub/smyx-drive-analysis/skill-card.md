## Description:

Analyzes driver videos for unsafe driving behaviors and produces driving safety reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Drivers and road-safety teams use this skill to assess driving footage for fatigue, distraction, seatbelt use, and other unsafe behaviors, and to review analysis reports and report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver videos or private video URLs may be sent to lifeemergence.com services.

Mitigation: Review the destination and obtain permission before submitting sensitive footage or private URLs.

Risk: The skill can create or reuse a cloud-linked identity and persist user and token data locally for report history.

Mitigation: Review account creation and local data retention before installation; restrict access to stored credentials and history.

## Reference(s):

- [Skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-drive-analysis)
- [Analysis API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Driving-behavior analysis reports, structured JSON results, report links, or Markdown report-history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report detail and analysis type are selectable; results can be saved to a file.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata; bundled SKILL.md lists 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
