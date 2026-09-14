## Description:

InvAssistant provides a multi-asset investment portfolio management framework with A/B/C asset-class rules, seven portfolio risk controls, QMS quality scoring, and disciplined entry and exit logic for US, A-share, and HK stocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to review portfolios, classify holdings and candidates, check concentration and drawdown rules, and produce advisory entry or exit observations under the documented framework. It is decision support, not tax, legal, regulatory, or individualized financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive portfolio details may be sent to arbitrary webhook destinations.

Mitigation: Keep webhook push disabled unless the destination is verified, use official HTTPS provider URLs, and redact portfolio details before sending reports.

Risk: Generated entry and exit signals may be mistaken for financial advice or execution instructions.

Mitigation: Treat outputs as advisory and manually verify market data, cost basis, rule checks, and portfolio context before acting.

Risk: Persisted portfolio rules or automation prompts can preserve incorrect assumptions.

Mitigation: Review proposed state changes before applying them and keep rule updates logged with source and timestamp.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/invassistant)
- [README](README.md)
- [US Stock Strategy](references/us_stock_strategy.md)
- [A-Share Strategy](references/a_share_strategy.md)
- [Risk Control and Overrides](references/risk_control_and_overrides.md)
- [Candidate Admission Gates](references/candidate_admission_gates.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON portfolio check output, Python helper scripts, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should carry data source and timestamp annotations where numeric market or portfolio values are used.]

## Skill Version(s):

2.3.14 (source: SKILL.md frontmatter, README, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
