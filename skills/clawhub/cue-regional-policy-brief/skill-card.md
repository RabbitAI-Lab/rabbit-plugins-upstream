## Description:

用 Cue 聚合指定区域的政策发布、招商动态及市场数据——筛选高价值合规线索与潜客名单，产出结构化周度情报简报，赋能律所 BD 团队精准获客。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向律所 BD、招商和合规团队，汇总指定区域的政策发布、招商动态与市场信息，整理潜在合规线索和客户需求，形成周度商机简报。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to provide an API key through chat, which could expose the credential.

Mitigation: Configure the key locally through CUE_API_KEY or a protected configuration file; rotate any key already shared.

Risk: The external runner can be updated automatically, and its code was not included in this review.

Mitigation: Review and pin the runner before execution, and require approval before applying updates.

Risk: Optional scheduled runs consume Cue credits until disabled.

Mitigation: Confirm the schedule and expected usage, monitor the credit balance, and disable the schedule when it is no longer needed.

## Reference(s):

- [Cue runner repository (documented in the skill)](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror (documented in the skill)](https://gitee.com/sensedeal/cue-skills)
- [Cue platform](https://cuecue.cn)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, HTML]

**Output Format:** [Structured Chinese policy and business brief in Markdown, plus a standalone HTML dashboard]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links and may include an optional scheduled-run configuration.]

## Skill Version(s):

1.0.10 (source: target release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
