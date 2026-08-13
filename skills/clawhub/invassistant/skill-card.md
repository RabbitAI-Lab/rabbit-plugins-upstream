## Description:

InvAssistant is a multi-asset investment portfolio management framework for US, A-share, and HK stocks with asset-class rules, seven portfolio red lines, and QMS quality scoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to review investment portfolios, classify holdings, apply risk-control red lines, evaluate QMS scoring, and structure disciplined entry or exit decisions. It is decision support for portfolio management, not financial, tax, legal, or regulatory advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portfolio files and holdings reports may contain sensitive financial information, especially when local reports are saved or notification scripts are enabled.

Mitigation: Store portfolio files locally with appropriate access controls, keep webhook URLs and secrets private, and verify message destinations before using push features.

Risk: The skill can propose buy, sell, reduce, add, or exit actions as part of portfolio risk-control workflows.

Mitigation: Treat all output as advisory decision support and require user review before any position-changing action.

## Reference(s):

- [InvAssistant ClawHub Page](https://clawhub.ai/haiyangchenbj/skills/invassistant)
- [US Stock Strategy](references/us_stock_strategy.md)
- [A-Share Strategy](references/a_share_strategy.md)
- [Risk Control and Overrides](references/risk_control_and_overrides.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with optional Python-backed portfolio analysis and notification commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read local portfolio files, save local analysis reports, and optionally send reports through configured messaging webhooks.]

## Skill Version(s):

2.3.6 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
