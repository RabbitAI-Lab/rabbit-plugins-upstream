## Description: <br>
drand-mcp-server是一个提供可验证随机数的服务，用于AI应用中的模型驱动流程，支持通过时间或轮次获取随机数。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI application builders use this skill to retrieve drand quicknet randomness for the latest round, a specific round, or a specific time. Use requires a XiaoBenYang API key and should include independent verification when high-integrity randomness is required. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security evidence says the skill presents itself as a drand randomness tool but routes through XiaoBenYang. <br>
Mitigation: Install only when intentionally using XiaoBenYang as the proxy and independently verify returned drand values for high-integrity use cases. <br>
Risk: Security evidence says the skill asks for an API key and stores it locally in plaintext .env. <br>
Mitigation: Use a least-privilege key, avoid shared workspaces, rotate exposed keys, and remove .env secrets after use. <br>
Risk: Security evidence notes unrelated Gaokao template artifacts and mismatches. <br>
Mitigation: Review the artifact before deployment and confirm the documented tool behavior matches the intended randomness workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/drand) <br>
- [Publisher profile](https://clawhub.ai/user/alinklab) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance, Configuration instructions] <br>
**Output Format:** [Markdown summary of JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns raw upstream API data with success and message fields; requires an API key before calls can be made.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
