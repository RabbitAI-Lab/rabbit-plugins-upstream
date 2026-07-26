## Description: <br>
WHOIS查询服务 helps agents look up domain registration details, refresh WHOIS server data, and list supported top-level domains through a XiaoBenYang MCP-backed API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to retrieve domain registration details, nameservers, registrar data, status values, and supported TLD information from a third-party WHOIS service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a XiaoBenYang API key and may save it in a local plaintext .env file. <br>
Mitigation: Prefer providing the key through a secure environment or secret manager, and remove any local .env entry when it is no longer needed. <br>
Risk: Domain lookup requests are sent through mcp.xiaobenyang.com, a third-party service. <br>
Mitigation: Use the skill only when sending queried domains to that service is acceptable for the intended workflow. <br>
Risk: Raw WHOIS output can contain personal registration data. <br>
Mitigation: Request raw WHOIS data only when necessary and handle returned registration data according to privacy and retention requirements. <br>
Risk: Server security evidence reports inconsistent copied documentation. <br>
Mitigation: Review the tool behavior and generated output before relying on the skill in production workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/who-is) <br>
- [XiaoBenYang API key portal](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [Markdown summaries derived from tool-returned JSON dictionaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Tool results include success, message, and raw fields; raw WHOIS output may be included when requested.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact frontmatter states 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
