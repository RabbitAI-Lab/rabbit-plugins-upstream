## Description: <br>
一个基于模型上下文协议(MCP)的服务器，提供对Kubernetes故障排除手册的访问，支持搜索、内容获取和AI集成。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and platform engineers use this skill to search, list, and fetch Kubernetes troubleshooting runbooks through a XiaoBenYang MCP-backed API for incident response and operational support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores a user API key locally in a .env file and sends it to the XiaoBenYang API. <br>
Mitigation: Use a disposable or limited-scope API key, keep .env out of version control and backups, and install only if the XiaoBenYang service is trusted. <br>
Risk: The security summary flags unrelated Gaokao and school-search leftovers, making the package scope and provenance unclear. <br>
Mitigation: Review the package before broad use and clean or replace unrelated leftovers before production deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/kubernetes-runbooks) <br>
- [XiaoBenYang service](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [Markdown summary of JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY and depends on responses from the XiaoBenYang service.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
