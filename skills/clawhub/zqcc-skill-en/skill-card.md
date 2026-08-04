## Description: <br>
English edition of the zqcc Qichacha relay skill for querying Chinese company registration, shareholders, contacts, risks, intellectual property, operations, executives, and historical records through the zqcc MCP and Chat API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shijingyu](https://clawhub.ai/user/shijingyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to query Qichacha-backed Chinese enterprise data, perform company due diligence, check legal and operational risks, and configure MCP or Chat API access with a zqcc AppKey. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid zqcc AppKey, and successful business calls or Chat API answers can consume credits. <br>
Mitigation: Check the zqcc console for balance and call ledger, avoid unnecessary retries, and do not retry 401 or 402 responses automatically. <br>
Risk: The AppKey is a secret credential and the config command prints a usable Authorization header. <br>
Mitigation: Keep ZQCC_APP_KEY out of prompts, logs, screenshots, repositories, and shared terminal output; treat generated MCP configuration as secret-bearing. <br>
Risk: Queries and responses may contain company contacts, litigation, executive, or other sensitive enterprise research data. <br>
Mitigation: Use separate session IDs for separate users or matters and return only the data needed for the task. <br>


## Reference(s): <br>
- [zqcc Public API Reference](references/api.md) <br>
- [zqcc Tool Catalog](references/tools.md) <br>
- [zqcc Service Homepage](https://zqcc.mkstone.club) <br>
- [zqcc MCP Endpoint](https://zqcc.mkstone.club/mcp/stream) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command output from the zqcc API wrapper] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include enterprise data returned by the zqcc MCP or Chat API; successful business calls can consume paid zqcc credits.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
