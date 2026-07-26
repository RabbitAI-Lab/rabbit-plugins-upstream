## Description: <br>
Ask a Legend gives an agent one legendary trader's method-based read on a market symbol, using fetched market data and presenting the result as analysis rather than a trading signal. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fxdavid-offbeatforex](https://clawhub.ai/user/fxdavid-offbeatforex) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Traders, analysts, and finance-focused agents use this skill to request a single legendary trader-style analysis for forex, crypto, stock, or other market symbols. It is intended as a second opinion and explicitly avoids presenting its output as financial advice or a trading signal. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automatically installs and updates external code before running analysis. <br>
Mitigation: Review the upstream repositories and setup script before installation, and install only in environments where cloning external repositories and installing Python packages is acceptable. <br>
Risk: The skill may store an optional TradingView API key in local files under ~/.tlc/.env. <br>
Mitigation: Enter secrets directly into the local file rather than chat, protect the ~/.tlc directory, and remove the configuration when the persistent state is no longer needed. <br>
Risk: Trading analysis can be mistaken for actionable financial advice. <br>
Mitigation: Treat outputs as a second opinion only, confirm source market data, and avoid relying on generated analysis as a trading signal. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fxdavid-offbeatforex/skills/ask-a-legend) <br>
- [Server-resolved GitHub import](https://github.com/FXDavid-OffbeatForex/tlc-hermes-skills/tree/main/skills/ask-a-legend) <br>
- [TLC project homepage](https://github.com/FXDavid-OffbeatForex/TLC) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown analysis with a JSON ballot block] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local setup and market-data access; if data fetching fails, it should report the failure instead of fabricating prices or indicators.] <br>

## Skill Version(s): <br>
0.1.0 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
