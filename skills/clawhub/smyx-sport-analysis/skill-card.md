## Description:

Analyzes video from outdoor sports events to identify possible injuries, sudden health concerns, and other safety risks, then provides a structured report and timely warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Event organizers and sports safety teams can review video from races and other outdoor events for possible falls, injuries, signs of physical distress, posture concerns, and environmental hazards. The skill returns a structured report with warnings and response suggestions; it is for safety reference and does not replace professional medical assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private reports could be associated with the wrong user if account separation or server-side authorization is insufficient.

Mitigation: Require reliable per-user account separation and verify server-side authorization before using shared workspaces or retrieving reports.

Risk: Video uploads may send private footage to a provider even when an export-only option is expected.

Mitigation: Confirm export-only behavior works and review the provider's upload, access, retention, and payment terms before submitting footage.

Risk: Credential-bearing requests could reach an unapproved destination.

Mitigation: Restrict credential-bearing requests to approved HTTPS destinations.

Risk: Video-based findings may be incomplete and could be mistaken for a medical diagnosis.

Mitigation: Treat results as safety reference only; stop activity and seek professional medical help for urgent symptoms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sport-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface notes](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured JSON analysis results and Markdown summaries with risk findings, warnings, response suggestions, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Safety reference only; not a medical diagnosis]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
