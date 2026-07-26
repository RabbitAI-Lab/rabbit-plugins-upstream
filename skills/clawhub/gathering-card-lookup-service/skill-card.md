## Description: <br>
一个基于Model Context Protocol (MCP)的服务端，提供万智牌中文卡牌信息的查询和搜索功能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Players, collectors, and agents can use this skill to look up Chinese Magic: The Gathering card information, search cards with query syntax, browse sets, and retrieve set card lists through the XiaoBenYang API. The skill requires an API key before use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads and writes XBY_APIKEY in a local .env file. <br>
Mitigation: Use a restricted or throwaway API key and review local credential storage before installation. <br>
Risk: The security summary flags an image-composition tool that is not clearly disclosed by the stated card lookup purpose. <br>
Mitigation: Review the hzls tool before deployment and require the publisher to disclose or remove it if it is not needed. <br>
Risk: Dependencies are version-ranged rather than pinned. <br>
Mitigation: Install in an isolated environment and pin or lock dependencies before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/gathering-card-lookup-service) <br>
- [XiaoBenYang API key page](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration] <br>
**Output Format:** [Tool result dictionaries with raw JSON data, success status, and status message; agents typically summarize the raw data as text or Markdown.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires XBY_APIKEY; lookup and search results depend on the upstream XiaoBenYang service.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
