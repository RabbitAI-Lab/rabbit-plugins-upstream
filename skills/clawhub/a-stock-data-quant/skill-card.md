## Description:

Provides a finance research and data-analysis skill for A-share, Hong Kong, U.S. stock, fund, ETF, futures, options, macro, valuation, quant factor, backtesting, screening, and research-report workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jangviktor-web](https://clawhub.ai/user/jangviktor-web)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve market and financial data, run quantitative analysis and backtests, evaluate securities, and draft structured finance research reports. It is intended for finance workflows where outputs should be checked against current market data and reviewed before investment use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled or shared API credentials could expose provider access or create unclear authorization boundaries.

Mitigation: Remove bundled credentials before deployment and require each installation to supply its own provider keys through a protected secret store.

Risk: Credential persistence may store sensitive API keys outside the user's expected secret-management boundary.

Mitigation: Disable cross-session credential persistence unless the platform provides protected storage, and prevent credentials from being written to repositories, logs, prompts, or user-visible outputs.

Risk: Broad automatic activation can route many finance requests through external data providers or scripts.

Mitigation: Review activation rules before installation and require explicit user confirmation before enabling fallback providers or authenticated data sources.

Risk: Dependencies are specified with lower bounds rather than exact pins, which can change installed code over time.

Mitigation: Install in an isolated environment, pin and review dependencies, and avoid automatic package installation in production workflows.

Risk: Market data, model outputs, and investment analysis can be stale, incomplete, or misleading.

Mitigation: Cross-check outputs against authoritative current data sources and require human review before making trading, portfolio, or investment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jangviktor-web/skills/a-stock-data-quant)
- [A-stock full reference](references/a-stock-full.md)
- [Connector guidance](CONNECTORS.md)
- [HiThink Finance overview](references/hithink-finance/00-overview.md)
- [HiThink Finance API](references/hithink-finance/api.md)
- [MX finance data skill](references/mx-skills/mx-finance-data/SKILL.md)
- [MX finance search skill](references/mx-skills/mx-finance-search/SKILL.md)
- [MX macro data skill](references/mx-skills/mx-macro-data/SKILL.md)
- [MX stocks screener skill](references/mx-skills/mx-stocks-screener/SKILL.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands, structured tables, and optional generated data or report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate local HTML charts, Markdown reports, Excel files, cached data, and script outputs depending on the selected workflow.]

## Skill Version(s):

3.8.0 (source: frontmatter, manifest, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
