## Description:

通过知你AI助手查询多平台客户资料、会话、聊天记录与分群，并在用户确认后打开客户对话或发送消息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhinikefu](https://clawhub.ai/user/zhinikefu)

### License/Terms of Use:

MIT-0

## Use Case:

客服团队使用此技能查询跨渠道客户资料、实时及历史会话、聊天记录、分群和 API Key 用量；确认目标客户及内容后，可执行客户对话打开和文本或图片消息发送，并查看任务进度。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized access exposes customer profiles and chat history.

Mitigation: Review OAuth or API-key permissions and limit access to the intended customer-service data.

Risk: Bulk outreach can contact unintended customers, and sent messages cannot be recalled.

Mitigation: Verify recipient selection and message content, and require explicit user confirmation before sending.

Risk: Deleting a message task can irreversibly remove its record.

Mitigation: Review the task and retain needed details before deletion.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhinikefu/skills/zhini-ai-assistant-skills)
- [知你客服官网](https://ai.zhinikefu.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language summaries and task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Customer outreach actions require explicit user confirmation; results depend on the connected account's permissions.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
