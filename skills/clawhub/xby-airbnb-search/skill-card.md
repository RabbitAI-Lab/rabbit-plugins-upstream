## Description: <br>
一个提供高级筛选功能和详细房源信息的Airbnb搜索桌面扩展，适用于旅行规划和房源研究。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travel planners and property researchers use this skill to search Airbnb listings with filters and retrieve listing details through the XiaoBenYang API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores the XiaoBenYang API key in a local plaintext .env file. <br>
Mitigation: Use a scoped or revocable API key, protect the local environment file, and remove the key when the skill is no longer needed. <br>
Risk: The Airbnb tools expose an ignoreRobotsText option. <br>
Mitigation: Review or disable this option before use and keep requests aligned with applicable site rules and policies. <br>
Risk: Some artifact text and code comments still refer to an unrelated gaokao skill. <br>
Mitigation: Have the publisher clean up or clarify stale references before relying on the package in a managed environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/xby-airbnb-search) <br>
- [XiaoBenYang API key page](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration guidance] <br>
**Output Format:** [Markdown summaries of JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a XiaoBenYang API key before calls can be made.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
