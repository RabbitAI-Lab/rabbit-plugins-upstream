## Description: <br>
Returns daily time-series metrics for a single Ozon Russia SKU, including sales, price, stock, rating, and optional search-position or visibility signals for trend, seasonality, and anomaly review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketplace analysts, ecommerce operators, and agents use this skill to inspect the day-by-day performance of one Ozon SKU and identify growth, seasonality, stockouts, price movement, or data gaps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads a LinkFox API key from environment variables and sends requests to external LinkFox services. <br>
Mitigation: Use a scoped API key, keep LINKFOX_TOOL_GATEWAY unset or restricted to a trusted LinkFox endpoint, and run the skill only in environments approved for LinkFox API access. <br>
Risk: Calls may consume paid LinkFox credits and marketplace trend requests can incur a nonzero cost. <br>
Mitigation: Confirm the requested SKU and date window before execution, rely on the documented 24-hour cache for repeated identical calls, and ask before making additional paid lookups. <br>
Risk: Full marketplace API responses are saved locally under the current working directory. <br>
Mitigation: Run the skill in an appropriate project directory and review or clean generated linkfox data and cache folders after use, especially in shared repositories. <br>
Risk: The skill may send feedback reports to LinkFox when quality, mismatch, praise, dissatisfaction, or improvement signals are detected. <br>
Mitigation: Avoid including sensitive user or business data in feedback content and review feedback behavior before enabling the skill in sensitive workflows. <br>


## Reference(s): <br>
- [MPSTATS Ozon 商品趋势 API 参考](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-mpstats-ozon-product-trend) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON, files] <br>
**Output Format:** [Markdown guidance with JSON API responses and saved JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full responses are saved under the current working directory; small responses can also be printed inline, while larger responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
