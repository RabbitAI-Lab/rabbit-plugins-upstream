## Description: <br>
Fetches Chinese stock and futures market data via the Tushare API, including quotes, futures data, company fundamentals, and macroeconomic indicators. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manifoldor](https://clawhub.ai/user/manifoldor) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agents use this skill to fetch Chinese equity, futures, company, fund-flow, and macroeconomic data from Tushare after configuring a Tushare API token. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Tushare API token. <br>
Mitigation: Treat TUSHARE_TOKEN like a password, keep it out of shared files and logs, and use a controlled Python environment. <br>
Risk: Some data access depends on Tushare account permissions, paid access, or service availability. <br>
Mitigation: Confirm the account has the required Tushare permissions and verify returned data before relying on it. <br>
Risk: The artifact's registration link includes a referral-style parameter. <br>
Mitigation: Use the main Tushare site directly if you do not want to use a referral-style registration URL. <br>


## Reference(s): <br>
- [Tushare Stock API Reference](references/stock_api.md) <br>
- [Tushare Futures API Reference](references/futures_api.md) <br>
- [Tushare Official Website](https://tushare.pro) <br>
- [Tushare Stock Documentation](https://tushare.pro/document/2?doc_id=14) <br>
- [Tushare Futures Documentation](https://tushare.pro/document/2?doc_id=134) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Text, JSON] <br>
**Output Format:** [Markdown guidance with shell commands; the bundled script prints terminal text tables and JSON for realtime quotes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, pip3, the tushare and pandas packages, and the TUSHARE_TOKEN environment variable.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
