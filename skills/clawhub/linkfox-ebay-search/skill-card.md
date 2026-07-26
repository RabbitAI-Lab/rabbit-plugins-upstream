## Description: <br>
Searches eBay international marketplaces through LinkFox so an agent can retrieve product listings, compare prices, review sold items, and summarize marketplace results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and commerce operators use this skill to search eBay listings across regional marketplaces, compare product prices, inspect sold or completed listings, and prepare marketplace research summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and request metadata are sent to LinkFox services using a LinkFox API key. <br>
Mitigation: Use the skill only for queries appropriate to share with LinkFox and store API keys in environment variables with normal secret-handling controls. <br>
Risk: Each search may spend LinkFox credits, and repeated fresh searches can increase cost. <br>
Mitigation: Rely on the documented cache when suitable and confirm with the user before additional searches, pagination, or cache bypasses that could spend more credits. <br>
Risk: Full API responses are written to local JSON files and may contain search results or operational metadata. <br>
Mitigation: Keep the generated linkfox data directory out of shared repositories and remove saved responses when they are no longer needed. <br>
Risk: The API gateway can be redirected with LINKFOX_TOOL_GATEWAY. <br>
Mitigation: Leave the default gateway in place unless the alternate destination is trusted and approved. <br>
Risk: Automatic feedback or onboarding behavior can contact additional LinkFox endpoints or prompt installation of another LinkFox skill. <br>
Mitigation: Review this behavior before installation and disable or avoid it where the deployment requires tighter outbound network control. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-ebay-search) <br>
- [eBay 商品搜索 API 参考](references/api.md) <br>
- [LinkFox Skills guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>
- [LinkFox account portal](https://os.linkfox.com/) <br>
- [LinkFox Skills](https://skill.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown summaries with optional JSON responses and saved JSON data files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search calls may spend LinkFox credits, use a 24-hour local cache, and save full API responses under a local linkfox data directory.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
