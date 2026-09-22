## Description:

Analyzes videos of vehicle drivers to identify unsafe driving behaviors and generate professional road-safety reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Drivers, road-safety teams, and developers use this skill to analyze driving videos or video URLs for fatigue, distraction, seatbelt use, posture, and other unsafe behaviors. It returns structured findings, safety suggestions, history-query results, and report links for education and awareness workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driving videos, video URLs, and report-history requests are sent to remote services.

Mitigation: Use only with approved driving media, confirm the service operator and data-retention practices, and verify production HTTPS endpoints before installation.

Risk: The skill can create or reuse an internal user identity and persist authentication tokens locally.

Mitigation: Review local SQLite token storage, workspace file permissions, identity lifecycle, and token cleanup requirements before deployment.

Risk: Packaged configuration includes plaintext development HTTP endpoints.

Mitigation: Confirm the active configuration uses trusted production HTTPS endpoints and does not route production traffic to development hosts.

Risk: A payment-required response can instruct the agent to install a separate payment skill.

Mitigation: Require user or administrator approval before installing payment-related skills or following recharge workflows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-drive-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](artifact/references/api_doc.md)
- [Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, guidance]

**Output Format:** [Markdown report text or structured JSON, with optional saved output files and report export links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports mp4, avi, and mov inputs up to 10 MB; can analyze local files or remote video URLs and query cloud report history.]

## Skill Version(s):

1.0.12 (source: server release metadata; SKILL.md frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
