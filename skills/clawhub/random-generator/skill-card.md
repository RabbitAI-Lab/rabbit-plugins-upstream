## Description: <br>
一款符合MCP协议的加密安全随机数生成服务器，适用于AI应用、LLM及其他需要高质量随机数的系统。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to request random integers, floats, bytes, UUIDs, strings, choices, and booleans through a Xiaobenyang-backed MCP API. It is intended for workflows that need random values but can rely on a third-party remote service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Xiaobenyang API key and saves it in a local .env file. <br>
Mitigation: Install only when local secret storage is acceptable, use a scoped API key when possible, and avoid sharing the workspace or .env contents. <br>
Risk: Random values are produced through a third-party remote service. <br>
Mitigation: Do not use outputs for security-critical tokens, keys, or identifiers unless the provider, API behavior, and transport assumptions have been independently verified. <br>
Risk: Server security evidence marks the release as suspicious and notes inconsistent copied project references. <br>
Mitigation: Review the skill behavior and documentation before deployment, especially the API-key flow, remote dependency, and copied references. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/alinklab/skills/random-generator) <br>
- [Publisher Profile](https://clawhub.ai/user/alinklab) <br>
- [Xiaobenyang API Key Portal](https://xiaobenyang.com) <br>
- [Xiaobenyang MCP API Endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, API calls, guidance] <br>
**Output Format:** [Markdown summary of JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns raw upstream API data with success status and message fields.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
