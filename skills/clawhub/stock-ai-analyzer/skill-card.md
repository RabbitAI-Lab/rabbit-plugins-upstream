## Description: <br>
Stock AI Analyzer helps agents perform fundamental research on China A-share companies, including growth quality, valuation posture, market-theme fit, governance, competitive position, and risk analysis from public market evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chinfi-codex](https://clawhub.ai/user/chinfi-codex) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to produce evidence-grounded China A-share fundamental research, including valuation framing, business-quality review, market-theme assessment, governance checks, and risk discussion. The skill is intended for public-data research workflows and explicitly keeps investment conclusions with the agent rather than deterministic scripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may access public finance-data services, create local report or cache files, and use local tracking storage. <br>
Mitigation: Install only when that access pattern is acceptable, review generated files, and verify ALPHA_PG_URL or DATABASE_URL before running tracking commands. <br>
Risk: A Tushare token may be required for data collection. <br>
Mitigation: Provide the token through the intended environment only, avoid committing token-bearing .env files, and rotate credentials if accidental exposure occurs. <br>
Risk: Stock analysis can be mistaken for financial advice or overstate confidence when data is stale or incomplete. <br>
Mitigation: Keep outputs framed as research, distinguish source facts from agent judgment, disclose missing data, and retain the skill's non-investment-advice boundary. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chinfi-codex/skills/stock-ai-analyzer) <br>
- [Deep research mode](references/deep_mode.md) <br>
- [Growth success rate framework](references/growth_success_rate.md) <br>
- [Industry valuation library](references/industry_valuation_library.md) <br>
- [Living report structure](references/living_report.md) <br>
- [Research orchestration guide](references/orchestration.md) <br>
- [Qualitative framework](references/qualitative_framework.md) <br>
- [Quantitative framework](references/quantitative_framework.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown research reports and text guidance with optional JSON evidence packs, shell commands, and rendered HTML report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses public finance data, a Tushare token when available, local report/cache files, and optional local PostgreSQL or SQLite tracking storage.] <br>

## Skill Version(s): <br>
2.2.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
