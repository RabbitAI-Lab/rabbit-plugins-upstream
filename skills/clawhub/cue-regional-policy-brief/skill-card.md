## Description:

用 Cue 汇总指定区域的政策、招商和市场信息，形成面向律所业务拓展的周度商机简报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

律所业务拓展团队使用该技能跟踪区域政策和招商动态，识别潜在合规服务需求与潜在客户，并生成带来源链接的周度简报。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 聊天中索取或披露 Cue API Key 可能泄露凭据。

Mitigation: 不要把 API Key 粘贴到聊天中；仅由用户本人创建并保存在本地配置或环境变量中。

Risk: 依赖可变更的第三方 Cue runner 代码。

Mitigation: 仅在信任 Cue 和 runner 来源时安装，并在运行或更新前审查代码。

Risk: 区域目标、客户名称和业务拓展策略可能发送至 Cue 处理。

Mitigation: 提交任务前核对输入，避免发送不应共享的客户或业务敏感信息。

## Reference(s):

- [ClawHub 技能发布页](https://clawhub.ai/panting09266-ai/skills/cue-regional-policy-brief)
- [Cue 平台](https://cuecue.cn)
- [Cue API Key 管理](https://cuecue.cn/api-key?src=clawhub-regional-policy-brief)
- [技能文档指定的 Cue runner](https://github.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown 简报及原始报告链接]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [按区域整理政策更新、招商动态、合规线索、潜在客户和来源链接；可保存为本地 Markdown 文件。]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
