## Description:

用 Cue 聚合指定区域的政策发布、招商动态及市场数据，筛选合规线索与潜客名单，并产出结构化的区域政策商机简报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business-development teams use this skill to turn regional policy changes, investment-promotion activity, market signals, and compliance triggers into prospecting-oriented intelligence briefs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries may disclose regional, industry, policy-topic, or business-intelligence interests to Cue/cuecue.cn.

Mitigation: Avoid confidential client names, regulated data, and sensitive prospecting targets unless third-party sharing has been approved.

Risk: The brief depends on Cue service availability and external public data sources, so results may be delayed, incomplete, or stale.

Mitigation: Review source links in the generated brief and verify material findings against official policy or agency sources before business use.

Risk: Local execution requires a Cue API key and an external runner setup.

Mitigation: Store the API key in the expected local configuration or environment variable and verify the runner setup before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-regional-policy-brief)
- [ClawHub publisher profile](https://clawhub.ai/user/panting09266-ai)
- [Cue sample regional policy brief](https://cuecue.cn/share/TRk4KUxsHw1y89JrEnsRH)
- [Cue API key page](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown brief with source links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue API key and may send the selected region, industry, policy topic, and related business-intelligence query contents to Cue/cuecue.cn.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
