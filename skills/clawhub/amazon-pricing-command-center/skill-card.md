## Description: <br>
Amazon Pricing Command Center analyzes Amazon ASINs with ZooData data to produce RAISE/HOLD/LOWER pricing signals, competitor context, trend summaries, and profit simulations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers and ecommerce operators use this skill to evaluate product pricing, compare category competition, simulate margins, and decide whether to raise, hold, or lower prices for one or more ASINs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Amazon ASINs, category or keyword queries, and related pricing or market-research inputs are sent to ZooData. <br>
Mitigation: Use the skill only with product and market data you are comfortable sending to ZooData. <br>
Risk: The bundled script exposes broader market, review, keyword, monitoring, opportunity, and listing-audit workflows beyond the pricing-focused description. <br>
Mitigation: Invoke only pricing-relevant commands unless you explicitly intend those broader analyses. <br>
Risk: Credential handling can use environment variables or local config files. <br>
Mitigation: Prefer the ZOODATA_API_KEY environment variable and avoid storing API keys in plaintext project files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/apiclaw/skills/amazon-pricing-command-center) <br>
- [ZooData API documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>
- [ZooData homepage](https://zoodata.ai) <br>
- [Repository homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [Field reference](references/reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown reports with tables, shell command invocations, and JSON API results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY; reports should include data provenance and API usage.] <br>

## Skill Version(s): <br>
1.1.3 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
