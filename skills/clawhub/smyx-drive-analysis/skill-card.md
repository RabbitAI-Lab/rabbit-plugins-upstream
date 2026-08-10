## Description:

Analyzes driver videos to identify unsafe driving behaviors and generate structured road-safety reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze driving videos or video URLs for fatigue, distraction, seatbelt use, posture, and other unsafe driving patterns. It returns structured reports, safety suggestions, and links to cloud-hosted report details or history when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driving videos or video URLs may be sent to the configured cloud service and can contain sensitive driver, vehicle, route, or location information.

Mitigation: Use only approved media, confirm consent and data-handling requirements, and install the skill only where the configured cloud analysis service is acceptable.

Risk: The skill can silently create or reuse an internal account identity and store account or token data locally.

Mitigation: Review local workspace storage policies before installation, restrict workspace access, and clear stored identity data according to the environment's retention policy.

Risk: Cloud report history can be queried, which may expose prior driving-analysis reports associated with the resolved identity.

Mitigation: Limit use to environments where historical report access is expected, and verify account scoping before enabling report-list workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-drive-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON analysis reports, with optional saved text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report links and historical report tables.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact SKILL.md frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
