## Description:

Performs AI analysis on input video clips/image content and generates a smooth, natural scene description. | 视觉摘要智述技能，对传入的视频片段/图片内容进行AI分析，生成一段通顺自然的场景描述内容

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze clear images, videos, local files, or media URLs and receive visual scene summaries, structured analysis results, and report links. It can also retrieve historical visual summary reports associated with the current internal identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media and report requests are sent to lifeemergence.com/open.lifeemergence.com services.

Mitigation: Use only media approved for those services and avoid sensitive content unless the service data handling is acceptable.

Risk: The skill may create or reuse a local identity and store service tokens locally.

Mitigation: Review local data storage policy, protect workspace files, and clear generated identity or token data when no longer needed.

Risk: Historical report links may be tied to the current internal identity.

Mitigation: Share report output only with authorized users and verify the active identity before listing historical reports.

## Reference(s):

- [Visual summary API documentation](references/api_doc.md)
- [Common AI analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-visual-summary-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands]

**Output Format:** [Markdown or JSON analysis text, with optional saved output files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local file or URL input; accepted local formats include mp4, avi, and mov with a 10MB limit.]

## Skill Version(s):

1.0.13 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
