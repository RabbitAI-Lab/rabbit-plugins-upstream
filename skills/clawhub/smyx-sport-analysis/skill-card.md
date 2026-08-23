## Description:

Analyzes outdoor sports event media for participant safety risks such as falls, injuries, discomfort, posture issues, and environmental hazards, then returns structured reports, warnings, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators supporting outdoor sports events use this skill to submit event video, images, or media URLs for participant risk analysis and to retrieve structured safety reports or historical report lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Participant media or media URLs may be uploaded to remote backend services for analysis.

Mitigation: Use only media appropriate for cloud processing, obtain required consent, and install the skill only when the publisher and backend are trusted.

Risk: The skill may silently create or reuse a local/default identity and store authentication data in a local SQLite database.

Mitigation: Run the skill in an isolated workspace, protect the workspace data directory, and clear stored identities or tokens when access should end.

Risk: The skill contacts configured backend endpoints and queries cloud report history.

Mitigation: Review endpoint configuration before use and restrict execution to environments where those network calls are expected.

Risk: Sports injury and health-risk analysis may be incomplete or inaccurate.

Mitigation: Treat outputs as safety-support information, not medical diagnosis, and escalate urgent incidents to qualified medical personnel.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sport-analysis)
- [API Documentation](artifact/references/api_doc.md)
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON analysis reports with report links; optional saved text or JSON output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local mp4, avi, or mov files up to 10 MB, or public media URLs; can query historical reports through configured backend services.]

## Skill Version(s):

1.0.11 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
