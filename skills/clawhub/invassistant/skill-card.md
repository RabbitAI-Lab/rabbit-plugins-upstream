## Description:

InvAssistant helps review US, A-share, and Hong Kong stock portfolios using asset-class rules, portfolio risk controls, and quality scoring, without placing trades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and portfolio reviewers use this skill to classify holdings, check portfolio risk limits, and evaluate entry or exit decisions across US, mainland Chinese, and Hong Kong equities. Its reports and suggested actions are decision support, not autonomous trading or personalized financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portfolio suggestions may influence financial decisions.

Mitigation: Review proposed actions and the underlying portfolio data yourself before acting.

Risk: Enabled webhook notifications may send report contents to a configured endpoint.

Mitigation: Check webhook URLs before enabling pushes and keep notification secrets in environment variables or private configuration.

Risk: Edits to local portfolio or configuration files may affect later assessments.

Mitigation: Review local portfolio and configuration changes before relying on future reports.

## Reference(s):

- [InvAssistant release on ClawHub](https://clawhub.ai/haiyangchenbj/skills/invassistant)
- [US stock strategy](artifact/references/us_stock_strategy.md)
- [A-share strategy](artifact/references/a_share_strategy.md)
- [Portfolio risk controls and overrides](artifact/references/risk_control_and_overrides.md)
- [Candidate admission gates](artifact/references/candidate_admission_gates.md)
- [Capital plan consistency audit](artifact/references/capital_plan_audit.md)
- [Derived price level governance](artifact/references/derived_price_governance.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Configuration instructions, Shell commands]

**Output Format:** [Text or Markdown guidance and portfolio reports; optional local JSON configuration and reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional market-data fetching and user-enabled webhook report notifications]

## Skill Version(s):

2.3.19 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
