## Description:

Detects whether anyone has fallen within a target area, supports video stream analysis, and is suitable for real-time safety monitoring of elderly people living alone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and care-monitoring operators use this skill to submit fall-detection videos or video URLs for cloud-based analysis. The skill returns structured detection results, report links, and account-linked history for review and follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive fall-detection videos or video URLs are processed by the remote lifeemergence.com service.

Mitigation: Use the skill only for footage where recorded people have consented to remote processing and where sending video to that service is appropriate.

Risk: The skill silently creates or reuses an internal identity and retrieves cloud history tied to that identity.

Mitigation: Review identity handling before installation and avoid using shared workspaces when account-linked report history should remain separated.

Risk: Authentication tokens are stored locally by the skill support code.

Mitigation: Restrict workspace access, rotate credentials when needed, and remove local token data before sharing the workspace.

## Reference(s):

- [Skill Page](https://clawhub.ai/18072937735/skills/smyx-fall-detection-video-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Fall Detection Video Analysis API Documentation](artifact/references/api_doc.md)
- [Common AI Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files]

**Output Format:** [Markdown text with structured JSON content and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include a cloud report export link and account-linked report history.]

## Skill Version(s):

1.0.12 (source: server release evidence; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
