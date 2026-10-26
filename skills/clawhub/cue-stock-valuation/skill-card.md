## Description:

用 Cue 对个股进行全周期估值分析——融合短线资金流向与中长线估值模型，短期看情绪博弈与支撑压力，中长期看业绩兑现与安全边际。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向外部用户及投资研究者，用于查看个股短、中、长期资金情绪、业绩展望、估值区间与安全边际，并形成结构化研究报告。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The externally updated runner includes advice to disable sandbox protections, which can weaken isolation.

Mitigation: Review and pin a trusted runner version before use, keep sandbox protections enabled, and limit network and file access to what the research task requires.

Risk: Research queries are sent to Cue, calls consume credits, and local authentication code reads the user's Cue API key.

Mitigation: Tell the user before running research, protect the key, let the user configure their own credentials, and avoid sending unnecessary sensitive information.

## Reference(s):

- [Cue 股票研究报告示例](https://cuecue.cn/share/NMJ36JGzIwOx8SPJXB_WR)
- [Runner repository (referenced by the skill; not server-resolved provenance)](https://github.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [中文结构化个股研究报告（Markdown）]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [涵盖短线资金与技术面、中长期估值及安全边际；结果依赖 Cue 与外部数据源，不构成具体买卖建议。]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
