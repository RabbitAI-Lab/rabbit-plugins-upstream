## Description:

Analyzes China A-share watchlists and holdings to produce deterministic value scores, trading-environment scores, scenario valuation, data-gap reporting, constrained allocation references, and offline HTML reports without placing trades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[holauv](https://clawhub.ai/user/holauv)

### License/Terms of Use:

MIT

## Use Case:

External investors, analysts, and agent users use this skill to review China A-share watchlists or portfolios, collect market and financial inputs, score value and trading conditions, and generate an offline report with data gaps and allocation references. Outputs are quantitative references, not investment advice or trade execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to use an external npm data client for market and portfolio data.

Mitigation: Run in a restricted workspace and review, preinstall, or pin the npm package before use.

Risk: The skill can store watchlist, position, snapshot, and report files locally.

Mitigation: Avoid exposing unrelated files or credentials and keep portfolio work in a dedicated workspace.

Risk: Finance outputs can be mistaken for investment advice or executable trading instructions.

Mitigation: Treat outputs as quantitative references, confirm any watchlist or paper-trade action before execution, and do not use the skill for automatic orders.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/holauv/skills/stock-portfolio-advisor)
- [README](README.md)
- [v2 input, source, and valuation fields](references/indicator-mapping.md)
- [Value scoring model v2.3.0](references/scoring-model.md)
- [Data acquisition playbook](references/data-playbook.md)
- [Backtesting, rolling calibration, and version management](references/backtesting.md)
- [A-share value analysis optimization review](references/valuation-review-2026-09-05.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, JSON files, HTML reports]

**Output Format:** [Markdown guidance with shell commands, JSON inputs and outputs, and offline HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include data provenance, model version, weights version, scenario assumptions, data gaps, and non-advice risk notes.]

## Skill Version(s):

2.3.0 (source: frontmatter, CHANGELOG, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
