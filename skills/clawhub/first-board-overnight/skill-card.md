## Description:

基于可审计 A 股数据评估首板隔夜模拟交易，筛选候选标的，生成 BUY、WATCH 或 NO_TRADE 决策，并制定 T+1 退出计划。

This skill is ready for commercial/non-commercial use.

## Publisher:

[fize](https://clawhub.ai/user/fize)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to evaluate A-share first-board overnight simulated trading candidates with explicit market evidence, risk gates, and T+1 exit planning. It supports candidate review, entry decisions, exit plans, and trade reviews without treating missing data as proof.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create local strategy reports and optional SVG charts in the user's workspace.

Mitigation: Install only when local report and chart generation is acceptable, and review generated files before relying on them.

Risk: Trading decisions can be misleading if market, plan-review, or sim-trade integrations provide incomplete or stale data.

Mitigation: Require explicit timestamps, data sources, readiness status, counterevidence, and unknown fields before treating an output as actionable.

Risk: A simulated order could be created when the user explicitly requests one and the strategy gates pass.

Mitigation: Use only simulated accounts, require status READY and decision BUY, and report the real simulated order status instead of assuming execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/fize/skills/first-board-overnight)
- [Publisher Profile](https://clawhub.ai/user/fize)
- [Data Acquisition](references/data-acquisition.md)
- [Strategy Definition](references/strategy.md)
- [Entry Policy](references/entry-policy.md)
- [Evidence Contract](references/evidence-contract.md)
- [T+1 Exit Policy](references/exit-policy.md)
- [Risk Policy](references/risk-policy.md)
- [Trade Review Schema](references/review-schema.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown strategy reports with structured decision fields, optional shell commands, and optional local SVG charts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saves standardized reports under ./report/strategy/ and may create local SVG charts from market JSON inputs.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
