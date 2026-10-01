## Description:

Performs AI analysis on input video clips/image content and generates a smooth, natural scene description. | 视觉摘要智述技能，对传入的视频片段/图片内容进行AI分析，生成一段通顺自然的场景描述内容

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to submit images, videos, local files, or media URLs for visual understanding and natural-language scene summaries. It can also query cloud-hosted historical analysis reports associated with the skill's internal identity flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images, videos, or media URLs are sent to lifeemergence.com/open.lifeemergence.com cloud services for analysis.

Mitigation: Use the skill only with media that may be shared with those services, and avoid confidential media or private/internal URLs unless the backend and retention policy are trusted.

Risk: Reports may be associated with an internally generated or supplied identity, and service tokens may be stored in the workspace data directory.

Mitigation: Review identity handling and token storage before installation, and restrict workspace access where report history or tokens may be sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-visual-summary-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Open API service](https://open.lifeemergence.com/smyx-open-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like text produced by the skill's scripts, with optional saved result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured analysis content, report links, historical report tables, and progress or error messages.]

## Skill Version(s):

1.0.16 (source: server release metadata; artifact frontmatter reports 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
