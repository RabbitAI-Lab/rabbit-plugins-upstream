## Description:

用 Cue 一键生成月度大类资产配置报告，整合全球 CPI、利率、国内宏观及资金流向，从宏观逻辑推导至股、债、商配置比例，产出可交付客户的配置建议书。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External advisors, investment teams, and agent users use this skill to generate monthly asset-allocation reports for macro review, client recommendations, investment committee preparation, and portfolio rebalancing discussion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Report prompts and included financial context are sent to the external Cue service.

Mitigation: Use only with information that is appropriate to send to cuecue.cn and review account/API-key handling before installation.

Risk: Generated allocation reports may be mistaken for automated trading or account-management authority.

Mitigation: Treat reports as advisory material and require human review before client delivery or portfolio action.

Risk: Reports are stored locally under the configured output path.

Mitigation: Choose an output path with appropriate access controls for client or portfolio information.

Risk: The skill relies on an external runner and external service availability.

Mitigation: Inspect the runner before use and run the documented health checks before generating reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-asset-allocation)
- [Cue service](https://cuecue.cn)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Sample report](https://cuecue.cn/share/JJiW9tVCEK7Yq3AW0zDnw)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with shell-command and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated report is written to the configured local output path and can optionally be converted to Word or PDF with pandoc.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
