## Description:

InvAssistant provides multi-asset portfolio analysis and investment decision support for US, China A-share, and Hong Kong stocks using asset-tier rules, portfolio red-line controls, and QMS scoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and finance-oriented agents use this skill to generate portfolio check reports, entry and exit signals, and risk-control guidance for multi-market equity portfolios. Outputs should be treated as financial decision support rather than trading automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Actionable trading signals may be mistaken for financial advice or automatic trade instructions.

Mitigation: Treat generated entry and exit signals as informational only and require human review before any trade.

Risk: Market data, formulas, or risk-gate checks may be stale, incomplete, or mismatched.

Mitigation: Verify market data, formulas, red-line checks, QMS scores, and entry/exit outputs independently before acting.

Risk: Webhook pushes may expose portfolio information to configured third-party messaging services.

Mitigation: Enable webhook notifications only after reviewing the destination service and the portfolio fields that will be sent.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/invassistant)
- [US Stock Strategy](artifact/references/us_stock_strategy.md)
- [A-Share Strategy](artifact/references/a_share_strategy.md)
- [Risk Control and Overrides](artifact/references/risk_control_and_overrides.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown portfolio reports, optional JSON signal output, and concise command/configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May fetch market data and can send configured webhook notifications; outputs are informational decision support.]

## Skill Version(s):

2.3.4 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
