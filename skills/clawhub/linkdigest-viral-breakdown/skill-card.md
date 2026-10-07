## Description:

拆解单条抖音、小红书、TikTok 或 YouTube 内容的开头钩子、结构节拍、标题和行动号召，并按读取的原文核对引用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

内容创作者和营销团队用它分析单条公开视频或图文笔记的钩子、节奏和文案结构，获取可复用的创作模板；不用于预测传播效果。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted links and results are sent to an external service and results may be cached by link.

Mitigation: Submit only public, non-sensitive links or share text; avoid private, deleted or login-only content.

Risk: The skill uses an API key and the optional npx MCP setup runs an additional dependency.

Mitigation: Keep the key in environment or local configuration, never in chat; prefer the bundled Python script or curl, and review and pin mcp-remote before using npx.

Risk: Verified quotations are checked against extracted text, which can contain transcription errors; analysis and engagement snapshots may be incomplete or stale.

Mitigation: Check important quotations against the original content, review missing-information notes, and treat engagement as a dated snapshot.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/jackchew7143/skills/linkdigest-viral-breakdown)
- [LinkDigest 中文文档](https://linkdigest.dev/zh/docs)
- [LinkDigest API specification](https://linkdigest.dev/openapi.json)
- [LinkDigest privacy policy](https://linkdigest.dev/privacy)

## Skill Output:

**Output Type(s):** [Analysis, Text, Guidance]

**Output Format:** [Markdown or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a hook, up to 10 timed or image-indexed beats, title formula, call to action, reusable template and missing-information notes; JSON also includes the source reading and engagement snapshot.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
