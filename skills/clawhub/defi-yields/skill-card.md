## Description: <br>
DeFi收益分析服务 helps AI agents retrieve and summarize DeFi yield-pool opportunities from DefiLlama, including TVL, APY, 30-day mean APY, and prediction data with optional chain or project filters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and AI agents use this skill to query DeFi yield pools, filter by blockchain or project, and present key metrics for yield exploration. Treat the results as informational analysis rather than financial advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may store the XBY API key in a local .env file. <br>
Mitigation: Use a low-privilege API key, avoid shared workspaces, and remove or rotate the key after use. <br>
Risk: The security summary reports mismatched leftover gaokao/search_schools instructions that make the real data flow unclear. <br>
Mitigation: Inspect the artifact before installing and remove or reconcile leftover instructions before using it with credentials or financial workflow context. <br>
Risk: The security verdict is suspicious pending review. <br>
Mitigation: Review before installing and run the skill in a least-privileged environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/defi-yields) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API base](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, configuration, guidance] <br>
**Output Format:** [Markdown or structured JSON summaries derived from upstream API responses] <br>
**Output Parameters:** [1D; optional chain and project filters] <br>
**Other Properties Related to Output:** [Requires XBY_APIKEY; the artifact can persist the key to a local .env file.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact frontmatter is 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
