## Description:

InvAssistant is a multi-asset investment portfolio management framework for US, A-share, and HK stocks with A/B/C asset-class rules, portfolio red-line controls, QMS scoring, and optional local Python decision-support helpers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to review portfolios, classify holdings, evaluate risk-control red lines, score stock candidates, and generate framework-compliant observations for human investment review. It is decision support only and does not provide autonomous trading or financial, tax, legal, or regulatory advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat generated entry, exit, or risk-control observations as trade instructions.

Mitigation: Present outputs as decision-support observations and require independent human review before any investment action.

Risk: Portfolio or watchlist symbols are sent to quote APIs when market data helpers are used.

Mitigation: Install only if this data sharing is acceptable, review configured data sources, and avoid entering information that should not leave the local environment.

Risk: Optional chat webhook helpers can send full report text to configured WeCom, DingTalk, or Feishu endpoints.

Mitigation: Keep webhook adapters disabled unless needed, verify destination URLs and secrets, and review report content before enabling delivery.

Risk: Outdated or vulnerable dependencies could affect the optional Python helpers.

Mitigation: Keep the pinned dependency ranges updated and rescan the skill before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/invassistant)
- [Publisher profile](https://clawhub.ai/user/haiyangchenbj)
- [README](README.md)
- [Changelog](CHANGELOG.md)
- [US Stock Strategy](references/us_stock_strategy.md)
- [A-Share Strategy](references/a_share_strategy.md)
- [Risk Control and Overrides](references/risk_control_and_overrides.md)
- [Candidate Admission Gates](references/candidate_admission_gates.md)
- [Capital Plan Consistency Audit](references/capital_plan_audit.md)
- [Derived Price Level Governance](references/derived_price_governance.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, JSON snapshots, Python helper output, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs require human review; optional webhook delivery sends user-selected report text only after configuration.]

## Skill Version(s):

2.3.17 (source: frontmatter, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
