## Description:

InvAssistant is a multi-asset investment portfolio management framework for US, A-share, and HK stocks with A/B/C asset-class rules, seven portfolio risk controls, and four-factor QMS quality scoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to review portfolios, classify holdings, evaluate watchlist candidates, apply risk-control rules, and produce disciplined investment decision-support reports. It is not intended to provide individualized financial, tax, legal, or regulatory advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests command execution and file-write authority for portfolio workflow updates.

Mitigation: Install and run it only in a sandbox or profile where file writes are limited to a dedicated portfolio directory, and grant shell execution only when it is required for a reviewed task.

Risk: The skill can direct persistent updates to automation prompts, runtime memory, and portfolio state.

Mitigation: Require explicit human confirmation before any persistent prompt, memory, or portfolio-state change is written.

Risk: The skill provides investment decision-support logic that could be mistaken for individualized financial advice.

Mitigation: Keep outputs framed as framework-based observations, require human review before action, and preserve the not-individualized-advice disclaimer.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/invassistant)
- [Publisher profile](https://clawhub.ai/user/haiyangchenbj)
- [A-share strategy](artifact/references/a_share_strategy.md)
- [US stock strategy](artifact/references/us_stock_strategy.md)
- [Risk control and overrides](artifact/references/risk_control_and_overrides.md)
- [Candidate admission gates](artifact/references/candidate_admission_gates.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with tables, action lists, data-source annotations, and occasional code or shell blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Portfolio actions should be framed as decision-support observations requiring human review, with sourced and timestamped market data where numbers are used.]

## Skill Version(s):

2.3.10 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
