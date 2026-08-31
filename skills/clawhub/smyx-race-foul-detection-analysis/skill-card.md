## Description:

Analyzes pet race start or finish videos to identify false starts, lane crossing, finish order, and lane assignments for referee review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, event staff, and developers use this skill to run video-based foul detection for pet racing, including false-start and lane-crossing checks. Results are intended to support referee review rather than replace the final on-site decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Race media or media URLs may be sent to a remote service for analysis.

Mitigation: Review the configured service endpoints and only process media that is approved for that destination.

Risk: The skill may silently create or reuse an account identity and store session tokens or profile data in the workspace.

Mitigation: Run it in an isolated workspace, review local stored identity data, and remove or rotate tokens after use when appropriate.

Risk: History queries may retrieve prior cloud reports linked to the resolved identity.

Mitigation: Confirm the user is authorized to view those reports before running history-list mode.

Risk: Bundled configuration may select dev HTTP or private-network endpoints.

Mitigation: Change configuration to approved production HTTPS endpoints before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-race-foul-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands]

**Output Format:** [Markdown reports with structured JSON-style results, report links, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report history when history-query mode is requested.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
