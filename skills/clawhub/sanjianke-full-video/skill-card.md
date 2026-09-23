## Description:

Supports text-to-video, first/last-frame video, and multimodal reference video generation through the a7w full_video submit and query APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

Developers, creators, and agent operators use this skill to configure an a7w API key, submit full_video generation jobs, and query task status or results. It is intended for workflows that need video generation from text, frame inputs, or reference media while using the user's own a7w account credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The client can send the bearer API key to a user-configurable host.

Mitigation: Keep the default api.a7w.cn host unless you intentionally control the destination; avoid --host and A7W_HOST in normal use.

Risk: The bundled client can call broader a7w marketplace APIs beyond the full_video submit and query flow.

Mitigation: For least-privilege deployments, narrow the client or wrapper to api.a7w.cn and the full_video submit/query endpoints only.

Risk: Calls can spend the user's a7w account credits, including repeated asynchronous submissions.

Mitigation: Review parameters before submitting, avoid duplicate submissions, and monitor task status and point usage with the documented client commands.

Risk: Generated video content may require legal, copyright, or content-policy review before use.

Mitigation: Review generated outputs before publication and apply the user's own compliance process for source media and generated content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-full-video)
- [开始使用：注册、充值、配置 Key](references/getting-started.md)
- [全能视频生成 · 提交任务](references/api-submit.md)
- [全能视频生成 · 查询任务](references/api-query.md)
- [算力集市 · 注册领 API Key](https://api.a7w.cn/)
- [AI 插件市场](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided a7w API key; submit calls may create asynchronous tasks, poll until completion, and consume the user's account credits.]

## Skill Version(s):

1.0.5 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
