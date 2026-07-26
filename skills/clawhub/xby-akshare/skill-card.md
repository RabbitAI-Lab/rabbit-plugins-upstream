## Description: <br>
股票数据服务 helps agents retrieve Chinese stock-market quotes, historical data, disclosures, fundamentals, rankings, capital flows, research reports, and finance news through a XiaoBenYang-backed API workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to query Chinese equities market summaries, individual stock data, historical K-line data, disclosures, rankings, capital flows, research reports, and finance news from an agent session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the XiaoBenYang API key, stock queries, and optional token parameters to a third-party remote API. <br>
Mitigation: Install and use the skill only when that data sharing is acceptable for the intended environment and users. <br>
Risk: The skill stores the XiaoBenYang API key in a local .env file. <br>
Mitigation: Protect the workspace, use a revocable key, and rotate or remove the key if the workspace is shared or no longer needs the skill. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/alinklab/skills/xby-akshare) <br>
- [XiaoBenYang API Portal](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP Service](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [Structured JSON responses from API calls, usually summarized for the user in text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a XiaoBenYang API key; responses may include raw upstream data and API error messages.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
