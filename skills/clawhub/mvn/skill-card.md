## Description: <br>
Maven MCP Server是一个通过自然语言交互的AI驱动Maven依赖管理工具，提供版本检查、安全扫描和依赖分析功能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to check Maven dependency versions, list available artifact versions, scan Java projects for vulnerabilities, and analyze POM files through a natural-language workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill persists an API key in a local .env file. <br>
Mitigation: Use a limited-scope API key, remove the .env entry when finished, and prefer session-only credential handling where possible. <br>
Risk: The skill sends local project path metadata and dependency or POM details to an external XiaoBenYang service. <br>
Mitigation: Avoid running it in sensitive repositories unless that remote data flow is acceptable, and review the service trust boundary before use. <br>
Risk: Raw service responses may expose more dependency, project, or vulnerability detail than intended. <br>
Mitigation: Review returned data before sharing it and prefer versions that redact raw responses when appropriate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/mvn) <br>
- [XiaoBenYang service](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Analysis, Guidance] <br>
**Output Format:** [Markdown summary of API results and tool guidance, with raw JSON data summarized for the user] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY credential and sends Maven dependency, project path, or POM-file metadata to the XiaoBenYang service.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter: 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
