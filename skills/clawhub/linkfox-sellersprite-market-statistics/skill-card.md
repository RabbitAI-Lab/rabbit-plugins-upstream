## Description: <br>
This skill retrieves SellerSprite category-level Amazon market statistics for a node path, including top-listing averages, price, BSR, sales, seller counts, and new-product indicators. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketplace sellers, analysts, and agents use this skill to evaluate Amazon category market quality and competition from SellerSprite statistics for a known category node path. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys, request details, and session or app identifiers are sent to the configured LinkFox gateway. <br>
Mitigation: Use a dedicated LinkFox API key, check LINKFOX_TOOL_GATEWAY before running, and avoid exposing unrelated sensitive environment variables in the agent session. <br>
Risk: SellerSprite market-statistics calls consume paid credits. <br>
Mitigation: Confirm the query parameters and expected credit use before repeated calls; rely on the built-in 24-hour cache for identical requests. <br>
Risk: Full API responses and cache data are written to local linkfox data directories. <br>
Mitigation: Review the selected output directory and clean stored response or cache files when they contain sensitive commercial research. <br>


## Reference(s): <br>
- [API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-sellersprite-market-statistics) <br>
- [SellerSprite Market Statistics Gateway](https://tool-gateway.linkfox.com/sellersprite/market/statistics) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [JSON response files with stdout JSON or summary text, plus concise Markdown guidance for interpreting the statistics.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LinkFox API credentials; API results are cached for 24 hours and full responses are written under a linkfox session data directory.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
