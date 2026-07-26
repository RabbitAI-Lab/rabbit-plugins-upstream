## Description: <br>
Atlas Docs MCP服务器为AI助手提供库和框架的技术文档，将官方文档处理为适合LLM使用的Markdown版本，适用于Cursor、Cline、Windsurf等MCP兼容的LLM客户端。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI assistant users use this skill to discover available documentation sets, search library and framework documentation, and retrieve LLM-friendly Markdown documentation pages or full documentation content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release security summary reports a mixed service identity, which may make the intended backend and behavior unclear. <br>
Mitigation: Review the publisher's documentation and install only after the publisher clarifies the backend and resolves the service-identity mismatch. <br>
Risk: The skill asks for and persists an API key before making requests. <br>
Mitigation: Do not provide an API key until the publisher documents credential storage and deletion; if use is approved, provide only a scoped key and rotate it after testing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/atlas-docs) <br>
- [Publisher profile](https://clawhub.ai/user/cainingnk) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown or structured text summarized from upstream JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY before use; full-document retrieval may return a large amount of text.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
