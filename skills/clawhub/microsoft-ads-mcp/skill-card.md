## Description: <br>
Create and manage Microsoft Advertising campaigns (Bing Ads / DuckDuckGo Ads) via MCP server - campaigns, ad groups, keywords, ads, and reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bit-of-a-shambles](https://clawhub.ai/user/bit-of-a-shambles) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and advertising operators use this skill to configure an MCP connection for Microsoft Advertising and manage campaigns, ad groups, keywords, ads, and reporting from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control real Microsoft Advertising campaigns through an external MCP server. <br>
Mitigation: Inspect the linked MCP server and Python dependencies, use an isolated environment, and require explicit human review before activating campaigns, changing bids, adding keywords, or creating ads. <br>
Risk: Microsoft Ads credentials and mcporter configuration may expose advertising account access if mishandled. <br>
Mitigation: Protect the mcporter config and Microsoft Ads credentials, and test with paused or low-budget campaigns before broader use. <br>


## Reference(s): <br>
- [Microsoft Ads MCP server homepage](https://github.com/Duartemartins/microsoft-ads-mcp-server) <br>
- [Microsoft Advertising](https://ads.microsoft.com) <br>
- [Microsoft Advertising developer portal](https://developers.ads.microsoft.com) <br>
- [FastMCP](https://github.com/jlowin/fastmcp) <br>
- [Bing Ads Python SDK](https://github.com/BingAds/BingAds-Python-SDK) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes MCP command examples for Microsoft Ads account, campaign, keyword, ad, and reporting operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
