## Description:

用 Cue 汇总全球与国内宏观指标，并生成月度股、债、商品配置建议及风险提示。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

投资顾问、客户顾问及投委会材料编写者可用它梳理宏观环境、评估股债商品配置方向，并生成月度配置建议书。输出用于参考，不构成具体金融产品推荐。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance may lead users to share a secret Cue API key in chat.

Mitigation: Configure the key locally and do not share it in chat; replace any key already shared.

Risk: The workflow relies on an external runner and Cue service, and report generation can consume account credits.

Mitigation: Review and pin the external runner before execution, and check account-credit use before starting a report.

## Reference(s):

- [Cue platform](https://cuecue.cn/)
- [ClawHub release](https://clawhub.ai/panting09266-ai/skills/cue-asset-allocation)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Markdown report with macro analysis, allocation rationale and proportions, risk notes, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a Cue report link when a report is successfully generated; does not recommend specific fund or product codes.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
