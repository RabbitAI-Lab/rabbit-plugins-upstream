## Description:

Analyzes frontal face images or videos to identify emotion categories, quantify intensity, flag abnormal emotion scores, and return structured emotion-recognition reports or history listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to analyze user-provided face images or videos for emotion-recognition workflows, including human-computer interaction feedback, mental-health monitoring support, and cloud report retrieval. Results are informational and should not be treated as professional psychological diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload face images or videos and emotion-analysis results to external services.

Mitigation: Use only with informed user consent, avoid unnecessary sensitive media, and review the service data-handling and retention terms before deployment.

Risk: The skill may silently create or reuse a persistent local identity and retrieve cloud-stored report history.

Mitigation: Run it only in workspaces where identity linkage is expected, restrict access to generated reports, and provide users a clear process for report review and deletion.

Risk: Emotion-recognition output can be misleading if interpreted as clinical assessment.

Mitigation: Present results as informational signals only and route sustained distress or abnormal-emotion concerns to qualified professionals.

Risk: Account tokens may be stored in a shared workspace database.

Mitigation: Limit installation to trusted workspaces, protect local storage, and rotate or revoke tokens if workspace access changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-human-emotion-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands]

**Output Format:** [Markdown reports, Markdown history tables, and JSON-formatted structured analysis.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dominant emotion, per-emotion scores, abnormal-emotion flags, report links, and optional saved output files.]

## Skill Version(s):

1.0.11 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
