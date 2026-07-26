## Description: <br>
Retrieves structured Amazon product details for one or more ASINs through the LinkFox Keepa product request API, including pricing, images, listing dates, dimensions, FBA fees, rankings, and optional monthly sales history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers, analysts, and developers use this skill to retrieve and summarize structured product data for specified ASINs across supported Amazon marketplaces. It is suited to price checks, product comparisons, monthly sales trend review, category lookup, dimensions, fees, and other ASIN-level analysis. <br>

### Deployment Geography for Use: <br>
Global, with product queries limited to the supported Amazon marketplaces listed in the skill documentation. <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a LinkFox API key and may make paid product-data requests that consume credits. <br>
Mitigation: Use it only with an approved LinkFox account, confirm credit-consuming lookups before running them, and rely on the 24-hour cache for repeated identical parameters. <br>
Risk: Automatic feedback reporting can send conversation-derived feedback content to LinkFox. <br>
Mitigation: Disable or avoid automatic feedback reporting unless the user explicitly wants that feedback sent, and review feedback content before submission. <br>
Risk: Full API responses are stored locally and cached, which can persist product research data in the workspace. <br>
Mitigation: Run the skill in a trusted workspace and review or clean the linkfox output and cache directories after sensitive analysis. <br>
Risk: LINKFOX_TOOL_GATEWAY can redirect API traffic if set in the environment. <br>
Mitigation: Leave the default gateway in place or set LINKFOX_TOOL_GATEWAY only to a trusted LinkFox-compatible endpoint. <br>


## Reference(s): <br>
- [Keepa API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-keepa-product-request) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown summaries, shell command examples, and saved JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are saved under a local linkfox session data directory; small responses print full JSON, larger responses print summaries unless --inline is used; repeated parameters are cached for 24 hours.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
