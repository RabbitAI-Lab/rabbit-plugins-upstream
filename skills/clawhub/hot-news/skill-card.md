## Description: <br>
热点聚合服务 aggregates real-time hot-news and ranking feeds through the XiaoBenYang MCP API across technology, business, social, media, and consumer sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask an agent for current trending topics, rankings, and news lists from supported Chinese and international sources. The skill routes requests to a XiaoBenYang MCP API tool and summarizes the returned JSON for the user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores the XiaoBenYang API key as plaintext in a local .env file. <br>
Mitigation: Use a dedicated low-privilege API key, avoid using the skill in repositories where .env may be committed, and prefer secure secret storage when available. <br>
Risk: Server security evidence reports leftover identifiers from another product and a broken tools.py file. <br>
Mitigation: Review the source and test imports and tool calls before installation; consider waiting for a repaired release for production workflows. <br>
Risk: Server security guidance notes unpinned dependencies. <br>
Mitigation: Install in an isolated environment and pin or lock dependency versions before broader deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/hot-news) <br>
- [XiaoBenYang API key portal](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown summaries derived from upstream JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a XiaoBenYang API key; tool calls return success status, raw response data, and a status message.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
