## Description: <br>
提供菲律宾标准地理编码（PSGC）API访问的模型上下文协议（MCP）服务器，包含完整的菲律宾地理层级数据。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to query Philippines Standard Geographic Code data, including island groups, regions, provinces, cities, municipalities, barangays, hierarchy lookup, name search, and code validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores an API key in a local plaintext .env file. <br>
Mitigation: Prefer setting XBY_APIKEY through the runtime environment or a managed secret store, and avoid committing local .env files. <br>
Risk: The skill routes requests through a broadly scoped third-party MCP-style service. <br>
Mitigation: Install only if you trust xiaobenyang.com with the API key and review its behavior before use in sensitive workspaces. <br>
Risk: Security evidence flags under-disclosed, leftover unrelated configuration. <br>
Mitigation: Review the generic call_api path and leftover gaokao/template references before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/philippine-geocoding) <br>
- [XiaoBenYang API provider](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown summaries derived from JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY credential for upstream API access.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
