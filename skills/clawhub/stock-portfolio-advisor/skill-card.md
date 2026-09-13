## Description:

Analyzes A-share watchlists and holdings, gathers market, financial, risk, and news evidence, computes sector-aware value and trading-environment scores, reports fundamental valuation scenarios, data gaps, and risk-policy-constrained allocation references, and generates an offline HTML report without placing trades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[holauv](https://clawhub.ai/user/holauv)

### License/Terms of Use:

MIT

## Use Case:

External users and analysts use this skill to review A-share watchlists or portfolios, produce traceable valuation scores, identify missing data, and prepare allocation references constrained by a user's risk policy. It is intended for analysis and reporting, not automated trading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run an external npm data client during market-data collection.

Mitigation: Install and run it only after trusting the npm package and registry path, preferably in a restricted workspace.

Risk: A snapshot-write issue could overwrite local portfolio JSON files when processing untrusted result data.

Mitigation: Use snapshot commands only with trusted result JSON after validating dates as `YYYY-MM-DD` and constraining writes to the intended history directory.

Risk: Financial analysis outputs can be mistaken for investment advice or trading instructions.

Mitigation: Present outputs as analytical references, keep the no-auto-trading boundary visible, and require user review before any portfolio action.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/HoLauv/stock-portfolio-advisor)
- [ClawHub skill page](https://clawhub.ai/holauv/skills/stock-portfolio-advisor)
- [Indicator mapping](references/indicator-mapping.md)
- [Scoring model](references/scoring-model.md)
- [Data playbook](references/data-playbook.md)
- [Backtesting](references/backtesting.md)
- [Valuation review](references/valuation-review-2026-09-05.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell command snippets, JSON inputs and outputs, and generated HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include stock scoring summaries, valuation scenarios, data-gap notes, allocation references, snapshots, and offline reports; outputs are analytical references and not trade orders.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata); artifact frontmatter and README report 2.1.0

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
