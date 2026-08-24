## Description:

Invassistant is a multi-asset investment portfolio management framework with A/B/C asset-class rules, seven portfolio risk controls, and four-factor QMS quality scoring for US, China A-share, and HK stocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to structure portfolio reviews, red-line risk checks, candidate QMS scoring, and rule-based entry or exit analysis across US, China A-share, and HK equity holdings. Outputs are decision-support analysis and require human review before any financial action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Investment analysis output could be mistaken for financial advice or automated trading direction.

Mitigation: Treat outputs as analysis aids, verify all market data and assumptions, and require explicit human review before any trade or financial decision.

Risk: Portfolio rules and risk checks depend on accurate, current holdings and market data.

Mitigation: Use sourced, timestamped data for each number and mark unsourced values instead of filling gaps by assumption.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/invassistant)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown structured review reports with tables, action-list observations, and data-source annotations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Decision-support only; numerical claims should include source and timestamp, and unsourced values are marked.]

## Skill Version(s):

2.3.8 (source: server evidence release.version and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
