## Description:

Scores China A-share watchlists and holdings with deterministic sector-routed value scoring, separate trading-environment scoring, scenario valuation, data-gap reporting, constrained allocation references, and offline HTML reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[holauv](https://clawhub.ai/user/holauv)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to review China A-share watchlists or holdings, gather and track market and financial inputs, run deterministic scoring and scenario valuation, and produce portfolio allocation references and offline reports. It does not automatically place trades and its outputs are not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to run an external npm data client for market and financial data.

Mitigation: Review the client before use, run the skill in a restricted workspace, or replace the client with a preinstalled and verified data tool.

Risk: Watchlist, holding, snapshot, and report files may contain sensitive portfolio information.

Mitigation: Avoid exposing unrelated credentials or private files to the agent, keep generated files in a restricted workspace, and review reports before sharing.

Risk: Generated reports and allocation references can be mistaken for trading instructions or financial advice.

Mitigation: Treat outputs as financial analysis only, require explicit review before watchlist or simulated-trade actions, and do not rely on the skill for automatic trading.

Risk: Security guidance notes snapshot date validation and HTML escaping issues for hostile or shared input files.

Mitigation: Fix those issues before relying on untrusted inputs or using generated reports in shared environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/holauv/skills/stock-portfolio-advisor)
- [README](README.md)
- [Scoring Model](references/scoring-model.md)
- [Indicator Mapping](references/indicator-mapping.md)
- [Data Playbook](references/data-playbook.md)
- [Backtesting](references/backtesting.md)
- [Valuation Review 2026-09-05](references/valuation-review-2026-09-05.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown summaries and tables, JSON scoring inputs/results, shell commands, configuration updates, and offline HTML reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic scoring output; allocation is a constrained reference, not a trade order.]

## Skill Version(s):

2.4.0 (source: frontmatter, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
