## Description:

Detects fire and smoke in video streams and images for fire early warning in security surveillance, forest fire prevention, and industrial park scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to submit images, videos, or media URLs for fire and smoke detection, receive structured analysis, and query prior cloud-hosted detection reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media submitted for analysis is sent to a cloud service.

Mitigation: Use only media approved for this external processing path and avoid submitting sensitive footage unless that data flow is acceptable.

Risk: Analysis and history retrieval are linked to an internal identity that may be created or reused automatically.

Mitigation: Review identity handling before deployment and limit use to environments where cloud report history tied to that identity is acceptable.

Risk: Session tokens may be stored in a workspace SQLite database.

Mitigation: Protect the workspace, restrict access to local database files, and rotate or clear tokens according to local security policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fire-smoke-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)
- [Analysis API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files]

**Output Format:** [Markdown and JSON structured analysis reports, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fire and smoke detection status, risk level, confidence details, alert guidance, report links, and history tables.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
