## Description:

Detects fire and smoke in video scenes, supports video stream and image analysis, and is intended for early warning scenarios such as security surveillance, forest fire prevention, and industrial parks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit local files or media URLs for fire and smoke detection, receive structured analysis reports, and query cloud report history for incident review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied images, videos, and URLs may be sent to third-party cloud services for analysis.

Mitigation: Use only media and URLs approved for cloud processing, and avoid sensitive surveillance footage or private URLs unless that processing is acceptable.

Risk: The skill silently creates or reuses a local identity and can query cloud report history.

Mitigation: Review report-history behavior before deployment and run the skill in a workspace where identity-linked history access is expected.

Risk: Service tokens may persist in a workspace SQLite database and the skill may read data/smyx-api-key.txt.

Mitigation: Install in a controlled workspace, restrict access to local data files and databases, and rotate or remove stored credentials when the skill is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fire-smoke-detection-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Files]

**Output Format:** [Markdown text with structured JSON analysis and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detection results, risk guidance, report links, and cloud report-history listings.]

## Skill Version(s):

1.0.12 (source: server release evidence; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
