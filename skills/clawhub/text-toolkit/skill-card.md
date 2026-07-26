## Description: <br>
一个提供文本转换、格式化和分析功能的MCP服务器，可直接集成到开发工作流中。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and other ClawHub users use this skill to perform text conversion, encoding and decoding, formatting, counting, hashing, UUID, lorem ipsum, and regex tasks through an external MCP API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Routine text operations may send private documents, source code, credentials, HMAC keys, or regulated data to an external API provider. <br>
Mitigation: Use only with data that may be processed off-machine, and avoid private documents, source code, credentials, HMAC keys, and regulated data unless the provider is trusted. <br>
Risk: The skill stores an API key in a local .env file. <br>
Mitigation: Use a scoped, revocable API key and avoid persisting it in a project .env file when possible. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/text-toolkit) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP service](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [JSON tool results summarized as user-facing text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY and sends tool parameters to an external API.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter is 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
