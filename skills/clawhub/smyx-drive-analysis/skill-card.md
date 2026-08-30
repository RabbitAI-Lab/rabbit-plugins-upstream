## Description:

Analyzes driver videos to identify unsafe behaviors such as fatigue, distraction, seat belt issues, posture concerns, and other driving risks, then returns structured safety reports and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit driving videos or video URLs for safety behavior analysis, then review structured findings and safety-improvement suggestions. It can also retrieve cloud-stored historical driving-analysis reports associated with the local or upstream identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driving videos or video URLs may be uploaded to configured remote services for analysis.

Mitigation: Install only when the publisher and service endpoints are trusted, and avoid submitting sensitive media unless users have consent and the retention expectations are acceptable.

Risk: The skill may read or create a local identity and persist tokens in a workspace SQLite database.

Mitigation: Run in a controlled workspace, inspect or clear local data after use, and avoid sharing the workspace database with unintended users.

Risk: Historical report queries may return cloud-stored reports linked to the resolved identity.

Mitigation: Use separate identities or isolated workspaces when report history should not be mixed across users or deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-drive-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API interface documentation](references/api_doc.md)
- [Smyx analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, files]

**Output Format:** [JSON or Markdown analysis report with optional report export link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a local file when an output path is provided.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter states 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
