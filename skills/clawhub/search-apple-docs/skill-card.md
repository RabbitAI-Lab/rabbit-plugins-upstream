## Description: <br>
通过模型上下文协议（MCP）访问苹果官方开发者文档、框架、API及WWDC视频，支持AI驱动的自然语言查询，提供Swift/Objective-C代码示例和技术指南。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to search Apple Developer Documentation, inspect Apple framework APIs, review platform compatibility, and retrieve WWDC transcripts or code examples through a XiaoBenYang-backed MCP API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Apple documentation queries and a XiaoBenYang API key to a third-party backend, and may store the key in a local .env file. <br>
Mitigation: Use a dedicated API key, keep the .env file out of source control, and rotate or delete the key when you stop using the skill. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/alinklab/skills/search-apple-docs) <br>
- [Apple Developer Documentation](https://developer.apple.com/documentation/) <br>
- [XiaoBenYang service](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown summaries with structured API result data and code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a XiaoBenYang API key; tool responses may include raw API result fields for the agent to summarize.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
