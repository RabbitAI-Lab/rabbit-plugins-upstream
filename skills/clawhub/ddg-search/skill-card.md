## Description: <br>
一个提供DuckDuckGo网络搜索能力并具备内容抓取和解析功能的模型上下文协议（MCP）服务器。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask an agent to perform DuckDuckGo-style web searches and fetch webpage content through the xiaobenyang.com service after configuring an XBY API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is advertised as a DuckDuckGo search skill, but server security evidence says it depends on a different third-party service. <br>
Mitigation: Use the skill only when the user or deployment owner trusts xiaobenyang.com with search queries, fetched URLs, and the XBY API key. <br>
Risk: The artifact persists the XBY API key in a local .env file in plaintext. <br>
Mitigation: Prefer managed secret storage or environment injection where available, restrict local file access, and rotate the key if exposure is suspected. <br>
Risk: The server security guidance says the package should align its name, docs, code, credential handling, and dependency pinning before broad use. <br>
Mitigation: Review the service dependency, credential flow, and dependency versions before broad or production deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/ddg-search) <br>
- [ALinkLab publisher profile](https://clawhub.ai/user/alinklab) <br>
- [XiaoBenYang service site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [JSON result dictionaries with human-readable summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY API key; search queries and fetched URLs are sent to xiaobenyang.com.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter is 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
