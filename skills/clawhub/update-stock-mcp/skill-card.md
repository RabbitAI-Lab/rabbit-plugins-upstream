## Description: <br>
Update Stock MCP runs an MCP stdio service that creates, updates, and queries local DuckDB databases for China A-share stock data, with optional QuantAll integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mifochen](https://clawhub.ai/user/mifochen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to prepare and maintain local China A-share market data in DuckDB, then query price data or point QuantAll at the prepared database. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores the Tushare API token in a plaintext local file. <br>
Mitigation: Use a dedicated token with the minimum practical privileges, restrict local file permissions, and remove or rotate the token when the skill is no longer needed. <br>
Risk: The skill can write local database and configuration files. <br>
Mitigation: Run it in a controlled workspace, choose database paths deliberately, and back up any existing DuckDB files before updates. <br>
Risk: The skill can start a background QuantAll MCP service on 127.0.0.1:8686. <br>
Mitigation: Review the Start_QuantAll behavior before use, confirm that the local port is expected, and know how to stop the spawned service. <br>
Risk: The skill contacts external finance-data providers Tushare and baostock. <br>
Mitigation: Use it only where those network calls and the providers' terms are acceptable for the intended workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mifochen/skills/update-stock-mcp) <br>
- [Publisher profile](https://clawhub.ai/user/mifochen) <br>
- [Tushare registration](https://tushare.pro/register) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration snippets, shell commands, and MCP tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can create or update local DuckDB databases and local configuration files when the MCP tools are executed.] <br>

## Skill Version(s): <br>
2.2.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
