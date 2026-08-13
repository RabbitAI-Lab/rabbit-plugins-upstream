## Description:

Performs AI analysis on input video clips/image content and generates a smooth, natural scene description. | 视觉摘要智述技能，对传入的视频片段/图片内容进行AI分析，生成一段通顺自然的场景描述内容

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze image or video content from files or URLs, generate scene descriptions and structured reports, and retrieve prior visual-summary reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded media or supplied URLs are processed by the publisher's remote APIs.

Mitigation: Use the skill only with media whose remote processing is acceptable; avoid private, regulated, or confidential images and videos unless that data flow has been approved.

Risk: The skill silently creates or reuses local/cloud identity state and stores account tokens in a local workspace SQLite database.

Mitigation: Run the skill in an isolated workspace and clear local identity or token state when it is no longer needed.

Risk: Cloud report history can be queried through the skill and associated with the active identity state.

Mitigation: Confirm report-history access and retention expectations before deploying the skill for sensitive workflows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-visual-summary-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown or JSON analysis reports, with optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured recognition results, report links, and history tables; default detail level is json.]

## Skill Version(s):

1.0.12 (source: server release evidence; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
