## Description: <br>
智能模板发现助手 - 为 AI 应用提供强大的 epub360 模板搜索能力 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to search epub360 templates by keyword and receive structured template results for AI-assisted template discovery workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles a user-provided API key and stores it in a local plaintext .env file. <br>
Mitigation: Use only in environments where plaintext local secret storage is acceptable, or move the key to environment variables or a secure secret store before deployment. <br>
Risk: The security evidence reports inconsistent routing and documentation signals. <br>
Mitigation: Review the tool routing and documentation before deployment so users understand which template-search function is being called. <br>
Risk: The security evidence recommends clearer network and file-write permissions and dependency maintenance. <br>
Mitigation: Declare required network and file-write behavior, and pin or update dependencies as part of release review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/epub-template-server) <br>
- [Publisher profile](https://clawhub.ai/user/alinklab) <br>
- [XiaoBenYang API key portal](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API Calls, configuration, guidance] <br>
**Output Format:** [Markdown summary of JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided XBY_APIKEY before calling the upstream template search API.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
