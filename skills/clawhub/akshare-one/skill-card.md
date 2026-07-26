## Description: <br>
基于akshare-one的MCP服务器，提供中国股票市场数据的全面接口，包括历史数据、实时数据、新闻数据和财务报表等金融信息。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and analysts use this skill to route stock-data requests to a Xiaobenyang MCP API service for Chinese market history, real-time quotes, company news, financial statements, insider trading data, financial metrics, and trading-day time information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for a third-party Xiaobenyang API key and stores it in a local .env file. <br>
Mitigation: Install only if the user trusts the Xiaobenyang service, use a low-privilege or disposable key where possible, avoid shared keys, inspect or remove the .env entry after use, and rotate the key after use in a shared or synced workspace. <br>
Risk: Security evidence flags confusing leftover Gaokao/XBY configuration. <br>
Mitigation: Review the configuration values and service identity before use so the requested API endpoint, MCP ID, and data domain match the intended stock-data workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/akshare-one) <br>
- [Xiaobenyang API service](https://xiaobenyang.com) <br>
- [Xiaobenyang MCP endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Markdown, Guidance] <br>
**Output Format:** [Markdown summaries of JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Xiaobenyang API key and returns raw upstream API data with success and status messages.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
