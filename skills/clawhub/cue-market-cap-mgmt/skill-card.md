## Description:

用 Cue 跑市值管理场景的深度研究，从价值创造、传播、实现三维构建市值管理方案，覆盖策略方案、并购标的挖掘、潜在上市企业挖掘、股权激励方案设计、市值监测日报、上市公司全景速览、市值健康度诊断和非上市企业估值监控。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to run Cue research workflows for market-capitalization management, capital-markets events, trading context, disclosures, and regulatory signals. It helps produce source-linked research reports and decision support, but does not replace due diligence, legal review, underwriting, or professional investment judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may clone or update an external Cue runner before execution.

Mitigation: Review the Cue runner source and pin or control the runner location when tighter supply-chain assurance is required.

Risk: The workflow uses a Cue account API key and may spend Cue credits after confirmation.

Mitigation: Require explicit user confirmation before running a paid research workflow and use only the intended Cue account configuration.

Risk: Market-capitalization research may be incomplete or misleading if treated as professional advice.

Mitigation: Keep source links in the output, verify material claims, and treat reports as decision support rather than due diligence, legal, underwriting, or investment advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-market-cap-mgmt)
- [Cue playbook API](https://cuecue.cn/api/playbook)
- [Cue runner repository](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with source links and inline shell commands or execution guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final reports should retain source links; runner executions may return ok or empty.]

## Skill Version(s):

1.0.1 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
