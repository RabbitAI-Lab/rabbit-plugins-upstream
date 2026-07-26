## Description: <br>
一个用于访问英国国家统计局(ONS) Beta API的模型上下文协议(MCP)服务器，无需API密钥即可获取官方统计数据。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query ONS dataset metadata, search datasets, retrieve dataset details, and request observations or latest data through the packaged tool functions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence says the skill is advertised as keyless official ONS access but asks for and stores a xiaobenyang API key and sends requests to a xiaobenyang endpoint. <br>
Mitigation: Install only when the user intentionally trusts xiaobenyang as the backend, is comfortable sending queries and the API key there, and accepts local .env storage. <br>
Risk: The skill may lead users to provide credentials beyond what they expected for public ONS statistics access. <br>
Mitigation: Do not provide unrelated credentials; prefer a direct official ONS integration for keyless public statistics access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/ons-data) <br>
- [XiaoBenYang service](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown summary of JSON tool responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Tool responses include success status, raw upstream data, and a status message.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
