## Description:

Performs AI analysis on input video clips/image content and generates a smooth, natural scene description. | 视觉摘要智述技能，对传入的视频片段/图片内容进行AI分析，生成一段通顺自然的场景描述内容

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit image or video inputs for visual summarization and receive scene-summary text, structured analysis results, historical report listings, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, videos, and URLs may be sent to the publisher's cloud service for analysis.

Mitigation: Use only media and URLs approved for third-party processing; avoid private media or internal URLs unless retention and access controls are documented.

Risk: The skill may silently create or reuse identities and maintain local tokens.

Mitigation: Review local identity and token storage behavior before installation, and define cleanup procedures for shared or sensitive workspaces.

Risk: Historical report queries may retrieve cloud report history associated with the resolved identity.

Mitigation: Run history queries only in contexts where the resolved identity and associated reports are appropriate for the current user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-visual-summary-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown text with JSON content, status messages, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local media paths, public media URLs, optional output files, and cloud historical report listing.]

## Skill Version(s):

1.0.14 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
