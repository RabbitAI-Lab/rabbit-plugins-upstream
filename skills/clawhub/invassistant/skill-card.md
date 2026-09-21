## Description:

InvAssistant is a multi-asset investment portfolio management framework for US, A-share, and HK stocks, with A/B/C asset-class rules, red-line portfolio risk controls, QMS quality scoring, and optional Python decision-support helpers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Individual investors and agent users use this skill to review portfolios, classify holdings, check red-line risk controls, evaluate candidate positions with QMS scoring, and draft disciplined entry or exit guidance. It is decision support only and does not place trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outputs may be mistaken for individualized financial advice or direct trading instructions.

Mitigation: Treat outputs as decision support, require human review before any portfolio action, and avoid using the skill for tax, legal, regulatory, or real-time trading decisions.

Risk: Portfolio details may be exposed through logs, shared files, or optional webhook reports.

Mitigation: Keep holdings data in local trusted storage, avoid sharing generated reports that contain sensitive positions, and enable webhook delivery only to destinations the user controls and trusts.

Risk: Market-data fetching and webhook helpers transmit data off-machine when enabled.

Mitigation: Review endpoint configuration before use; the Yahoo Finance quote fetcher should only request public quote data, and notification helpers should remain disabled until a webhook URL is explicitly configured.

Risk: Missing or stale configuration can make portfolio checks misleading.

Mitigation: Review generated configuration before use and rely on the skill's fail-closed gates and red-line checks rather than treating a clean script run as permission to trade.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/invassistant)
- [Publisher profile](https://clawhub.ai/user/haiyangchenbj)
- [Yahoo Finance quote endpoint disclosed for market-data fetching](https://query1.finance.yahoo.com)
- [README](artifact/README.md)
- [Changelog](artifact/CHANGELOG.md)
- [US Stock Strategy](artifact/references/us_stock_strategy.md)
- [A-Share Strategy](artifact/references/a_share_strategy.md)
- [Risk Control and Overrides](artifact/references/risk_control_and_overrides.md)
- [Candidate Admission Gates](artifact/references/candidate_admission_gates.md)
- [Capital Plan Consistency Audit](artifact/references/capital_plan_audit.md)
- [Derived Price Level Governance](artifact/references/derived_price_governance.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional JSON/YAML configuration and Python command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include portfolio review tables, red-line pass/fail flags, QMS scores, position-sizing checks, and webhook-ready report text.]

## Skill Version(s):

2.3.18 (source: frontmatter, CHANGELOG, server release metadata; released 2026-09-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
