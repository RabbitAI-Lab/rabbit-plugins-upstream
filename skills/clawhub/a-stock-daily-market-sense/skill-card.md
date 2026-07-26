## Description: <br>
Generates post-market A-share market research reports from Tushare Pro daily market data, Baostock style-index data, deterministic evidence packs, factor backtests, catalyst research, lifecycle tracking, and optional HTML rendering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chinfi-codex](https://clawhub.ai/user/chinfi-codex) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Market analysts, research agents, and developers use this skill to generate A-share daily or historical market reviews covering index trend, style rotation, turnover concentration, money effect, rising themes, abnormal high-volume declines, feature groups, and factor-mining research. The artifact states that it does not provide buy, sell, stop-loss, target-price, automated trading, portfolio-optimization, or single-stock fundamental advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports broad local credential lookup for market-data and search API credentials. <br>
Mitigation: Set required credentials explicitly in the runtime environment and avoid running the skill from directories that contain unrelated .env files. <br>
Risk: The security scan notes outbound calls to third-party market-data and search providers and proxy environment changes in the daily runner. <br>
Mitigation: Review provider access, proxy behavior, and egress expectations before using the daily runner. <br>
Risk: The skill writes report, evidence, module-context, and lifecycle files and uses a PostgreSQL alpha-data database. <br>
Mitigation: Run it only with an intended PostgreSQL database and report workspace, then review generated files before sharing or deploying outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chinfi-codex/skills/a-stock-daily-market-sense) <br>
- [CLI reference](references/cli_reference.md) <br>
- [Report template](references/report_template.md) <br>
- [Theme lifecycle reference](references/theme_lifecycle.md) <br>
- [Catalyst and subline mining methodology](references/methodology/catalyst_subline_mining.md) <br>
- [Factor mining methodology](references/methodology/factor_mining.md) <br>
- [Output discipline](references/methodology/output_discipline.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, HTML, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports, JSON evidence packs and module contexts, optional HTML reports, and shell commands with configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces deterministic evidence files before model-authored report sections; optional HTML rendering adds presentation charts without changing report conclusions.] <br>

## Skill Version(s): <br>
2.0.2 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
