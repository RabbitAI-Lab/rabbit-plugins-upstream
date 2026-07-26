## Description: <br>
Hugeicons MCP Server是一个基于TypeScript的服务器，提供Hugeicons图标库的集成工具和资源，支持多种平台的图标搜索、获取和使用指南。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and designers use this skill to look up Hugeicons icons, glyphs, and platform-specific usage guidance through a XiaoBenYang-backed MCP service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a XiaoBenYang API key and stores it in a local .env file. <br>
Mitigation: Install only when the publisher and third-party service are trusted, and use a scoped or revocable key where possible. <br>
Risk: Icon queries and parameters are sent to a XiaoBenYang MCP endpoint. <br>
Mitigation: Avoid sending sensitive project or customer information in icon search terms or platform requests. <br>
Risk: The artifact contains leftover references to an unrelated school-service project, which makes the package purpose ambiguous. <br>
Mitigation: Review the artifact contents and security scan result before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/hugeicons) <br>
- [XiaoBenYang API access](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Markdown, Guidance] <br>
**Output Format:** [Markdown summaries of JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a XiaoBenYang API key and sends icon query parameters to a third-party MCP endpoint.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
