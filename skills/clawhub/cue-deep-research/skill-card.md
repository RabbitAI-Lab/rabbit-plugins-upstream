## Description:

通过 Cue 服务对公开数据开展多源交叉验证，并输出附可回查来源链接的深度研究报告；支持使用用户指定的参考资料进行风格仿写。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

研究人员、分析师及其智能体可用它基于公开数据调研公司、行业和市场事件，开展主体比较或风险排查，并生成带来源链接的报告。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A reference document used for style imitation may be uploaded to Cue for analysis.

Mitigation: Use only documents you explicitly approve for upload; exclude confidential, personal, regulated, or proprietary material.

Risk: The separately downloaded runner is unpinned and its executable behavior was not verified in this release.

Mitigation: Review and pin a trusted runner version before use, and protect the Cue service key.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-deep-research)
- [Cue runner repository (listed by the skill)](https://github.com/sensedeal/cue-skills)
- [Cue runner mirror (listed by the skill)](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files]

**Output Format:** [Structured Markdown research report with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Organized findings, cross-source checks, risk notes, and source URLs; optional style imitation.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
