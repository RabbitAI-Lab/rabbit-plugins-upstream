## Description:

帮助动漫、漫剧、游戏和原创IP团队通过 AI-HIVE MCP 规划并生成强透视、高反差漫画动画内容，包含原创设定、分镜、关键帧、动画片段、任务记录和验收清单，并要求付费生成、批量、发送和公开发布前再次确认。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

动漫、漫剧、游戏、原创IP 和角色内容团队用它把强透视、高反差漫画动画需求转成可审计的制作计划、小样、AI-HIVE 模型路由和验收清单，并在确认后生成关键帧或视频片段。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send AI-HIVE credentials to an MCP URL controlled through AI_HIVE_MCP_URL.

Mitigation: Prefer OAuth through a trusted MCP client. If using API-key or access-token environment variables, unset AI_HIVE_MCP_URL or confirm it is exactly https://ai-hive.iclip.cn/api/mcp before running the helper.

Risk: Image or video generation, uploads, batch actions, sending, or publishing can incur cost or expose user-provided material.

Mitigation: Keep the skill's confirmation gates: query available models and prices first, create only a minimal sample before approval, and require explicit user confirmation before paid or public actions.

Risk: Anime style references or user assets can create rights issues if copied too closely or used without authorization.

Mitigation: Use original characters and assets, describe reference works only by mechanisms such as composition or pacing, and confirm rights for people, brands, music, fonts, images, and video before generation or release.

## Reference(s):

- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP endpoint](https://ai-hive.iclip.cn/api/mcp)
- [MCP login and binding guide](references/mcp-binding.md)
- [Original workflow card](references/original-workflow.md)
- [OAuth MCP configuration example](references/mcp-config.example.json)
- [API-key MCP configuration example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and optional local JSON work-order files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide AI-HIVE MCP model lookup and, after explicit user confirmation, image or video generation tasks.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
