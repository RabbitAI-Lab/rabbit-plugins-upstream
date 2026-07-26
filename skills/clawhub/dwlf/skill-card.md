## Description: <br>
DWLF gives an agent native access to DWLF, a market analysis platform for crypto, stocks, and forex. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andywilliams](https://clawhub.ai/user/andywilliams) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let an agent retrieve DWLF market data, technical indicators, strategy signals, backtests, portfolio data, watchlists, trade journals, chart annotations, trade plans, position sizing, and academy content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use local DWLF API keys and perform broad account changes. <br>
Mitigation: Install only if you trust DWLF and require confirmation before account-changing actions such as POST, PUT, DELETE, purge, bulk activation, settings, trade, strategy, watchlist, or API-key operations. <br>
Risk: Plaintext or shared TOOLS.md API-key storage can expose credentials. <br>
Mitigation: Prefer setting DWLF_API_KEY explicitly and remove or verify any person-specific TOOLS.md fallback before use. <br>


## Reference(s): <br>
- [DWLF skill page](https://clawhub.ai/andywilliams/skills/dwlf) <br>
- [DWLF](https://dwlf.co.uk) <br>
- [DWLF API base](https://api.dwlf.co.uk/v2) <br>
- [API endpoints reference](references/api-endpoints.md) <br>
- [Strategy builder reference](references/strategy-builder.md) <br>
- [DWLF MCP server](https://github.com/dwlf-ai/dwlf-mcp-server) <br>
- [DWLF Clawdbot skill repository](https://github.com/andywilliams/dwlf-clawdbot-skill.git) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON API payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses curl and jq through scripts/dwlf-api.sh; requires a DWLF API key for authenticated account operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
