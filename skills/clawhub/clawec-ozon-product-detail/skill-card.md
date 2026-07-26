## Description: <br>
Queries ClawEC's Ozon product detail API for up to 10 product IDs at a time and helps summarize price, sales, conversion, commission, inventory, and related operating metrics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External ecommerce operators, analysts, and agents use this skill to retrieve Ozon product details by item ID, compare products, and produce Chinese-language product research summaries. It supports SKU-level research, competitor analysis, batch product lookup, and operational review of price, sales, traffic, conversion, commission, fulfillment, and stock signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Ozon product IDs and query parameters to ClawEC's external API. <br>
Mitigation: Use it only when that data sharing is acceptable for the user's workflow and organization. <br>
Risk: API credentials could be exposed if copied into prompts, files, or command history. <br>
Mitigation: Provide the API key through the CLAWEC_API_KEY environment variable and do not hardcode it. <br>
Risk: API responses or product metrics may be unavailable, stale, incomplete, or returned as business-level errors. <br>
Mitigation: Check top-level status, data.success, errorCode, and errorMessage before relying on product analysis. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/anyunzhong/skills/clawec-ozon-product-detail) <br>
- [Ozon Product Detail Response Schema](references/response-schema.md) <br>
- [ClawEC API Base URL](https://www.clawec.com/api) <br>
- [ClawEC API Key Page](https://www.clawec.com/api-key?source=q-clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API calls, Guidance] <br>
**Output Format:** [Markdown summaries with optional bash commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CLAWEC_API_KEY and accepts comma-separated Ozon item IDs, period, sort field, sort direction, and update period.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
