## Description: <br>
一个支持AI助手读取和分析PDF文件的MCP服务器，提供PDF元数据提取、页面范围阅读和关键词搜索等功能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to read PDF content, inspect PDF metadata, retrieve selected page ranges, and search within PDFs through a remote XiaoBenYang service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PDF paths, PDF URLs, and search terms are sent to the XiaoBenYang remote backend. <br>
Mitigation: Do not use the skill with confidential PDFs, private URLs, or sensitive search terms unless the user trusts the service and its data handling. <br>
Risk: The API key is stored as a plaintext local secret. <br>
Mitigation: Avoid committing or sharing the .env file and rotate the key if it may have been exposed. <br>
Risk: The security summary flags documentation mismatch and data-flow ambiguity that require review. <br>
Mitigation: Review the skill behavior and remote-service data flow before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/read-pdf) <br>
- [Publisher profile](https://clawhub.ai/user/alinklab) <br>
- [XiaoBenYang API key service](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [Agent-facing prose derived from JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include PDF text, metadata, page excerpts, search results, success status, and API status messages.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
