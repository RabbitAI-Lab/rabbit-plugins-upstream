## Description: <br>
Fetch Chinese stock and futures market data via the Tushare API, including stock quotes, futures data, company fundamentals, and macroeconomic indicators. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wdblink](https://clawhub.ai/user/wdblink) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and financial-data users use this skill to query Chinese stock, futures, company, and macroeconomic data through Tushare-backed commands. It is useful when an agent needs market-data retrieval guidance and command examples for Chinese markets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A Tushare API token can be exposed if users paste credentials into shared chats, logs, shell history, or screenshots. <br>
Mitigation: Use a dedicated Tushare token where possible and avoid sharing token values in prompts, logs, or screenshots. <br>
Risk: Installing Python dependencies into a shared environment can affect other Python tools. <br>
Mitigation: Install tushare and pandas in a virtual environment when practical. <br>
Risk: Market data may be unavailable, permission-gated, delayed, or unsuitable as the sole basis for financial decisions. <br>
Mitigation: Check Tushare account permissions and verify important market data against authoritative sources before acting on it. <br>


## Reference(s): <br>
- [Tushare Stock API Reference](references/stock_api.md) <br>
- [Tushare Futures API Reference](references/futures_api.md) <br>
- [Tushare Official Site](https://tushare.pro) <br>
- [Tushare Stock API Documentation](https://tushare.pro/document/2?doc_id=14) <br>
- [Tushare Futures API Documentation](https://tushare.pro/document/2?doc_id=134) <br>
- [Tushare Registration](https://tushare.pro/register) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and CLI text or JSON data output descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided TUSHARE_TOKEN and Python dependencies; some Tushare endpoints may require account points or paid permissions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
