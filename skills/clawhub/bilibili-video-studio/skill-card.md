## Description:

B站视频一站式解析与创作工场：用户提供 B 站视频 URL 和需求后，生成转文字稿、内容总结、爆款拆解、分镜脚本、原创脚本、提示词、PPT 内容提取或备考笔记。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, educators, marketers, and agent users use this skill to turn Bilibili video links into structured Markdown deliverables such as transcripts, summaries, content breakdowns, scripts, prompts, slide extracts, and study notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary flags an unsafe API-key setup flow that asks users to paste a full Cue API key into chat and have the agent persist it locally.

Mitigation: Configure CUE_API_KEY or ~/.cue/config.json outside the conversation, restrict local file permissions, avoid echoing or logging the key, and rotate any key that was already shared in chat.

Risk: Bilibili URLs and Cue authentication are sent to the Cue service for remote parsing.

Mitigation: Use the skill only for videos and account credentials that the user is comfortable sending to Cue, and avoid private, sensitive, or platform-restricted content.

Risk: Workflows may download full videos or obtain direct media URLs, which can raise copyright, privacy, or platform-policy concerns.

Mitigation: Limit use to content the user has rights to process, avoid redistributing downloaded media, and review generated reports before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/panting09266-ai/skills/bilibili-video-studio)
- [Cue Omni Reader](https://cuecue.cn/hub/omni-reader)
- [Cue API Key Management](https://cuecue.cn/hub/api-key)
- [Cue Remote Omni Reader MCP Endpoint](https://mcp.cuecue.cn/api/omni-reader/mcp/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with tables, code blocks, shell command examples, and optional structured JSON prompt output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write parsed source text and generated Markdown reports to the workspace; results depend on Bilibili URL accessibility, Cue service availability, and user-provided Cue API authentication.]

## Skill Version(s):

1.1.1 (source: server release metadata; artifact frontmatter declares 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
