## Description: <br>
Provides fund knowledge lookup and stock search by routing agent-selected tool calls to XiaoBenYang API services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent developers use this skill to answer fund knowledge questions and search stock information after providing a XiaoBenYang API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores a XiaoBenYang API key in a local .env file. <br>
Mitigation: Use a dedicated API key, keep .env out of shared folders and source control, and rotate or delete the key after use. <br>
Risk: Queries and the API key are sent to xiaobenyang.com. <br>
Mitigation: Avoid submitting sensitive personal, financial, or confidential data unless the service terms and data handling are acceptable. <br>
Risk: The artifact has rough packaging quality, including stale names and a likely invalid Python tools file. <br>
Mitigation: Review and test the installed files before relying on the skill in production workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/fund-knowledge-query) <br>
- [XiaoBenYang API key portal](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration] <br>
**Output Format:** [Markdown summaries of JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires XBY_APIKEY and sends query parameters to xiaobenyang.com; API responses are service-dependent.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
