## Description:

Performs AI analysis on input video clips/image content and generates a smooth, natural scene description. | 视觉摘要智述技能，对传入的视频片段/图片内容进行AI分析，生成一段通顺自然的场景描述内容

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to send clear image or video inputs to a remote visual-analysis service and receive natural-language scene summaries, structured analysis results, report links, or historical report listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, videos, and report queries are sent to the provider's cloud service.

Mitigation: Use the skill only with media approved for that provider, and confirm upload, retention, and sharing practices before deployment.

Risk: The security evidence says the skill silently manages identity and tokens.

Mitigation: Make identity and token creation, reuse, storage, and revocation explicit and controllable before production use.

Risk: The security evidence reports an active plaintext development API configuration.

Mitigation: Remove the development HTTP profile and require HTTPS before attaching credentials, media, or report data.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-visual-summary-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json]

**Output Format:** [Markdown or JSON visual-analysis report with scene descriptions, structured findings, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the returned report to a file when an output path is provided; artifact documentation states support for jpg, jpeg, png, mp4, avi, and mov inputs up to 10 MB.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata; artifact frontmatter states 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
