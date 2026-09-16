## Description:

Multi-asset investment portfolio management framework with A/B/C asset-class differentiated rules, 7 red-line portfolio risk controls, and 4-factor QMS quality scoring for US, A-share, and HK stocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use InvAssistant to review portfolios, classify holdings, evaluate entry and exit rules, run red-line risk checks, and generate human-reviewed decision-support reports for US, A-share, and HK stock strategies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial reports, red-line checks, and entry or exit observations may be mistaken for autonomous trading instructions or personalized financial advice.

Mitigation: Treat outputs as decision support only; manually review all alerts, thresholds, and action lists before taking any financial action.

Risk: Local portfolio configuration and generated reports can contain sensitive financial information.

Mitigation: Install only where local portfolio data access is acceptable, keep configuration files controlled, and review report contents before sharing them.

Risk: Optional WeCom, DingTalk, and Feishu webhook helpers can transmit report content to a configured destination.

Mitigation: Leave webhook notifications disabled unless the destination URL and signing settings have been verified; send only reports the user intentionally chooses to push.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/invassistant)
- [A-share Strategy](references/a_share_strategy.md)
- [Candidate Admission Gates](references/candidate_admission_gates.md)
- [Risk Control and Overrides](references/risk_control_and_overrides.md)
- [US Stock Strategy](references/us_stock_strategy.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with tables and action lists, optional JSON script output, and inline shell or configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Decision-support outputs require human review before any financial action; optional webhook helpers transmit only user-selected report content after configuration.]

## Skill Version(s):

2.3.15 (source: SKILL.md frontmatter, README.md, evidence release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
