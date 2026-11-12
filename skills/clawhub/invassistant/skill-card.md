## Description:

InvAssistant helps agents review multi-market stock portfolios using asset-class rules, portfolio risk controls, and quality scoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Investors use the skill to review holdings, classify positions, check portfolio risk rules, and evaluate stock candidates across US, A-share, and Hong Kong markets. Its reports support human decisions and are not financial advice.

### Deployment Geography for Use:

Global; market coverage is US, China A-shares, and Hong Kong stocks.

## Known Risks and Mitigations:

Risk: ClawScan marks the release suspicious with medium confidence, citing reported weaknesses in its investment guidance that could lead to flawed portfolio decisions.

Mitigation: Review the reported investment-check flaws and independently verify the inputs and recommendations; require human review before acting.

Risk: ClawScan also raises concerns about network, file, and dependency capabilities, and notes that its scan was partial because a local reference could not be resolved.

Mitigation: Confirm the host runtime permissions and resolved dependency versions, and review the unresolved reference before installing or relying on the skill.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/haiyangchenbj/skills/invassistant)
- [Publisher profile](https://clawhub.ai/user/haiyangchenbj)
- [Risk controls and overrides](artifact/references/risk_control_and_overrides.md)
- [US stock strategy](artifact/references/us_stock_strategy.md)
- [A-share strategy](artifact/references/a_share_strategy.md)
- [Candidate admission gates](artifact/references/candidate_admission_gates.md)
- [Capital plan audit](artifact/references/capital_plan_audit.md)
- [Derived price governance](artifact/references/derived_price_governance.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Text, Markdown, Configuration]

**Output Format:** [Structured portfolio review reports with classification and risk tables, human-reviewed action observations, data-source annotations, and optional local configuration files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Decision support only; verify market data and review recommendations before any action. The bundled helpers do not place trades autonomously.]

## Skill Version(s):

2.3.20 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
