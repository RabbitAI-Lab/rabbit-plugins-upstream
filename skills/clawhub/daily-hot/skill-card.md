## Description: <br>
基于Model Context Protocol (MCP)协议的全网热点趋势一站式聚合服务，支持Python实现，适用于新闻资讯、社交媒体、科技开发等多领域。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to fetch and summarize current trending topics, rankings, and news from supported Chinese and international sources through Xiaobenyang MCP API-backed tools. It is suited for news monitoring, social trend review, technology updates, consumer topics, and optional user-requested website crawling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores the Xiaobenyang API key in a local .env file. <br>
Mitigation: Use a dedicated low-value API key, keep .env out of source control, and rotate the key if it may have been exposed. <br>
Risk: The crawl_website tool can request arbitrary URLs. <br>
Mitigation: Do not use crawl_website with private, internal, authenticated, or sensitive URLs, and review requested URLs before execution. <br>
Risk: The security verdict is suspicious. <br>
Mitigation: Review the skill before installing and confirm that its API calls, credential handling, and crawling behavior match the intended deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/daily-hot) <br>
- [Publisher profile](https://clawhub.ai/user/cainingnk) <br>
- [Xiaobenyang API key site](https://xiaobenyang.com) <br>
- [Xiaobenyang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API Calls, configuration, guidance] <br>
**Output Format:** [Markdown summaries derived from JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Tool responses include success status, raw upstream payload, and a message field before the agent summarizes the result for the user.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
