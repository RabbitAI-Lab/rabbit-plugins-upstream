## Description: <br>
Provides an API-key-backed toolset for retrieving Hacker News stories, comments, user information, and story search results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to ask an agent for Hacker News story lists, story details with comments, user profiles, and search results through the configured third-party MCP service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a third-party API key and may store it in a local plaintext .env file. <br>
Mitigation: Use a low-privilege or disposable key, review the .env file after use, and avoid sharing workspaces that contain the saved key. <br>
Risk: Requests are routed through the external xiaobenyang MCP service rather than directly to public Hacker News APIs. <br>
Mitigation: Install only if you trust the xiaobenyang service, and verify important results before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/hnews) <br>
- [XiaoBenYang API key service](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Markdown, Guidance] <br>
**Output Format:** [Markdown summaries derived from JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a third-party API key and may persist it in a local plaintext .env file.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter is 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
