## Description: <br>
一个提供QAnon帖子数据集访问的MCP服务器，用于人类学和社会学研究，支持搜索、过滤和分析功能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers and analysts use this skill to query and summarize QAnon post data by post ID, keyword, date range, author ID, and word-frequency views through the XiaoBenYang API service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan verdict is suspicious because the package mixes QAnon dataset behavior with unrelated Gaokao/XiaoBenYang school-service remnants. <br>
Mitigation: Review the package contents and confirm the upstream service and exposed tools before installation. <br>
Risk: The skill stores the XiaoBenYang API key in a local .env file as plaintext. <br>
Mitigation: Use a minimally privileged API key, avoid sharing the workspace, and remove the .env file when the skill is no longer needed. <br>
Risk: The skill depends on a third-party API service for results. <br>
Mitigation: Install only if you trust the XiaoBenYang service and are comfortable sending requests and credentials to it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/qanon) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, analysis, configuration, guidance] <br>
**Output Format:** [Markdown summaries derived from JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY credential; API results depend on the XiaoBenYang service.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
