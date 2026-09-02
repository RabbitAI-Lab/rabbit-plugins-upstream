## Description:

Analyzes fixed-camera video or video URLs to estimate adolescent screen-use posture, session duration, daily screen-looking time, alert level, and respectful family guidance without making a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze home, study-room, or school fixed-camera video for teen phone or game screen-use indicators, produce structured reports, and query prior cloud reports. It is intended to support monitoring and gentle family reminders, not clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles minors' camera footage or video URLs and cloud report data.

Mitigation: Use only with informed consent from guardians and the adolescent, confirm retention and sharing controls, and avoid uploading unnecessary or long-lived raw video.

Risk: The skill silently creates or reuses local identities and stores tokens in a local database.

Mitigation: Review local data storage, token handling, and deletion controls before deployment, and restrict access to the workspace data directory.

Risk: The bundled configuration includes dev/private HTTP endpoints and cloud-history queries.

Mitigation: Confirm production endpoint configuration, transport security, and authorization boundaries before using the skill with real data.

Risk: Behavior classification may be mistaken for a medical or psychiatric assessment.

Mitigation: Present results as visual posture and screen-time observations only, and route clinical concerns to qualified professionals.

## Reference(s):

- [API Reference](references/api_doc.md)
- [Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-teen-screen-addiction-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown text containing structured JSON results, report links, or history lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include posture states, screen-time totals, alert levels, recommended actions, parent summaries, and report export links.]

## Skill Version(s):

1.0.3 (source: server release evidence; artifact frontmatter lists 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
