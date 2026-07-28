## Description: <br>
Fetches Chinese financial-market data and investment research information across A-shares, Hong Kong stocks, funds, indices, financial statements, announcements, research reports, news, macroeconomics, sectors, themes, industry chains, and market statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kenneth-bro](https://clawhub.ai/user/kenneth-bro) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External analysts, researchers, and developers use this skill to retrieve, compare, and export structured Chinese market data for financial research workflows. It is intended for data retrieval and research support, not direct trading advice, automated trading, or order execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys can be exposed if copied directly into shell history or logs during non-interactive setup. <br>
Mitigation: Use an interactive setup flow or a secure secret-management mechanism instead of putting API keys directly on the command line. <br>
Risk: Skipping verification during setup can bypass checks the user may rely on before using the CLI. <br>
Mitigation: Avoid `--skip-verify` unless the user understands why it is needed and has reviewed the setup path. <br>
Risk: Trading-signal and financial-data outputs could be mistaken for investment advice. <br>
Mitigation: Treat outputs as research data only, confirm source coverage and recency, and avoid presenting the skill as a substitute for professional investment judgment. <br>
Risk: Free-text recognition endpoints may receive confidential account, portfolio, or personal financial details. <br>
Mitigation: Do not send confidential financial or personal information unless the provider's privacy controls have been reviewed and accepted. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data) <br>
- [API Reference Index](docs/references-index.en.md) <br>
- [Chinese API Reference Index](docs/references-index.md) <br>
- [Basic Data Reference](references/基础数据.md) <br>
- [Market Data Reference](references/市场数据.md) <br>
- [Announcements Reference](references/公告.md) <br>
- [Large Model Corpus Reference](references/大模型语料.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline CLI commands and structured data summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference CLI endpoints and parameters for retrieving financial datasets; API responses depend on network access, provider permissions, and user-supplied query scope.] <br>

## Skill Version(s): <br>
1.8.52 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
