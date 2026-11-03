## Description:

用 Cue 聚合指定区域的政策发布、招商动态及市场数据——筛选高价值合规线索与潜客名单，产出结构化周度情报简报，赋能律所 BD 团队精准获客。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

律所 BD 与市场情报团队可用它追踪中国指定区域的政策和招商动态，筛选合规服务线索与潜在客户，并生成周度简报。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Setup instructions ask users to paste a Cue access key into agent chat while giving conflicting assurances about agent access to it.

Mitigation: Configure the key through a protected local mechanism instead; rotate a key already shared in chat.

Risk: Downloaded runner updates should be reviewed, and optional scheduled reports continue consuming credits until disabled.

Mitigation: Review the runner and updates before execution; disable scheduled reports when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-regional-policy-brief)
- [Cue platform](https://cuecue.cn)
- [Cue runner repository](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [中国政府网](https://www.gov.cn)
- [国家发展和改革委员会](https://www.ndrc.gov.cn)
- [商务部](https://www.mofcom.gov.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML]

**Output Format:** [结构化中文 Markdown 情报简报；可选单文件 HTML 看板]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [内容按用户指定的区域及可选行业或政策主题生成，并包含来源链接；可选定时运行会持续消耗 Cue 积分。]

## Skill Version(s):

1.0.9 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
